#!/usr/bin/python3

from Crypto.Util.number import *

numero = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"
hex_value = hex(int(numero))[2:] #convertir el numero a hex
decoded_bytes = bytes.fromhex(hex_value) #convert de hex a bytes
decoded_string = decoded_bytes.decode('utf-8') #decodificar bytes a ascii

print(decoded_string)
