def get_intersection(re1, re2):
    find_ol = lambda x, y: (max(x[0], y[0]), min(x[1], y[1]))
    overlap = [find_ol(re1[i], re2[i]) for i in range(1, 4)]
    # check overlap with min max on boundaries instead of checking both ways
    no_overlap = overlap[0][0] > overlap[0][1] or overlap[1][0] > overlap[1][1] \
        or overlap[2][0] > overlap[2][1]
    if no_overlap:
        return []
    # reverse the sign of re2 according to inclusion-exclusion principle
    return [-re2[0]] + overlap

def create_cube_sets(cuboids):
    sets = []
    # creates sets according to: https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
    for cuboid in cuboids:
        new_sets = []
        for set in sets:
            if new_intersect := get_intersection(cuboid, set):
                new_sets.append(new_intersect)
        sets += new_sets
        if cuboid[0] == 1:
            sets.append(cuboid)
    return sets

def cubes_on(sets):
    cubes = 0
    for set in sets:
        x_len, y_len, z_len = set[1][1]-set[1][0], set[2][1]-set[2][0], \
            set[3][1]-set[3][0]
        cubes += set[0]*x_len*y_len*z_len
    return cubes

if __name__ == '__main__':
    instr = open("input.txt").read().splitlines()
    cuboids = []
    of = {'on': 1, 'off': -1}
    for line in instr:
        on_off, cuboid = line.split(' ')
        cuboid = [(int(el.split('..')[0][2:]), int(el.split('..')[1])+1)
                    for el in cuboid.split(',')] 
        cuboids.append([of[on_off]] + cuboid)
    cubes = cubes_on(create_cube_sets(cuboids))
    # part 1 - manually remove non-initialization part
    print(f"Solution: {cubes}")