from heapq import *
from copy import deepcopy

SLOTS = {(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)}
COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOMS = {'A':((3,2), (3,3)), 'B':((5,2), (5,3)), 'C':((7,2), (7,3)), 'D':((9,2), (9,3))}
ROOMS2 = {'A':((3,2), (3,3), (3,4), (3,5)), 'B':((5,2), (5,3), (5,4), (5, 5)), 
        'C':((7,2), (7,3), (7,4), (7,5)), 'D':((9,2), (9,3), (9,4), (9,5))}

def cost_function(a, b, cost_ap):
    cost = abs(b[0]-a[0])*cost_ap
    if cost:
        cost += (abs(1-a[1]) + abs(1-b[1]))*cost_ap
    else:
        cost = abs(1-a[1])*cost_ap
    return cost

def next_states(state, part1, rooms):
    new_states = []
    bottom = 3 if part1 else 5
    for x, y, curr_amphipod in state:
        if (x, y) in rooms[curr_amphipod] and \
            len([mark for i,j,mark in state if i==x and j>y and mark == curr_amphipod]) == bottom-y:
            continue
        if y != 1:
            possible_slots = set(SLOTS) | set(rooms[curr_amphipod])
        else:
            possible_slots = set(rooms[curr_amphipod])
        possible_slots -= {(x, y)}
        other_aps = set(state)-set((x, y, curr_amphipod))
        for ap in other_aps:
            if ap[1] == 1:
                # in hw cant have same x
                if ap[0] < x:
                    possible_slots -= {slot for slot in possible_slots if slot[0] <= ap[0]}
                elif ap[0] > x:
                    possible_slots -= {slot for slot in possible_slots if slot[0] >= ap[0]}
            else:
                #not in hw
                if ap[0] == x and ap[1] < y:
                    # locked in, no point moving anywhere
                    possible_slots = {}
                    break
                possible_slots -= {slot for slot in possible_slots if slot[1] >= ap[1] and slot[0] == ap[0]}

            if (ap[0], ap[1]) in rooms[curr_amphipod] and ap[2] != curr_amphipod:
                possible_slots -= set(rooms[curr_amphipod])
        if not possible_slots:
            continue
        correct_rooms = [slot for slot in possible_slots if slot in rooms[curr_amphipod]]
        new_state = [ap for ap in state if (ap[0], ap[1]) != (x, y)]
        if correct_rooms:
            slot = max(correct_rooms, key=lambda x: x[1])
            cost = cost_function((x, y), slot, COST[curr_amphipod]) 
            new_state.append((slot[0], slot[1], curr_amphipod))
            return [(tuple(new_state), cost)]
        for slot in possible_slots:
            cost = cost_function((x, y), slot, COST[curr_amphipod])
            new_state = [ap for ap in state if (ap[0], ap[1]) != (x, y)]
            new_state.append((slot[0], slot[1], curr_amphipod))
            new_states.append((tuple(new_state), cost))
    return new_states

def print_states(states):
    empty_map = ['#############',
                 '#...........#',
                 '###.#.#.#.###',
                 '  #.#.#.#.#  ',
                 '  #########  ']
    list_map = [list(row) for row in empty_map]
    lists = []
    print(' ----------------------------------')
    for s in states:
        new_list = deepcopy(list_map)
        for x, y, ap in s:
            new_list[y][x] = ap
        lists.append(new_list)
    for i in range(len(list_map)):
        print('| ', ''.join(lists[0][i]), '->', ''.join(lists[1][i]), ' |')

def occupied_rooms(state, part1):
    ap_range = range(1,4) if part1 else range(1,6)
    return tuple((i, j, state[j][i]) for j in list(ap_range)
                                     for i, slot in enumerate(state[j])
                                     if slot in ('A', 'B', 'C', 'D'))

def dijkstra(start_state, part1=False):
    open = [(0, occupied_rooms(start_state, part1))]
    track_state = {}
    costs = []
    rooms = ROOMS if part1 else ROOMS2
    while open:
        curr_state = heappop(open)
        successors = next_states(curr_state[1], part1, rooms)
        for successor, cost in successors:
            new_cost = curr_state[0] + cost
            if all([(ap[0], ap[1]) in rooms[ap[2]] for ap in successor]):
                costs.append(new_cost)
            try:
                if track_state[successor] <= new_cost:
                    continue
            except KeyError:
                pass
            track_state[successor] = new_cost
            heappush(open, (new_cost, successor))
        track_state[curr_state] = curr_state[0]
    return min(costs)

start_state1 = list(map(list, open("input.txt").read().splitlines()))
start_state2 = list(map(list, open("input2.txt").read().splitlines()))
p2 = dijkstra(start_state2, False)
p1 = dijkstra(start_state1, True)
print(f"Solution part 1: {p1}, part 2: {p2}")
#print(f"Solution part 1: {p1}, part 2: {1}")