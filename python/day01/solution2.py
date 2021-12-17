#!/usr/bin/env python3

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

first, second, third = map(int, lines[:3])
A, B, C = first+second+third, second+third, third
res = 0
for i in range(3, len(lines)):
    num = int(lines[i])
    B, C = B+num, C+num
    if B > A:
        res += 1
    A, B, C = B, C, num

print(res)