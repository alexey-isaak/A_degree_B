import random

A = input("Введите число А: ")
B = input("Введите число B - степнь числа А: ")


def degree(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    else:
        return a * degree(a, b - 1)


print(degree(int(A), int(B)))
