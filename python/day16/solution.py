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
    hex_input = f.readline().strip()

def parse(curr, bits, node):
    v = int(bits[curr:curr+3], 2)
    curr += 3
    t = int(bits[curr:curr+3], 2)
    curr += 3
    
    node["v"] = v
    node["t"] = t

    if t == 4:
        return parse_literal(curr, bits, node)
    else:
        return parse_operand(curr, bits, node)


def parse_operand(curr, bits, node):
    z = int(bits[curr], 2)
    curr += 1

    if z == 1:
        return parse_operand_one(curr, bits, node)
    else:
        return parse_operand_zero(curr, bits, node)


def parse_operand_zero(curr, bits, node):
    length_of_subpackets = int(bits[curr: curr+15], 2)
    curr += 15
    pos = curr
    node["kids"] = []
    while pos < curr+length_of_subpackets: 
        node["kids"].append({})
        pos  = parse(pos, bits, node["kids"][-1])

    return curr+length_of_subpackets


def parse_operand_one(curr, bits, node):
    num_of_packets = int(bits[curr:curr+11], 2)
    curr += 11
    
    node["kids"] = []
    for _ in range(num_of_packets):
        node["kids"].append({})
        curr = parse(curr, bits, node["kids"][-1])
    
    return curr

def parse_literal(curr, bits, node):
    last = False
    all = ""
    while last == False:
        piece = bits[curr:curr+5]
        curr += 5
        if piece[0] == "0":
            last = True
        all += piece[1:]
    node["val"] = int(all, 2)
    return curr

def hex_to_bin(hex):
    the_len = len(hex)*4
    binary = bin(int(hex, 16))[2:]
    binary = "0"*(the_len - len(binary)) + binary
    return binary

def calc_v(node):
    res = 0
    if "v" in node:
        res += node["v"]
    if "kids" in node:
        for kid in node["kids"]:
            res += calc_v(kid)
    return res

def calc_tree_value(node):
    if node["t"] == 4:
        return node["val"]
    
    if node["t"] == 0: 
        return sum(calc_tree_value(kid) for kid in node["kids"])
    if node["t"] == 1:
        res = 1
        for kid in node["kids"]:
            res *= calc_tree_value(kid)
        return res
    if node["t"] == 2: 
        res = float("inf")
        for kid in node["kids"]:
            res = min(res, calc_tree_value(kid))
        return res
    if node["t"] == 3:
        res = float("-inf")
        for kid in node["kids"]:
            res = max(res, calc_tree_value(kid))
        return res
    if node["t"] == 5:
        first = calc_tree_value(node["kids"][0])
        second = calc_tree_value(node["kids"][1])
        return 1 if first > second else 0
    if node["t"] == 6:
        first = calc_tree_value(node["kids"][0])
        second = calc_tree_value(node["kids"][1])
        return 1 if first < second else 0
    if node["t"] == 7:
        first = calc_tree_value(node["kids"][0])
        second = calc_tree_value(node["kids"][1])
        return 1 if first == second else 0

tree = {}
parse(0, hex_to_bin(hex_input), tree)
print(calc_v(tree))
print(calc_tree_value(tree))

