#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    parts = f.read().split("\n\n")

cells = parts[0].strip().split(",")
boards = [list([el.strip() for el in line.strip().split(" ") if el != ""] for line in part.split("\n")) for part in parts[1:]]

board_sets = [([set(row) for row in board], [set(col) for col in zip(*board)]) for board in boards]

for cell in cells:
    won = False
    for board in board_sets:
        won = False
        for row in board[0]:
            if cell in row:
                row.remove(cell)
                if len(row) == 0:
                    won = True
        for col in board[1]:
            if cell in col:
                col.remove(cell)
                if len(col) == 0:
                    won = True
        if won:
            res = 0
            for row in board[0]:
                res += sum(map(int, row))
            print(res * int(cell))
            break
    if won:
        break