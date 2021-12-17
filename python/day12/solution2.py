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
small_nodes = [el for el in adj_list if el != "start" and el != "end" and el.islower()]

def backtrack(node, visited, double, path, seen):
    if node == "end":
        if path not in seen:
            seen.add(path)
            return 1
        else:
            return 0
    
    res = 0
    for neigh in adj_list[node]:
        if neigh != "end" and neigh.islower():
            if neigh != double and visited[neigh] == 1:
                continue
            elif visited[neigh] == 2:
                continue
        if neigh == "start":
            continue
        else:
            if neigh != "end" and neigh.islower():
                visited[neigh] += 1
            res += backtrack(neigh, visited, double, path+","+neigh, seen)
        if neigh != "end" and neigh.islower():
            visited[neigh] -= 1
    return res
    
seen = set()
res = sum((backtrack("start", defaultdict(int), double, "start", seen) for double in small_nodes))
print(res)