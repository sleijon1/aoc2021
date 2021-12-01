instructions = open("C:/Users/simon/Documents/aoc2021/d1/input.txt").readlines()
instructions = list(map(int, instructions))
previous_sum = None
inc_count = 0
for i in range(0, len(instructions)-2):
    depth = sum(instructions[i:i+3])
    if previous_sum is not None and \
        depth > previous_sum:
        inc_count += 1
    previous_sum = depth

print(f"Solution part 2 {inc_count}")