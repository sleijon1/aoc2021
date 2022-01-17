import os
from collections import defaultdict

if __name__== '__main__':
    instructions = open(os.getcwd() + "\input.txt").read().splitlines()
    polymer = instructions[0]
    rep_dict = {row.split(' -> ')[0]:row.split(' -> ')[1] for row in instructions[2:]}
    pairs = defaultdict(int)
    counts = defaultdict(int)
    for i in range(len(polymer)-1):
        pairs[polymer[i]+polymer[i+1]] += 1
        counts[polymer[i]] += 1
    counts[polymer[i+1]] += 1
    for step in range(40):
        for pair, count in list(pairs.items()):
            mid = rep_dict[pair]
            counts[mid] += count
            pairs[pair[0]+mid] += count
            pairs[mid+pair[1]] += count
            pairs[pair] -= count
        if step in (9, 39):
            sort = list(sorted(counts.items(), key=lambda x: x[1]))
            print(f"Part {1 if step == 9 else 2}: {sort[-1][1] - sort[0][1]}")
    
    