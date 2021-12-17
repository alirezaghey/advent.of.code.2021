#!/usr/bin/env python3

import sys
import os
from functools import reduce

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = f.readlines()

grid = []
for line in lines:
    grid.append(list(map(int, line.strip())))

R, C = len(grid), len(grid[0])
res = 0
for r in range(R):
    for c in range(C):
        is_lowest = reduce(
            lambda acc, el: acc & el,
            [grid[r][c] < grid[dr+r][dc+c]  if 0 <= r+dr < R and 0 <= c+dc < C else True
             for (dr,dc) in ((-1, 0), (0, 1), (1, 0), (0, -1))], True
            )
        if is_lowest:
            res += grid[r][c]+1

print(res)
