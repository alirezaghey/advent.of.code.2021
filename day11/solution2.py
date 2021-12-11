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
    lines = [line.strip() for line in f.readlines()]
    
grid = [list(map(int, list(line))) for line in lines]
R, C = len(grid), len(grid[0])

for step in range(1, 1000):
    exploded = []
    seen = set()
    for r, c in [(r, c) for r in range(R) for c in range(C)]:
        grid[r][c] += 1
        if grid[r][c] > 9:
            exploded.append((r, c))
            seen.add((r, c))
    while exploded:
        new_exploded = []
        for r, c in exploded:
            for nr, nc in [(r+dr, c+dc)  for dr in range(-1, 2) for dc in range(-1, 2) if (dr, dc) != (0, 0)]:
                if 0 <= nr < R and 0 <= nc < C:
                    grid[nr][nc] += 1
                    if grid[nr][nc] > 9 and (nr, nc) not in seen:
                        new_exploded.append((nr, nc))
                        seen.add((nr, nc))
        exploded = new_exploded
        
    for r, c in seen:
        grid[r][c] = 0
    
    if all(all(x == 0 for x in row) for row in grid):
        print(step)
        break