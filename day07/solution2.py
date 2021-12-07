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
    positions = list(map(int, f.readline().split(",")))

m = max(positions)
best = float("inf")
coord = 0

for i in range(0, m+1):
    res = 0
    for pos in positions:
        res += abs(pos - i)*(abs(pos - i)+1)/2
    if res < best:
        best = res
        coord = i
    else:
        break

print(f'cost: {best}, coord: {coord}')