#!/usr/bin/env python3

import sys
import os
from collections import deque
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

def solve():
    res = []
    for r in range(R):
        for c in range(C):
            is_lowest = reduce(
                lambda acc, el: acc & el,
                [grid[r][c] < grid[r+dr][c+dc] if 0 <= r+dr < R and 0 <= c+dc < C else True
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1))],
                True
            )
            if is_lowest:
                res.append(bfs(r, c))
    res.sort(reverse=True)
    print(res[0]*res[1]*res[2])

def bfs(r, c):
    deq = deque([(r, c)])
    seen = set([(r, c)])
    while deq:
        rr, cc = deq.popleft()
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if rr+dr < 0 or rr+dr >= R or cc+dc < 0 or cc+dc >= C or (rr+dr, cc+dc) in seen or grid[rr+dr][cc+dc] == 9:
                continue
            deq.append((rr+dr, cc+dc))
            seen.add((rr+dr, cc+dc))
    return len(seen)

solve()