#!/usr/bin/python3

import base64

hex_decode=bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
base64_encoded = base64.b64encode(hex_decode).decode('utf-8')

print("Encoded Base64:", base64_encoded)
