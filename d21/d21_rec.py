from copy import deepcopy

def split_game(players, win_p1, win_p2):
    p = players
    while True:
        #print(p[1][0])
        #print(p)
        print(p[0][0])
        if p[0][0] >= 1:
            #print(win_p1[0])
            if p[0][2] == 1:
                win_p1[0] += 1
            else:
                win_p2[0] += 1
            break
        for die_roll in range(1, 4):
            new_pos = p[0][1] + die_roll
            wrapped_pos = new_pos % 10 if new_pos % 10 != 0 else 10
            new_score = wrapped_pos + p[0][0]
            player = p[0][2]
            # reverse player list so next player plays next recursion
            new_game = (p[1], ((new_score, wrapped_pos, player)))
            split_game(new_game, win_p1, win_p2)

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
    split_game(((0, p1_pos, 1), (0, p2_pos, 2)), win_p1:=[0], win_p2:=[0])
    print(f"Part 2: {max(win_p1[0], win_p2[0])}")