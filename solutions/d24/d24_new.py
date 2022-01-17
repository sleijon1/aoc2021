def gen_conditions(instructions):
    stack = []
    conditions = []
    for j, i in enumerate(range(0, len(instructions), 18)):
        set_op = instructions[i:i+18]
        if 'div z 26' in set_op:
            # have to satisfy condition w.r.t last added element
            # add condition
            pos, cond = stack.pop()
            new_cond = (j, pos, cond + int(set_op[5].split(' ')[-1]))
            conditions.append(new_cond)
        else:
            # stack item
            stack.append((j, int(set_op[-3].split(' ')[-1])))
    return conditions

def solve_conditions(conditions):
    smallest, largest = [], []
    for i, j, diff in conditions:
        val_1, val_2 = (9, 9 + diff) if diff < 0 else (9-diff, 9)
        val_3, val_4 = (abs(diff) + 1, 1) if diff < 0 else (1, diff+1)
        largest.append((j, val_1))
        largest.append((i, val_2))
        smallest.append((j, val_3))
        smallest.append((i, val_4))
    largest = sorted(largest, key=lambda x: x[0])
    smallest = sorted(smallest, key=lambda x: x[0])
    print('Solution p1: ', ''.join([str(x[1]) for x in largest]))
    print('Solution p2: ', ''.join([str(x[1]) for x in smallest]))

instructions = open("input.txt").read().splitlines()
solve_conditions(gen_conditions(instructions))

# biggest by hand: 92969593497992
# smallest by hand: 81514171491381