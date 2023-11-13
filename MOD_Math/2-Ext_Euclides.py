#!/usr/bin/python3
def MCD(a, b):
    if a == 0:
        return b, 0, 1
    mcd, U, V = MCD(b % a, a)
    u = V - (b // a) * U
    v = U
    return mcd, u, v

p = int(input("Num 1: "))
q = int(input("Num 2: "))

mcd, u, v = MCD(p, q)

print(f"MCD({p}, {q}) = {mcd}")
print(f"u = {u}, v = {v}")
