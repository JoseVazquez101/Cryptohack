#!/usr/bin/python3
num1=int(input("Num 1: "))
num2=int(input("Num 2: "))
primo1=[]
primo2=[]
for i in range(1, num1):
    value=num1 % i
    if value == 0:
        primo1.append(i)
for i in range(1, num2):
    value=num2 % i
    if value == 0:
        primo2.append(i)
str_num1 = ''.join(str(num) for num in primo1)
str_num2 = ''.join(str(num) for num in primo2)
mcd = max(set(primo1) & set(primo2))
print("MCD: ", mcd)
