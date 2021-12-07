import os
instructions = open(os.getcwd() + "\input.txt").read()
fishies = [int(fish) for fish in instructions.split(',')]

def run_sim(num_sim, fishies):
    groups = [0 for _ in range(9)]
    # init groups
    for fish in fishies:
        groups[fish] += 1
    for _ in range(num_sim):
        zeroes = groups.pop(0)
        groups.append(zeroes)
        groups[6] += zeroes
    return sum(groups)

print(f"Solution part 1: {run_sim(80, fishies)}, part 2: {run_sim(256, fishies)}")
