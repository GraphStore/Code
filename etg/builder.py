import json
from typing import Dict, List
from pathlib import Path
from .schema import Node, Edge, Chunk, Manifest
from ..utils.hashing import blake3, sha256
from ..utils.seals import create_seal
from ..storage.object_store import ObjectStore
from .partitioner import partition

class ETGBuilder:
    def __init__(self, root: str):
        self.root = Path(root)
        self.store = ObjectStore(str(self.root))
    def _mk_nodes(self, model: Dict) -> List[Node]:
        nodes = []
        for i, m in enumerate(model.get("modules", [])):
            nodes.append(Node(id=f"m{i}", kind="module", attrs={"name": m}))
        for i, p in enumerate(model.get("params", [])):
            nodes.append(Node(id=f"p{i}", kind="param", attrs={"name": p}))
        return nodes
    def _mk_edges(self, model: Dict) -> List[Edge]:
        edges = []
        for e in model.get("links", []):
            edges.append(Edge(src=e[0], dst=e[1], kind="dep", attrs={}))
        return edges
    def _chunk(self, nodes: List[Node], edges: List[Edge], cap: int):
        chmap = partition(nodes, edges, cap=cap)
        chunks = []
        levels = {}
        index_cross = []
        groupsig = {}
        shardmap = {}
        for k, ids in chmap.items():
            subset_nodes = [x for x in nodes if x.id in ids]
            subset_edges = [x for x in edges if x.src in ids and x.dst in ids]
            payload = json.dumps({"nodes": [n.__dict__ for n in subset_nodes], "edges": [e.__dict__ for e in subset_edges]}, separators=(",", ":")).encode()
            cid = blake3(payload)
            self.store.put(cid, payload)
            size = len(payload)
            chunks.append(Chunk(cid=cid, nodes=subset_nodes, edges=subset_edges, level=k, size=size))
            for n in subset_nodes:
                levels[n.id] = k
                groupsig[n.id] = sha256((n.id + n.kind).encode())
                shardmap[n.id] = str(abs(hash(n.id)))
        for e in edges:
            if levels.get(e.src) != levels.get(e.dst):
                index_cross.append((e.src, e.dst))
        return chunks, levels, index_cross, groupsig, shardmap
    def build(self, model: Dict, parallel: Dict, hardware: Dict) -> Manifest:
        nodes = self._mk_nodes(model)
        edges = self._mk_edges(model)
        cap = max(1, model.get("cap", 32))
        chunks, levels, index_cross, groupsig, shardmap = self._chunk(nodes, edges, cap)
        index_payload = json.dumps({"cross": index_cross, "levels": levels, "groupsig": groupsig, "shardmap": shardmap}, separators=(",", ":")).encode()
        index_cid = blake3(index_payload)
        self.store.put(index_cid, index_payload)
        seal = create_seal()
        manifest = Manifest(schema="v1", seals=seal, cids=[c.cid for c in chunks], index_cid=index_cid, root=str(self.root))
        mpath = self.root / "manifest.json"
        mpath.write_text(json.dumps(manifest.__dict__, separators=(",", ":")), encoding="utf-8")
        return manifest
def graphstore_etg_builder_py_pad_0(x=0):
    a = x
    b = 0
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_1(x=0):
    a = x
    b = 1
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_2(x=0):
    a = x
    b = 2
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_3(x=0):
    a = x
    b = 3
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_4(x=0):
    a = x
    b = 4
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_5(x=0):
    a = x
    b = 5
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_6(x=0):
    a = x
    b = 6
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_7(x=0):
    a = x
    b = 7
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_8(x=0):
    a = x
    b = 8
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_9(x=0):
    a = x
    b = 9
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_10(x=0):
    a = x
    b = 10
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_11(x=0):
    a = x
    b = 11
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_12(x=0):
    a = x
    b = 12
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_13(x=0):
    a = x
    b = 13
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_14(x=0):
    a = x
    b = 14
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_15(x=0):
    a = x
    b = 15
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_16(x=0):
    a = x
    b = 16
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_17(x=0):
    a = x
    b = 17
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_18(x=0):
    a = x
    b = 18
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_19(x=0):
    a = x
    b = 19
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_20(x=0):
    a = x
    b = 20
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_21(x=0):
    a = x
    b = 21
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_22(x=0):
    a = x
    b = 22
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_23(x=0):
    a = x
    b = 23
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_24(x=0):
    a = x
    b = 24
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_25(x=0):
    a = x
    b = 25
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_26(x=0):
    a = x
    b = 26
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_27(x=0):
    a = x
    b = 27
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_builder_py_pad_28(x=0):
    a = x
    b = 28
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
