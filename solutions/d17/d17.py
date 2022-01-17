if __name__== '__main__':
    instr = open("input.txt").read()
    # processing instructions
    x, y = instr.split(': ')[1].split(', ')  
    x = [int(b) for b in x.split('=')[1].split('..')]
    y = [int(b) for b in y.split('=')[1].split('..')]
    min_area = (min(x), min(y))
    max_area = (max(x)+1, max(y)+1)
    x_range = range(min_area[0], max_area[0])
    y_range = range(min_area[1], max_area[1])
    # hash for constant O(1) lookup
    area = {(x, y): True for x in x_range for y in y_range}
    # x lim obvious, y upper lim not sure whats best
    vels = [(x, y) for x in range(max_area[0]) for y in range(min_area[1], abs(min_area[1]))]
    hits = set()
    for x, y in vels:
        x_coord, y_coord = 0, 0
        i = 0
        x_incr, y_incr = x, y
        y_max = 0
        while True:
            # step sim
            y_coord += y_incr
            y_incr -= 1
            if y_coord > y_max:
                y_max = y_coord
            x_coord += x_incr
            if x_incr > 0:
                x_incr -= 1
            elif x_incr < 0:
                x_incr += 1
            # unreachable if hitting any of these
            if y_coord < min_area[1] and y_incr <= 0:
                break
            elif x_coord < min_area[0] and x_incr == 0:
                break
            elif x_coord > max_area[0]:
                break
            # add velocity and max y if in area
            try:
                if area[(x_coord, y_coord)]:
                    hits.add((x, y, y_max))
                    break
            except KeyError:
                # coords not in area
                pass
            i += 1
    sort_hits = sorted(hits, key=lambda x: x[2])
    print(f'Part 1: {sort_hits[-1]}, part 2: {len(sort_hits)}')