#!/usr/bin/env python3

import sys
import os
from collections import namedtuple

if len(sys.argv) != 2:
    print("Usage: ./solution1.py <input_file>")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("Error: no such file:", sys.argv[1])
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    parts = f.readline().strip().split(",")

x_min, x_max = list(map(int, parts[0][parts[0].find("x=")+2:].split("..")))
y_min, y_max = list(map(int, parts[1][parts[1].find("y=")+2:].split("..")))

print(x_min, x_max)
print(y_min, y_max)

Point = namedtuple("Point", ["x", "y"])
Velocity = namedtuple("Velocity", ["x", "y"])
res = 0

for x, y in ((x, y) for x in range(200) for y in range(-200, 200)):
    vel = Velocity(x, y)
    coord = Point(0, 0)

    while True:
        coord = Point(coord.x + vel.x, coord.y + vel.y)
        vel = Velocity(vel.x - 1 if vel.x > 0 else 0, vel.y - 1)

        if coord.x > x_max or coord.y < y_min:
            break
        if x_min <= coord.x <= x_max and y_min <= coord.y <= y_max:
            res += 1
            break

print(res)