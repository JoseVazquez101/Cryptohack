#!/usr/bin/env python3
from pwn import *
import json
import base64
import binascii
import codecs
import sys

def decode(type, data):
    if type == 'base64':
        return base64.b64decode(data).decode('utf-8')
    elif type == 'hex':
        return binascii.unhexlify(data).decode('utf-8')
    elif type == 'bigint':
        return binascii.unhexlify(data.replace('0x', '')).decode('utf-8')
    elif type == 'rot13':
        return codecs.encode(data, 'rot_13')
    elif type == 'utf-8':
        source = ""
        for char in data:
            source += chr(char)
        return source


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while True:

    received = json_recv()

    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    to_send = {
        "decoded": decode(received["type"], received["encoded"])
    }
    json_send(to_send)
