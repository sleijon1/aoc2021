import os
from copy import deepcopy
instructions = open(os.getcwd() + "\input.txt").read().splitlines()

def adjacent_tiles(grid: list, coord: tuple) -> list:
    x, y = coord
    adjacent = []
    try:
        _ = grid[y+1][x]
        # below
        adjacent.append((x, y+1))
        _ = grid[y+1][x+1]
        # below right
        adjacent.append((x+1, y+1))
    except IndexError:
        pass
    try:
        _ = grid[y][x+1]
        # right
        adjacent.append((x+1, y))
    except IndexError:
        pass

    if y > 0:
        # above
        adjacent.append((x, y-1))
        if x < len(grid[0])-1:
            # above right
            adjacent.append((x+1, y-1))
        if x > 0:
            # above left
            adjacent.append((x-1, y-1))
    if x > 0:
        # left
        adjacent.append((x-1, y))
        if y < len(grid)-1:
            # below left
            adjacent.append((x-1, y+1))
    return adjacent


def run_sim(octo_map, sims, p2=False):
    flashes = 0
    tot_oct = len(octo_map)*len(octo_map[0])
    for step in range(sims):
        nines = []
        for i, row in enumerate(octo_map):
            for j, _ in enumerate(row):
                octo_map[i][j] += 1
                if octo_map[i][j] > 9:
                    nines.append((i, j))
        added = [el for el in nines]
        while nines:
            flashes += 1
            i, j = nines.pop(0)
            adj = adjacent_tiles(octo_map, (j, i))
            octo_map[i][j] = 0
            for j, i in adj:
                if octo_map[i][j] != 0:
                    octo_map[i][j] += 1
                    if octo_map[i][j] > 9 and (i, j) not in added:
                        nines.append((i, j))
                        added.append((i, j))
        if len(added) == tot_oct and p2:
            return step+1
    return flashes

octo_map = [[int(char) for char in row] for row in instructions]
print(f"Part 1: {run_sim(deepcopy(octo_map), 100)}, part 2: {run_sim(octo_map, 1000, True)}")


