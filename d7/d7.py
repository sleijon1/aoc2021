import os
instructions = open(os.getcwd() + "\input.txt").read()
positions = [int(pos) for pos in instructions.split(',')]

def min_fuel(part_1=True):
    fuels = []
    for start_pos in range(min(positions), max(positions)):
        fuel = 0
        for pos in positions:
            fuel += abs(start_pos-pos) if part_1 \
                else sum(range(abs(start_pos-pos)+1))
        fuels.append(fuel)
    return min(fuels)

print(f"Solution part 1: {min_fuel(True)}, part 2: {min_fuel(False)}")