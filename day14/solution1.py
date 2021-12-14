#!/usr/bin/env python3

import sys
import os
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    parts = list(map(str.strip, f.read().split("\n\n")))

polymer = list(parts[0].strip())
rules = {key.strip() : val.strip() for key, val in
            (line.split(" -> ") for line in parts[1].split("\n"))}

for _ in range(10):
    new_polymer = []
    for i in range(len(polymer)-1):
        curr = "".join(polymer[i:i+2])
        char = rules[curr]
        new_polymer.extend([curr[0], char])
    new_polymer.append(polymer[-1])
    polymer = new_polymer

counter = Counter(polymer)
vals = list(sorted(counter.values()))
print(vals[-1] - vals[0])
