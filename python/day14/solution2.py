#!/usr/bin/env python3

import sys
import os
from collections import Counter
import math

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
polymer_counter = Counter()
for i in range(len(polymer)-1):
    polymer_counter["".join(polymer[i:i+2])] += 1


for _ in range(40):
    new_polymer_counter = Counter()
    for key in polymer_counter:
        char = rules[key]
        new_polymer_counter[key[0]+char] += polymer_counter[key]
        new_polymer_counter[char+key[1]] += polymer_counter[key]
    polymer_counter = new_polymer_counter

letter_counter = Counter()
print(polymer_counter)
vals = list(sorted(polymer_counter.values()))
print(vals[-1] - vals[0])

for key in polymer_counter:
    letter_counter[key[0]] += polymer_counter[key]
    letter_counter[key[1]] += polymer_counter[key]

print(letter_counter)
for key in letter_counter:
    print(f'{key}: {letter_counter[key]}, {letter_counter[key]/2}')

for key in letter_counter:
    letter_counter[key] = math.ceil(letter_counter[key]/2)

vals = list(sorted(letter_counter.values()))
print(vals[-1] - vals[0])