from copy import deepcopy
from itertools import product 

def quantum_memes(games, win_p1, win_p2):
    sums = [sum(x) for x in product([1, 2, 3], [1, 2, 3], [1, 2, 3])]
    # how many universes each roll appears in
    roll_count = {x:sums.count(x) for x in sums}
    first = True
    while games:
        p = games.pop()
        if p[0][0] >= 15:
            if p[0][2] == 1:
                win_p1[0] += p[0][3]
            else:
                win_p2[0] += p[0][3]
            continue
        elif not first:
            p[0][3] *= (3**3)
            p = p[::-1]
        for die_roll in range(3, 10):
            new_game = [[p[0][0], None, p[0][2], p[0][3], []], p[1]]
            new_game[0][3] *= roll_count[die_roll]
            new_game[0][4] = list(p[0][4])
            new_game[0][4].append(die_roll)
            new_pos = die_roll + p[0][1]
            new_game[0][1] = new_pos % 10 if new_pos % 10 != 0 else 10
            new_game[0][0] += new_game[0][1]
            games.append(new_game)
        first = False
    return 

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
    quantum_memes([[[0, p1_pos, 1, 1, []], [0, p2_pos, 2, 1, []]]], win_p1:=[0], win_p2:=[0])
    print(win_p1[0], win_p2[0])
    print(f"Part 2: {max(win_p1[0], win_p2[0])}")
    print(max(win_p1[0], win_p2[0]))