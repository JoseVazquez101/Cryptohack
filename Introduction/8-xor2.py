#!/usr/bin/python3

from pwn import xor

xor_bytehidden=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for byte in range(256):
	real_key=xor(byte, xor_bytehidden)
	if b'crypto' in real_key:
		key=real_key
		break
print(key)
