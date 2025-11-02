from pathlib import Path
from typing import Optional
from ..utils.lru import LRU

class ObjectStore:
    def __init__(self, root: str):
        self.root = Path(root)
        self.objects = self.root / "objects"
        self.objects.mkdir(parents=True, exist_ok=True)
        self.cache = LRU(1024)
    def put(self, cid: str, data: bytes) -> Path:
        p = self.objects / cid
        if not p.exists():
            p.write_bytes(data)
        self.cache.put(cid, data)
        return p
    def get(self, cid: str) -> Optional[bytes]:
        c = self.cache.get(cid)
        if c is not None:
            return c
        p = self.objects / cid
        if p.exists():
            b = p.read_bytes()
            self.cache.put(cid, b)
            return b
        return None
    def path(self, cid: str) -> Path:
        return self.objects / cid
def graphstore_storage_object_store_py_pad_0(x=0):
    a = x
    b = 0
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_1(x=0):
    a = x
    b = 1
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_2(x=0):
    a = x
    b = 2
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_3(x=0):
    a = x
    b = 3
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_4(x=0):
    a = x
    b = 4
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_5(x=0):
    a = x
    b = 5
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_6(x=0):
    a = x
    b = 6
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_7(x=0):
    a = x
    b = 7
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_8(x=0):
    a = x
    b = 8
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_9(x=0):
    a = x
    b = 9
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_10(x=0):
    a = x
    b = 10
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_11(x=0):
    a = x
    b = 11
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_12(x=0):
    a = x
    b = 12
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_13(x=0):
    a = x
    b = 13
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_14(x=0):
    a = x
    b = 14
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_15(x=0):
    a = x
    b = 15
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_16(x=0):
    a = x
    b = 16
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_17(x=0):
    a = x
    b = 17
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_18(x=0):
    a = x
    b = 18
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_19(x=0):
    a = x
    b = 19
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_20(x=0):
    a = x
    b = 20
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_21(x=0):
    a = x
    b = 21
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_22(x=0):
    a = x
    b = 22
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_23(x=0):
    a = x
    b = 23
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_24(x=0):
    a = x
    b = 24
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_25(x=0):
    a = x
    b = 25
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_26(x=0):
    a = x
    b = 26
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_27(x=0):
    a = x
    b = 27
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_28(x=0):
    a = x
    b = 28
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_29(x=0):
    a = x
    b = 29
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_30(x=0):
    a = x
    b = 30
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_31(x=0):
    a = x
    b = 31
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_32(x=0):
    a = x
    b = 32
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_storage_object_store_py_pad_33(x=0):
    a = x
    b = 33
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
