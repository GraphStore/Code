# GraphStore-ICDE

以 Execution Topology Graph 思想为核心的最小可运行实现，覆盖 Builder、Indexed Loader、Delta Patcher、Compactor、Sampler、Orchestrator、对象存储与多条 CLI。适合作为 ICDE 论文配套代码仓库与后续工程化的起点。仓库中所有 Python 源码均不含注释，便于评审与匿名化。

---

## TL;DR

- 将模型结构与依赖编码为内容寻址的分块（Chunk）与索引（Index）
- 用流水线装载器按层级并行读取与解析
- 通过增量补丁和 WAL 支持版本演进与可恢复写入
- 附带采样、压缩合并、校验、预取等拓展能力

---

## 环境与安装

**要求**
- Python ≥ 3.9
- Linux 或 macOS

**安装**

```bash
python -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -e .
```

依赖由 `pyproject.toml` 管理（核心：`numpy`、`torch`、`sqlite-utils`）。

---

## 快速上手

### 1) 用示例配置构建

```bash
python -m graphstore.cli.gs_build .gsdemo examples/config.yml
```

输出会在 `.gsdemo/` 生成：
- `objects/`：以内容哈希命名的对象文件
- `manifest.json`：ETG 与索引元数据
- `wal.log`：增量补丁写前日志（后续操作生成）

### 2) 挂载与读取

```bash
python -m graphstore.cli.gs_attach .gsdemo
```

返回包含：
- `chunks`: Chunk 数量
- `index`: 包含 `levels`、`cross`、`groupsig`、`shardmap`

### 3) 跑分

```bash
python -m graphstore.cli.gs_bench .gsdemo 10
```

输出平均装载时延（秒）。

### 4) 合并若干 Chunk

```bash
python -m graphstore.cli.gs_compact .gsdemo CID0 CID1 CID2 CID3
```

返回新的合并后 `CID`。

### 5) 采样与校验

```bash
python -m graphstore.cli.gs_sample .gsdemo CID 8
python -m graphstore.cli.gs_verify .gsdemo CID
```

`gs_sample` 输出子图样本，`gs_verify` 返回 `1` 或 `0`。

---

## 数据与文件格式

### 模型输入 `config.yml` 或 JSON

```yaml
modules:
  - block0
  - block1
params:
  - w0
  - w1
links:
  - ["m0", "m1"]
cap: 2
```

- `modules`: 逻辑模块名，入库时会被编号为 `m0..`
- `params`: 参数名，编号为 `p0..`
- `links`: 以内部 ID 串联的边；示例中 `m0->m1`
- `cap`: 分块容量上限

也可直接提供 JSON 文件，键相同。

### Manifest 结构（`manifest.json`）

```json
{
  "schema": "v1",
  "seals": { "python": "...", "system": "...", "env_hash": "..." },
  "cids": ["<chunk-cid-1>", "<chunk-cid-2>"],
  "index_cid": "<index-cid>",
  "root": "<absolute-path>"
}
```

### 索引结构（由 `index_cid` 指向）

```json
{
  "cross": [["m0","m8"], ["m7","m9"]],
  "levels": {"m0":0, "m1":0, "m8":1},
  "groupsig": {"m0":"...", "p12":"..."},
  "shardmap": {"m0":"...", "p12":"..."}
}
```

- `cross`: 跨 Chunk 的边对
- `levels`: 每个节点的层级
- `groupsig`: 基于节点 ID 与类型的签名
- `shardmap`: 简易分片映射字符串

### 对象存储布局

```
.gsdemo/
├─ objects/
│  ├─ <cid1>
│  ├─ <cid2>
├─ manifest.json
├─ wal.log
```

对象文件内容为 JSON 的字节序列，各对象名即其哈希。

---

## Python API 用法

```python
from graphstore.etg.builder import ETGBuilder
from graphstore.etg.loader import IndexedLoader
from graphstore.etg.delta import DeltaPatcher
from graphstore.etg.compactor import Compactor
from graphstore.storage.object_store import ObjectStore

root = ".gsdemo"
model = {
  "modules": [f"layer{i}" for i in range(64)],
  "params": [f"p{i}" for i in range(64)],
  "links": [[f"m{i}", f"m{i+1}"] for i in range(63)],
  "cap": 4
}

man = ETGBuilder(root).build(model, {}, {})
out = IndexedLoader(root).attach()
mpath = f"{root}/manifest.json"

import json, pathlib
man2 = dict(json.loads(pathlib.Path(mpath).read_text(encoding="utf-8")))
man2["cids"] = list(reversed(man2["cids"]))
DeltaPatcher(root).patch(man2)

c = Compactor(ObjectStore(root))
merged_cid = c.compact(man2["cids"][:4])
```

---

## 架构与核心概念

- 内容寻址：所有 Chunk 与索引对象均由内容计算哈希作为 ID，保证可复现与去重。
- Chunk：节点与边的最小持久化单元，大小受 `cap` 控制。
- Index：跨 Chunk 的依赖、层级、签名与分片映射。
- Builder：生成 Chunk 与 Index，并写出 `manifest.json`。
- Loader：三阶段流水（I/O → 解析 → 组装），并行化装载。
- Delta：比较现有 Manifest 与目标 Manifest 的差异，生成补丁并落盘。
- WAL：两条记录表示事务意图与提交，用于恢复与审计。
- Compactor：将多个 Chunk 合并为一个新对象，降低随机读取。
- Sampler：按给定 `CID` 抽样若干节点与边，便于可视化或调试。
- Runtime Stubs：`nccl_stub.py`、`ds_adapter.py`、`process_group.py`、`rpc_stub.py` 描述并行通信的占位接口，便于后续替换为真实实现。

---

## CLI 参考

```text
gs_build   ROOT MODEL_JSON_OR_YAML      构建 ETG 与索引
gs_attach  ROOT                         读取 manifest 并装载
gs_bench   ROOT REPEAT                  装载多次取平均时延
gs_patch   ROOT TARGET_MANIFEST_JSON    应用增量补丁
gs_compact ROOT CID...                  合并多个 CID 生成新对象
gs_sample  ROOT CID [K]                 抽样 K 个节点与边
gs_verify  ROOT CID                     校验 CID 格式与可解析
gs_inspect MANIFEST_JSON                查看 manifest 概览
```

示例：

```bash
python -m graphstore.cli.gs_build .gsdemo examples/config.yml
python -m graphstore.cli.gs_attach .gsdemo
python -m graphstore.cli.gs_bench .gsdemo 10
python -m graphstore.cli.gs_compact .gsdemo CID0 CID1
python -m graphstore.cli.gs_sample .gsdemo CID0 8
python -m graphstore.cli.gs_verify .gsdemo CID0
```


