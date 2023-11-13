#!/usr/bin/python3
#MOD 3
x=3
y=13
for i in range(65535):
    mod=3*i%13
    if mod == 1:
        print(i)
        break
