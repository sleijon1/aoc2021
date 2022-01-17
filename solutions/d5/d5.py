from collections import defaultdict
import os
instructions = open(os.getcwd() + "\input.txt").readlines()

def solutions(part_1=False):
    coords = defaultdict(int)
    for row in instructions:
        p1, p2 = row.split(' -> ')
        p1 = [int(c) for c in p1.split(',')]
        p2 = [int(c) for c in p2.split(',')]

        if part_1:
            if p1[0] != p2[0] and p1[1] != p2[1]:
                continue

        inc_i, inc_j = 0, 0
        if p1[0] > p2[0]:
            inc_i = -1
        elif p1[0] < p2[0]:
            inc_i = 1
        if p1[1] > p2[1]:
            inc_j = -1
        elif p1[1] < p2[1]:
            inc_j = 1

        while p1 != p2:
            coords[(p1[0], p1[1])] += 1
            p1 = [p1[0]+inc_i, p1[1]+inc_j]
        coords[(p1[0], p1[1])] += 1
        
    overlapping = len([point for point, val in coords.items() if val >= 2])
    return overlapping

print(f"Solution part 1: {solutions(True)}, part 2: {solutions()}")