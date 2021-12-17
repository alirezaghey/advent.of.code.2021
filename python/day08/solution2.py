#!/usr/bin/env python3

import sys
import os
from collections import defaultdict, Counter

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

len_uniques = {2: 1, 4: 4, 3: 7, 7: 8}
res = 0
for code, digit in zip(codes, digits):
    mapping_uniques = {}
    counter_chars = Counter()
    for c in code:
        counter_chars.update(c)
        if len(c) in len_uniques:
            mapping_uniques[len_uniques[len(c)]] = c
    
    mapping_chars = {}
    for c, v in counter_chars.items():
        if v == 9:
            mapping_chars['c'] = c 
        elif v == 8:
            if c not in mapping_uniques[1]:
                mapping_chars['a'] = c
            else:
                mapping_chars['b'] = c
        elif v == 7:
            if c not in mapping_uniques[4]:
                mapping_chars['d'] = c
            else:
                mapping_chars['g'] = c
        elif v == 6:
            mapping_chars['f'] = c
        elif v == 4:
            mapping_chars['e'] = c
    temp_res = ""
    for d in digit:
        if len(d) in len_uniques:
            temp_res += str(len_uniques[len(d)])
        elif len(d) == 5:
            if mapping_chars['e'] in d:
                temp_res += "2"
            elif mapping_chars['b'] in d:
                temp_res += "3"
            else:
                temp_res += "5"
        else:
            if mapping_chars['g'] not in d:
                temp_res += "0"
            elif mapping_chars['b'] in d:
                temp_res += "9"
            else:
                temp_res += "6"
    res += int(temp_res)

print(res)
