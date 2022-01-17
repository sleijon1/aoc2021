import os
from colorama import Cursor, Fore, Back, Style

def fold(dots, dir, coord):
    new_dots = dots.copy()
    for dot in dots:
        if dir=='y':
            if dot[1] > coord:
                new_dots.add((dot[0], coord - (dot[1] - coord)))
                new_dots.remove((dot[0], dot[1]))
        elif dir=='x':
            if dot[0] > coord:
                new_dots.add((coord - (dot[0] - coord), dot[1]))
                new_dots.remove((dot[0], dot[1]))
    return new_dots

if __name__ == '__main__':
    instructions = open(os.getcwd() + "\input.txt").read().splitlines()
    dots, folds = set(), []
    for row in instructions:
        if 'f' not in row and row != '':
            x, y = row.split(',')
            dots.add((int(x), int(y)))
        elif 'f' in row:
            folds.append((row.split(' ')[-1].split('=')))

    for i, (dir, coord) in enumerate(folds):
        dots = fold(dots, dir, int(coord))
        if i==0:
            print(f"Part 1: {len(dots)}")
    print("Part 2:")
    paper_x = max([x for x, _ in dots])
    paper_y = max([y for _, y in dots])
    paper = [['#' if (x, y) in dots else '.' for x in range(paper_x+1)] for y in range(paper_y+1)]
    for y in range(paper_y+1):
        for x in range(paper_x+1):
            if (x, y) in dots:
                print(Fore.GREEN + Back.BLACK + chr(1) + f"{Cursor.POS(x + 2, y + 2)}#")
            else:
                print(Back.BLACK + f"{Cursor.POS(x + 2, y + 2)} ")
    print(Style.RESET_ALL)