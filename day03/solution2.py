#!/usr/bin/env python3

from collections import defaultdict

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

s_oxygen = set()
s_scrubber = set()
for line in lines:
    s_oxygen.add(line)
    s_scrubber.add(line)

i = 0
while len(s_oxygen) > 1:
    b = 0
    for num in s_oxygen:
        if num[i] == '1':
            b += 1
        else:
            b -= 1
    temp_oxygen = s_oxygen.copy()
    if b >= 0:
        for el in s_oxygen:
            if el[i] != '0':
                temp_oxygen.remove(el)
    else:
        for el in s_oxygen:
            if el[i] != '1':
                temp_oxygen.remove(el)
    s_oxygen = temp_oxygen
    i += 1

i = 0
while len(s_scrubber) > 1:
    b = 0
    for num in s_scrubber:
        if num[i] == '1':
            b += 1
        else:
            b -= 1
    temp_scrubber = s_scrubber.copy()
    if b >= 0:
        for el in s_scrubber:
            if el[i] != '1':
                temp_scrubber.remove(el)
    else:
        for el in s_scrubber:
            if el[i] != '0':
                temp_scrubber.remove(el)
    s_scrubber = temp_scrubber
    i += 1

print(f'oxygen: {s_oxygen}, scrubber: {s_scrubber}')
oxygen = s_oxygen.pop()
scrubber = s_scrubber.pop()
oxygen = int(oxygen, 2)
scrubber = int(scrubber, 2)
print(f'power consumption: {oxygen * scrubber}')
