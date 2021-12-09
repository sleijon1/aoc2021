import os
instructions = open(os.getcwd() + "\input.txt").read().splitlines()

def get_adjacent(instructions, i, j):
    adjacent = []
    if j > 0:
        adjacent.append([(i,j-1), int(instructions[i][j-1])])
    if j < len(row)-1:
        adjacent.append([(i, j+1), int(instructions[i][j+1])])
    if i > 0:
        adjacent.append([(i-1,j), int(instructions[i-1][j])])
    if i < len(instructions)-1:
        adjacent.append([(i+1,j), int(instructions[i+1][j])])
    return adjacent

low_points, basin_sizes = [], []
for i, row in enumerate(instructions):
    for j, point in enumerate(row):
        adjacent = get_adjacent(instructions, i, j)
        if sum([int(point) < adj[1] for adj in adjacent]) == len(adjacent):
            queue = [adj[0] for adj in adjacent if adj[1] != 9]
            basin_size = 1
            visited = [(i,j)]
            while queue:
                new_i, new_j = queue.pop()
                new_adjacents = get_adjacent(instructions, new_i, new_j)
                for new_adj in new_adjacents:
                    if new_adj[1] != 9 and new_adj[0] not in visited \
                                        and new_adj[0] not in queue:
                        queue.append(new_adj[0])
                basin_size += 1
                visited.append((new_i, new_j))
            low_points.append(int(point))
            basin_sizes.append(basin_size)


p1 = sum(low_points) + len(low_points)
top3 = sorted(basin_sizes, reverse=True)[:3]
print(f"part 1: {p1}, part 2: {top3[0]*top3[1]*top3[2]}")