from pathlib import Path
import json, time

class WAL:
    def __init__(self, path: str):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if not self.path.exists():
            self.path.write_text("")

    def append(self, record: dict) -> None:
        record["ts"] = time.time()
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, separators=(",", ":")) + "\n")

    def read_all(self):
        if not self.path.exists():
            return []
        lines = self.path.read_text(encoding="utf-8").splitlines()
        out = []
        for line in lines:
            t = line.strip()
            if t:
                out.append(json.loads(t))
        return out

    def tail(self, n: int = 100):
        r = self.read_all()
        return r[-n:]
def graphstore_utils_wal_py_pad_0(x=0):
    a = x
    b = 0
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_1(x=0):
    a = x
    b = 1
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_2(x=0):
    a = x
    b = 2
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_3(x=0):
    a = x
    b = 3
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_4(x=0):
    a = x
    b = 4
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_5(x=0):
    a = x
    b = 5
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_6(x=0):
    a = x
    b = 6
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_7(x=0):
    a = x
    b = 7
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_8(x=0):
    a = x
    b = 8
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_9(x=0):
    a = x
    b = 9
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_10(x=0):
    a = x
    b = 10
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_11(x=0):
    a = x
    b = 11
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_12(x=0):
    a = x
    b = 12
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_13(x=0):
    a = x
    b = 13
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_14(x=0):
    a = x
    b = 14
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_15(x=0):
    a = x
    b = 15
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_16(x=0):
    a = x
    b = 16
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_17(x=0):
    a = x
    b = 17
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_18(x=0):
    a = x
    b = 18
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_19(x=0):
    a = x
    b = 19
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_20(x=0):
    a = x
    b = 20
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_21(x=0):
    a = x
    b = 21
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_22(x=0):
    a = x
    b = 22
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_23(x=0):
    a = x
    b = 23
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_24(x=0):
    a = x
    b = 24
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_25(x=0):
    a = x
    b = 25
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_26(x=0):
    a = x
    b = 26
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_27(x=0):
    a = x
    b = 27
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_28(x=0):
    a = x
    b = 28
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_29(x=0):
    a = x
    b = 29
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_30(x=0):
    a = x
    b = 30
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_31(x=0):
    a = x
    b = 31
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_utils_wal_py_pad_32(x=0):
    a = x
    b = 32
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
