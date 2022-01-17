from collections import defaultdict
instructions = open("input.txt").read().splitlines()
east, south = [], []
occupied = defaultdict(int)
for y, row in enumerate(instructions):
    for x, col in enumerate(row):
        if col in ('>', 'v'):
            occupied[(x, y)] = 1
        if col == '>':
            east.append((x, y))
        elif col == 'v':
            south.append((x, y))
moving = True
steps = 0
while moving:
    steps += 1
    moving = False
    conc = east + south
    new_east, new_south = [], []
    pairs = []
    for (ex, ey) in east:
        new_x = ex+1 if ex+1 < len(row) else 0
        if not occupied[(new_x, ey)]:
            moving = True
            new_east.append((new_x, ey))
            pairs.append([(new_x, ey), (ex, ey)])
        else:
            new_east.append((ex, ey))
    for (new_x, ey), (ex, ey) in pairs:
        occupied[(new_x, ey)] = 1
        occupied[(ex, ey)] = 0
    
    for (ex, ey) in south:
        new_y = ey+1 if ey+1 < len(instructions) else 0
        if not occupied[(ex, new_y)]:
            moving = True
            new_south.append((ex, new_y))
            pairs.append([(ex, new_y), (ex, ey)])
        else:
            new_south.append((ex, ey))

    for (ex, new_y), (ex, ey) in pairs:
        occupied[(ex, new_y)] = 1
        occupied[(ex, ey)] = 0
    if not moving:
        print(f"Solution part 1: {steps}")
        break
    east, south = new_east, new_south