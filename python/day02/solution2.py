#!/usr/bin/env python3

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

horizontal = depth = aim = 0
for line in lines:
    operation, quantity = line.split(" ")
    quantity = int(quantity)
    
    if operation == "forward":
        horizontal += quantity
        depth += aim * quantity
    elif operation == "down":
        aim += quantity
    else:
        aim -= quantity

print(f'depth: {depth}, horizontal: {horizontal}')
print(f'answer: {depth * horizontal}')