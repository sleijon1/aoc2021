from itertools import product

def part_1(cuboids):
    cubes_on = set()
    for on_off, (x, y, z) in cuboids:
        #print(list(product(x, y, z)))
        #exit()
        for cube in product(x, y, z):
            if on_off == 'on':
                cubes_on.add(cube)
            else:
                try:
                    cubes_on.remove(cube)
                except KeyError:
                    # cube not on
                    pass
    return cubes_on

if __name__ == '__main__':
    instr = open("input.txt").read().splitlines()
    cuboids = []
    for line in instr:
        on_off, cuboid = line.split(' ')
        cuboid = [range(int(el.split('..')[0][2:]), int(el.split('..')[1])+1) 
                    for el in cuboid.split(',')] 
        cuboids.append((on_off, cuboid))
    cubes_on = part_1(cuboids)
    #print(cubes_on)
    region_on = [(x, y, z) for (x, y, z) in cubes_on 
                if (-50 <= x <= 50) and (-50 <= y <= 50) and (-50 <= z <= 50)]
    print(f"Part 1: {len(region_on)}")