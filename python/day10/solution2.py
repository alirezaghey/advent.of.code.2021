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
    
scores = {"(": 1, "[": 2, "{": 3, "<": 4}
pairs = {"(": ")", "[": "]", "{": "}", "<": ">", ")": "(", "]": "[", "}": "{", ">": "<"}

def calc_line_score(line):
    stack = []
    res = 0
    for c in line:
        if c in "[{(<":
            stack.append(c)
        elif len(stack):
            if pairs[c] == stack[-1]:
                stack.pop()
    while stack:
        res *= 5
        res += scores[stack.pop()]
    return res

def solve(lines):
    res = []
    for line in lines:
        stack = []
        for c in line:
            if c in "[{(<":
                stack.append(c)
            elif len(stack):
                if pairs[c] !=  stack[-1]:
                    break
                else:
                    stack.pop()
        else:
            res.append(calc_line_score(line))
    res.sort()
    return res[len(res)//2]


print(solve(lines))