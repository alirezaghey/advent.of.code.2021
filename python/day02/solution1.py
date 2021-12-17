#!/usr/bin/env python3

filename = "input1.txt"

with open(filename, "r") as f:
    lines = f.readlines()

horizontal = depth = 0
for line in lines:
    operation, quantity = line.split(" ")
    quantity = int(quantity)
    
    if operation == "forward":
        horizontal += quantity
    elif operation == "down":
        depth += quantity
    else:
        depth -= quantity

print(f'depth: {depth}, horizontal: {horizontal}')
print(f'answer: {depth * horizontal}')