#!/usr/bin/env python3

import sys
import os
import heapq

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    grid = [list(map(int, list(line.strip()))) for line in f.readlines()]


R, C = len(grid), len(grid[0])
hp = [(0, (0, 0))]
seen = {(0,0): 0}

while hp:
    d, (r, c) = heapq.heappop(hp)
    if r == R-1 and c == C-1:
        print(d)
        break
    
    for nr, nc in ((r-1, c), (r, c+1), (r+1, c), (r, c-1)):
        if 0 <= nr < R and 0 <= nc < C:
            nd = d + grid[nr][nc]
            if (nr, nc) not in seen or seen[(nr, nc)] > nd:
                seen[(nr, nc)] = nd
                heapq.heappush(hp, (nd, (nr, nc)))


