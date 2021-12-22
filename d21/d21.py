from copy import deepcopy

def quantum_memes(games, win_p1, win_p2):
    splits = 0
    while games:
        p = games.pop()
        while True:
            for i in range(len(p)):
                if p[i][0] >= 21:
                    if p[i][2] == 1:
                        win_p1[0] += 1
                    else:
                        win_p2[0] += 1
                    break
                for die_roll in range(1, 4):
                    copy = deepcopy(p)
                    copy[i][1] += die_roll
                    copy[i][1] = copy[i][1] % 10 if copy[i][1] % 10 != 0 else 10
                    copy[i][0] += copy[i][1]
                    splits += 1
                    games.append(copy)
            if break_outer:
                break
    return splits

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
    splits = quantum_memes([[[0, p1_pos, 1], [0, p2_pos, 2]]], win_p1:=[0], win_p2:=[0])
    print(win_p1[0], win_p2[0])
    print(f"Part 2: {max(win_p1[0], win_p2[0])}")
    print(splits*max(win_p1[0], win_p2[0]))