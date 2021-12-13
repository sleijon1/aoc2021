import os

def split(paper, dir: str, coord: int):
    if dir=='y':
        return paper[:coord], paper[coord+1:]
    elif dir =='x':
        left = [[c for i, c in enumerate(row) if i < coord]
                 for row in paper]
        right = [[c for i, c in enumerate(row) if i > coord]
                  for row in paper]
        return left, right

def flip(dir: str, paper: list):
    if dir=='y':
        return paper[::-1]
    elif dir=='x':
        return [row[::-1] for row in paper]

def merge(dir: str, new_pap: list, flipped: list):
    if dir=='y':
        start_y = len(new_pap) - len(flipped)
        for y, row in enumerate(flipped):
                for x, mark in enumerate(row):
                    if mark == '#':
                        new_pap[start_y+y][x] = '#'
    elif dir=='x':
        start_x = len(new_pap[0]) - len(flipped[0])
        for y, row in enumerate(flipped):
                for x, mark in enumerate(row):
                    if mark == '#':
                        new_pap[y][start_x+x] = '#'
    return new_pap

def ppaper(*argv):
    for i, arg in enumerate(argv):
        print(f"Paper {i+1}")
        for p in arg:
            print(''.join(p))

def fold(paper: list, dir: str, coord: int):
    new_pap, to_flip = split(paper, dir, coord)
    flipped = flip(dir, to_flip)
    merge(dir, new_pap, flipped)
    return new_pap

if __name__ == '__main__':
    instructions = open(os.getcwd() + "\input.txt").read().splitlines()
    dots = []
    folds = []
    for row in instructions:
        if 'f' not in row and row != '':
            x, y = row.split(',')
            dots.append((int(x), int(y)))
        elif 'f' in row:
            folds.append((row.split(' ')[-1].split('=')))
    paper_x = max([x for x, _ in dots])
    paper_y = max([y for _, y in dots])
    paper = [['#' if (x, y) in dots else '.' for x in range(paper_x+1)] for y in range(paper_y+1)]
    for i, (dir, coord) in enumerate(folds):
        paper = fold(paper, dir, int(coord))
        if i == 0:
            count = sum([len([el for el in row if el == '#']) for row in paper])
            print(f"Part 1: {count}")
    print("Part 2:")
    ppaper(paper)