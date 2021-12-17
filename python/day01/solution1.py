#!/usr/bin/env python3

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

res = 0
prev_line = int(lines[0])
for i in range(1, len(lines)):
    line = int(lines[i])
    if line > prev_line:
        res += 1
    prev_line = line

print(res)