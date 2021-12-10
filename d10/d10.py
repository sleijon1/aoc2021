import os
instructions = open(os.getcwd() + "\input.txt").read().splitlines()

syn_map = {')': 3, ']': 57, '}': 1197, '>': 25137,}
synp2_map = {')': 1, ']': 2, '}': 3, '>': 4}
open = ['[', '{', '<', '(']
close = [']', '}', '>', ')']
matching = {'}': '{', ']': '[', '>': '<', ')':'('}
matching_rev = {'{': '}', '[': ']', '<': '>', '(':')'}

def syntax_check(syn, i=0, opened=[]):
    try:
        if syn[i] in open:
            opened.insert(0, syn[i])
            return syntax_check(syn, i+1, opened)
        elif syn[i] in close:
            if syn[i-1] == matching[syn[i]]:
                syn.pop(i-1)
                syn.pop(i-1)
                opened.pop(0)
                return syntax_check(syn, i-1, opened)
            else:
                return True, syn[i], opened
    except IndexError:
        # unfinished parentheses
        return False, None, opened

error_score = 0
fix_scores = []
for syn_row in instructions:
    error, unmatched, opened = syntax_check(list(syn_row), opened=[])
    if error:
        error_score += syn_map[unmatched]
    else:
        match_close = [matching_rev[op] for op in opened]
        total_score = 0
        for brack in match_close:
            total_score *= 5
            total_score += synp2_map[brack]
        fix_scores.append(total_score)

print(f"part 1: {error_score}, part 2: {sorted(fix_scores)[(len(fix_scores)-1)//2]}")