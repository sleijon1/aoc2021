import os
from collections import defaultdict, deque
instructions = open(os.getcwd() + "\input.txt").read().splitlines()
connections = defaultdict(lambda: [])
for row in instructions:
    fr, to = row.split('-')
    connections[fr].append(to)
    connections[to].append(fr)

def calc_paths(p1=True):
    queue = deque([['start', ['start']]])
    paths = []
    while queue:
        next_node = queue.pop()
        connected = connections[next_node[0]]
        possible = []
        for pos in connected:
            if pos.isupper():
                possible.append(pos)
                continue
            elif pos == 'start':
                continue
            else:
                if pos not in next_node[1] and p1:
                    possible.append(pos)
                elif not p1:
                    small_caves = [cave for cave in next_node[1] if cave.islower()]
                    small_caves.append(pos)
                    if len(small_caves) <= len(set(small_caves)) + 1:
                        possible.append(pos)

        for node in possible:
            new_path = next_node[1].copy()
            new_path.append(node)
            new_node = [node, new_path]
            if node == 'end':
                paths.append(new_path)
            else:
                queue.appendleft(new_node)
        if not possible and next_node[1][-1] == 'end':
            paths.append(next_node[1])

    return len(paths)

print(f"Part 1: {calc_paths()}, part 2: {calc_paths(False)}")
