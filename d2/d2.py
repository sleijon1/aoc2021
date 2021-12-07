instructions = open("C:/Users/simon/Documents/aoc2021/d2/input.txt").readlines()

def get_state(part_2=False):
    state = {'aim': 0, 'pos': 0, 'depth': 0}
    for instr in instructions:
        dir, val = instr.split(' ')
        val = int(val)
        if dir == 'up':
            state['aim'] -= val
        elif dir == 'forward':
            state['pos'] += val
            state['depth'] += val*state['aim']
        elif dir == 'down':
            state['aim'] += val
    ret_val = state['aim']*state['pos'] if not part_2 else state['depth']*state['pos']
    return ret_val

print(f"Solution part 1: {get_state()}, part 2: {get_state(True)}")