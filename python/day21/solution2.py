#!/usr/bin/env python3

import sys
import os
from itertools import product
from functools import cache

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

print(player_one_pos, player_two_pos)
sums_of_dies = list(map(sum, product(range(1,4), repeat=3)))

@cache
def dfs(player1, pos1, player2, pos2, turn):
    if player1 >= 21:
        return (1, 0)
    if player2 >= 21:
        return (0, 1)
    
    score_player1, score_player2 = 0, 0
    for die in sums_of_dies:
        if turn:
            one, two = dfs(
                player1+((pos1 + die) % 10 or 10), (pos1 + die) % 10 or 10,
                player2, pos2, False)
            score_player1, score_player2 = score_player1+one, score_player2+two
        else:
            one, two = dfs(
                player1, pos1,
                player2+((pos2 + die) % 10 or 10), (pos2 + die) % 10 or 10, True)
            score_player1, score_player2 = score_player1+one, score_player2+two
    return (score_player1, score_player2)

res = dfs(0, player_one_pos, 0, player_two_pos, True)
if res[0] > res[1]:
    print(f'Player one wins with {res[0]} universes while Player two has {res[1]}')
else:
    print(f'Player two wins with {res[1]} universes while Player one has {res[0]}')