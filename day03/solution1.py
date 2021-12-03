#!/usr/bin/env python3

from collections import defaultdict

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

dic = defaultdict(int)
for line in lines:
    for i in range(len(line)):
        if line[i] == '1':
            dic[i] += 1
        else:
            dic[i] -= 1
gama = epsilon = 0
for i in range(12):
    if dic[i] > 0:
        gama <<= 1
        epsilon <<= 1
        gama += 1
    else:
        gama <<= 1
        epsilon <<= 1
        epsilon += 1

print(f'gama: {gama}, epsilon: {epsilon}')
print(f'power consumption: {gama * epsilon}')
