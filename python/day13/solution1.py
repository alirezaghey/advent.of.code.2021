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
    parts = list(map(str.strip, f.read().split("\n\n")))

lines = parts[0].split("\n")
coords = set()
for line in lines:
    x, y = line.split(",")
    coords.add((int(x), int(y)))

folds = []
for line in parts[1].split("\n"):
    axis, qty = line.split(" ")[2].split("=")
    folds.append((axis.strip(), int(qty)))

def fold_y(coords, r_val):
    new_coords = set()
    for c, r in coords:
        if r > r_val:
            new_coords.add((c, 2*r_val - r))
        else:
            new_coords.add((c, r))
    return new_coords

def fold_x(coords, c_val):
    new_coords = set()
    for c, r in coords:
        if c > c_val:
            new_coords.add((2*c_val - c, r))
        else:
            new_coords.add((c, r))
    return new_coords

new_coords = fold_x(coords, folds[0][1])
print(len(new_coords))