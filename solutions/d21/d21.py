from collections import deque
from itertools import product 


def quantum_memes(p1_pos, p2_pos):
    sums = [sum(x) for x in product([1, 2, 3], [1, 2, 3], [1, 2, 3])]
    # how many universes each roll appears in
    roll_count = {x:sums.count(x) for x in sums}
    wins = [0, 0]
    games = deque([[[], [0, 0], [p1_pos, p2_pos]]])
    # [0, 0, 4, 8, universes]
    last_player = {1:0,0:1}
    while games:
        game = games.pop()
        for die_roll in range(3, 10):
            copy = [list(game[0]), list(game[1]), list(game[2])]
            if len(copy[0]) % 2 == 0:
                player = 0
            else:
                player = 1
            if copy[1][last_player[player]] >= 21:
                universe_wins = 1
                for pos in copy[0]:
                    universe_wins *= roll_count[pos]
                wins[last_player[player]] += universe_wins
                break
            # calculate where player ends up at
            new_pos = copy[2][player] + die_roll
            wrapped_pos = new_pos % 10 if new_pos % 10 != 0 else 10
            # update score
            copy[1][player] = wrapped_pos + copy[1][player]
            # update position
            copy[2][player] = wrapped_pos
            # add die roll for win calculation
            copy[0].append(die_roll)
            games.appendleft(copy)
    return wins

if __name__ == '__main__':
    instr = open("input.txt").read().splitlines()
    p1_pos, p2_pos = int(instr[0].split(': ')[-1]), int(instr[1].split(': ')[-1])
    die, die_i = 100, 1
    opp = {0: 1, 1:0}
    break_outer = False
    p = [[p1:=0, p1_pos], [p2:=0, p2_pos]]
    while True:
        for i in range(len(p)):
            for _ in range(3):
                p[i][1] += die_i%die if die_i%die != 0 else die
                die_i += 1
            p[i][1] = p[i][1] % 10 if p[i][1] % 10 != 0 else 10
            p[i][0] += p[i][1]
            if p[i][0] >= 1000:
                print(f"Part 1: {p[opp[i]][0]*(die_i-1)}")
                break_outer = True
                break
        if break_outer:
            break
    print(f"Part 2: {max(quantum_memes(p1_pos, p2_pos))}")