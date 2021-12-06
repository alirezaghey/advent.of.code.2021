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

fishes = defaultdict(int)
with open(filename, "r") as f:
    els = f.readline().split(",")

for el in els:
    fishes[int(el)] += 1

for i in range(256):
    new_fish = defaultdict(int)
    for fish in fishes:
        if fish == 0:
            new_fish[8] += fishes[fish]
            new_fish[6] += fishes[fish]
        else:
            new_fish[fish - 1] += fishes[fish]
    fishes = new_fish 

print(sum(fishes.values()))