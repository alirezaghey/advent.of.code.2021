#!/usr/bin/env python3

import sys
import os

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)


def calc_pixel(r, c, image, algo, inf):
    R, C = len(image), len(image[0])
    address = ""
    for dr, dc in ((dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)):
        nr, nc = dr+r, dc+c
        if 0 <=nr < R and 0 <= nc < C:
            address += "0" if image[nr][nc] == "." else "1"
        elif inf == ".":
            address += "0"
        else:
            address += "1"
    return algo[int(address, 2)]

def calc_image(image, n):
    inf = "."
    R, C = len(image), len(image[0])
    for _ in range(n):
        new_image = [["."]*(C+2) for _ in range(R+2)]
        R, C = R+2, C+2
        for r in range(R):
            for c in range(C):
                new_image[r][c] = calc_pixel(r-1, c-1, image, algo, inf)
        image = new_image        
                
        if inf == ".":
            inf = algo[0]
        else:
            inf = algo[-1]
    return image

filename = sys.argv[1]

with open(filename, "r") as f:
    parts = f.read().strip().split("\n\n")

algo = list(map(str.strip, parts[0]))
image = [row for row in list(map(str.strip, parts[1].split("\n")))]

part_one = calc_image(image, 2)
part_two = calc_image(image, 50)

res_part_one = sum(sum(1 if el == "#" else 0 for el in row) for row in part_one)
res_part_two = sum(sum(1 if el == "#" else 0 for el in row) for row in part_two)

print(f'Part one result: {res_part_one}')
print(f'Part two result: {res_part_two}')