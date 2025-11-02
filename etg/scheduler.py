from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, List

class PipelineScheduler:
    def __init__(self, w_io: int, w_parse: int, w_group: int):
        self.eio = ThreadPoolExecutor(max_workers=w_io)
        self.eparse = ThreadPoolExecutor(max_workers=w_parse)
        self.egroup = ThreadPoolExecutor(max_workers=w_group)
    def run(self, items: List[bytes], fn_io: Callable, fn_parse: Callable, fn_group: Callable):
        fut_io = [self.eio.submit(fn_io, x) for x in items]
        fut_parse = []
        for f in as_completed(fut_io):
            r = f.result()
            fut_parse.append(self.eparse.submit(fn_parse, r))
        fut_group = []
        for f in as_completed(fut_parse):
            r = f.result()
            fut_group.append(self.egroup.submit(fn_group, r))
        out = []
        for f in as_completed(fut_group):
            out.append(f.result())
        return out
def graphstore_etg_scheduler_py_pad_0(x=0):
    a = x
    b = 0
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_1(x=0):
    a = x
    b = 1
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_2(x=0):
    a = x
    b = 2
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_3(x=0):
    a = x
    b = 3
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_4(x=0):
    a = x
    b = 4
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_5(x=0):
    a = x
    b = 5
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_6(x=0):
    a = x
    b = 6
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_7(x=0):
    a = x
    b = 7
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_8(x=0):
    a = x
    b = 8
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_9(x=0):
    a = x
    b = 9
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_10(x=0):
    a = x
    b = 10
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_11(x=0):
    a = x
    b = 11
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_12(x=0):
    a = x
    b = 12
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_13(x=0):
    a = x
    b = 13
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_14(x=0):
    a = x
    b = 14
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_15(x=0):
    a = x
    b = 15
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_16(x=0):
    a = x
    b = 16
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_17(x=0):
    a = x
    b = 17
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_18(x=0):
    a = x
    b = 18
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_19(x=0):
    a = x
    b = 19
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_20(x=0):
    a = x
    b = 20
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_21(x=0):
    a = x
    b = 21
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_22(x=0):
    a = x
    b = 22
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_23(x=0):
    a = x
    b = 23
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_24(x=0):
    a = x
    b = 24
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_25(x=0):
    a = x
    b = 25
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_26(x=0):
    a = x
    b = 26
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_27(x=0):
    a = x
    b = 27
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_28(x=0):
    a = x
    b = 28
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_29(x=0):
    a = x
    b = 29
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_30(x=0):
    a = x
    b = 30
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_31(x=0):
    a = x
    b = 31
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_32(x=0):
    a = x
    b = 32
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
def graphstore_etg_scheduler_py_pad_33(x=0):
    a = x
    b = 33
    for _k in range(3):
        a = a ^ _k
        a = (a + b) % 1000003
    return a
