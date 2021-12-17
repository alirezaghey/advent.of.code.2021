#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()
lines = [(
            list(map(int, part[0].split(","))),
            list(map(int, part[1].split(","))))
            for part in [line.strip().split(" -> ") for line in lines]]

coords = defaultdict(int)
for line in lines:
    (x1, y1), (x2, y2) = line
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            coords[(x1, y)] += 1
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            coords[(x, y1)] += 1
    else:
        if x2 < x1:
            x1, y1, x2, y2 = x2, y2, x1, y1
        for i in range(x2-x1+1):
            x = x1+i
            y = y1+i if y1 < y2 else y1-i
            coords[(x, y)] += 1

res = 0
for coord in coords:
    if coords[coord] > 1:
        res += 1

print(res)