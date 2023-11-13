#!/usr/bin/python3

from pwn import xor

"""
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313 --> Key1, valor real en hex
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e --> Esta no importa porque ya tenemos KEY1 xd
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1  --> KEY2 xor KEY3, ya tenemos de KEY 1 a 3
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf  --> xor de KEY 1 a 3 con FLAG, genera FLAG inversa
"""
KEY1=bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_KEY3=bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_KEY1_KEY2_KEY3=bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

FLAG=(xor(KEY1, KEY2_KEY3, FLAG_KEY1_KEY2_KEY3)) #Con este xor se anulan las keys dejando solo a la FLAG, pues KEY1 xor KEY1 = 0
print(FLAG)
