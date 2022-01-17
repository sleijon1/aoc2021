import os
from math import inf
from collections import defaultdict
import time

def dijkstra(graph, start=(0, 0)):
    distance, cost, adj, paths = {}, {}, defaultdict(lambda: []), {}
    visited = defaultdict(lambda: False)
    for y, row in enumerate(graph):
        for x, val in enumerate(row):
            distance[(x, y)] = inf
            cost[(x, y)] = val
            for ad_x, ad_y in [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]:
                if ad_x < len(row) and ad_x >= 0 and \
                   ad_y < len(graph) and ad_y >= 0:
                   adj[(x, y)].append((ad_x, ad_y))
    visited[start] = True
    distance[start], cost[start] = 0, 0
    curr = start
    queue = []
    while True:
        for adjac in [x for x in adj[curr] if not visited[x] and x not in queue]:
            if distance[adjac] > cost[adjac] + distance[curr]:
                distance[adjac] = cost[adjac] + distance[curr]
                paths[adjac] = curr
                queue.append(adjac)
        queue = sorted(queue, key=lambda x: distance[x])
        curr = queue.pop(0)
        visited[curr] = True
        if not queue:
            break
    return paths, distance

def part_2_graph(graph):
    len_x, len_y = len(graph), len(graph[0])
    new_graph = []
    for y in range(len_y*5):
        new_graph.append(row := [])
        for x in range(len_x*5):
            og_x, og_y = x % len_x, y % len_y
            new_val = graph[og_y][og_x] + x//len_x + y//len_y
            if new_val > 9:
                new_val %= 9
            row.append(new_val)
    return new_graph

def calc_risk(graph):
    # ended up not needing paths for puzzle but keeping it anyway :D
    paths, cost = dijkstra(graph)
    total_cost = cost[(len(graph[0])-1, len(graph)-1)]
    return total_cost

if __name__== '__main__':
    instructions = open(os.getcwd() + "\input.txt").read().splitlines()
    graph = [list(map(int, row)) for row in instructions]
    p2_graph = part_2_graph(graph)
    tic = time.perf_counter()
    print(f"Part 1: {calc_risk(graph)}, part 2: {calc_risk(p2_graph)}")
    toc = time.perf_counter()
    print(f"Ran solutions in {toc - tic:0.4f} seconds")
    