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
    lines = [line.strip() for line in f.readlines()]

adj_list = defaultdict(list)
for line in lines:
    u, v = list(map(str.strip, (line.split("-"))))
    adj_list[u].append(v)
    adj_list[v].append(u)

def backtrack(node, visited):
    if node == "end":
        return 1
    
    res = 0
    for neigh in adj_list[node]:
        if neigh != "end" and neigh.islower() and neigh in visited:
            continue
        if neigh == "start":
            continue
        else:
            if neigh != "end" and neigh.islower():
                visited.add(neigh)
            res += backtrack(neigh, visited)
        if neigh != "end" and neigh.islower():
            visited.remove(neigh)
    return res
    
res = backtrack("start", set())
print(res)