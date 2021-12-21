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
    players  = f.read().strip().split("\n")

player_one_pos, player_two_pos = list(map(int, (player[-1] for player in players)))
player_one_score, player_two_score = 0, 0

print(player_one_pos, player_two_pos)
steps = 0
curr_die = 1
player_one_turn = True

while True:
    steps += 3
    curr = 0
    for _ in range(3):
        curr += curr_die
        curr_die = (curr_die + 1) % 100 or 100
    if player_one_turn:
        player_one_pos = (player_one_pos + curr) % 10 or 10
        player_one_score += player_one_pos
        if player_one_score >= 1000:
            print(steps, player_two_score)
            print(steps * player_two_score)
            break
    else:
        player_two_pos = (player_two_pos + curr) % 10 or 10
        player_two_score += player_two_pos
        if player_two_score >= 1000:
            print(steps, player_one_score)
            print(steps * player_one_score)
            break
    player_one_turn = False if player_one_turn else True
    

