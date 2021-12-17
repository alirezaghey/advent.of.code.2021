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
    lines = [list(map(str.strip, line.split("|"))) for line in f.readlines()]

codes, digits = [], []
for line in lines:
    codes.append(list(filter(lambda x: x.strip() != "", line[0].split(" "))))
    digits.append(list(filter(lambda x: x.strip() != "", line[1].split(" "))))
print(codes, digits)
uniques = {2: 1, 4: 4, 3: 7, 7: 8}
res = 0
for digit in digits:
    for d in digit:
        if len(d) in uniques:
            res += 1

print(res)