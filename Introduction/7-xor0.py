#!/usr/bin/python3

from pwn import xor

xor_convert=(xor(b'label', 13))
print(xor_convert)
