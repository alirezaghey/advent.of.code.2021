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

boards_that_won = set()
last = -1
for cell in cells:
    won = False
    for idx, board in enumerate(board_sets):
        won = False
        if idx in boards_that_won: continue
        for row in board[0]:
            if cell in row:
                row.remove(cell)
                if len(row) == 0:
                    won = True
                    boards_that_won.add(idx)
                    break
        for col in board[1]:
            if cell in col:
                col.remove(cell)
                if len(col) == 0:
                    won = True
                    boards_that_won.add(idx)
        if len(boards_that_won) == len(board_sets):
            last = idx
            break
    if len(boards_that_won) == len(board_sets):
        res = 0
        for row in board_sets[last][0]:
            res += sum(map(int, row))
        print(res * int(cell))
        exit()