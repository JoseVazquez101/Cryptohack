#!/usr/bin/python3
#MOD 4
x=11*11%29 # Esto impica 5 como residuo, por lo que la raiz modular de 11 es 5
print(x)

for i in range(65535):
    root = i * i % 29
    if root == 18:
        print(root)
        break

prime=29
ints=[14, 6, 11]
for i in range(65535):
    root = i * i % prime
    if root in ints:
        print("Residuo cuadratico: ", root,"\nEntero congruente:", i)
        break

