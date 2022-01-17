instructions = open("C:/Users/simon/Documents/aoc2021/d1/input.txt").readlines()
instructions = map(int, instructions)
previous_depth = None
inc_count = 0
for depth in instructions:
    if previous_depth is not None and \
        depth > previous_depth:
        inc_count += 1
    previous_depth = depth
print(f"Solution part 1 {inc_count}")