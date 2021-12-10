#!/usr/bin/env python3

import sys
import os
from functools import reduce

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    lines = [line.strip() for line in f.readlines()]
    
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
pairs = {"(": ")", "[": "]", "{": "}", "<": ">", ")": "(", "]": "[", "}": "{", ">": "<"}

def solve(lines):
    res = 0
    for line in lines:
        stack = []
        for c in line:
            if c in "[{(<":
                stack.append(c)
            elif len(stack):
                if pairs[c] != stack[-1]:
                    res += scores[c]
                    break
                else:
                    stack.pop()
    return res

print(solve(lines))

