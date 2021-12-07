import os
instructions = open(os.getcwd() + "\input.txt").readlines()
input_boards = instructions[2:]
input_boards.append('\n')
numbers = map(int, instructions[0].strip().split(','))
boards = []
new_board = []

for row in input_boards:
    if row == '\n':
        boards.append(new_board)
        new_board = []
        continue
    num_row = [[int(num), False] 
                for num in row.split() if num != '']
    new_board.append(num_row)

def calc_score(win_num, board):
    sum_um = 0
    for row in board:
        for col in row:
            if not col[1]:
                sum_um += col[0]
    return (sum_um*win_num, board)


def end():
    print(f"Part 1: {win_scores[0][0]}")
    print(f"Part 2: {win_scores[-1][0]}")
    exit()

win_scores = []
for num in numbers:
    for board in boards:
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col[0] == num:
                    col[1] = True
                    full_row = sum([mark[1] for mark in row]) == 5
                    full_col = sum([row[j][1] for row in board]) == 5
                    if full_col or full_row:
                        win_boards = [t[1] for t in win_scores]
                        if board not in win_boards:
                            win_scores.append(calc_score(num, board))
                        if len(win_scores) == len(boards):
                            end()