import numpy as np

def coord_sys_gen(beac_dist: list):
    directions = [0, 1, 2]
    # inefficient, calculating all possible 48
    for facing in directions:
        up = [el for el in directions if el != facing]
        up_axis = [((up[1], 1), (up[0], 1)), ((up[1], -1), (up[0], 1)), 
                  ((up[0], -1), (up[1], 1)), ((up[0], -1), (up[1], -1)),
                  ((up[0], 1), (up[1], 1)), ((up[1], -1), (up[0], -1)),
                  ((up[0], 1), (up[1], -1)), ((up[1], 1), (up[0], -1))]
        for fac_sign in (1, -1):
            for (x, xs), (z, zs) in up_axis:
                yield [xs*beac_dist[x],
                       fac_sign*beac_dist[facing],
                       zs*beac_dist[z]]

if __name__=='__main__':
    class LoopBreaker(Exception):
        pass

    beac_dists = open("input.txt").read().split('\n\n')
    scanners = []
    for beac_dist in beac_dists:
        x_list, y_list, z_list = np.array([], dtype=np.int16), np.array([], 
            dtype=np.int16), np.array([], dtype=np.int16)
        for dist in beac_dist.split('\n')[1:]:
            x, y, z = dist.split(',')
            x_list = np.append(x_list, int(x))
            y_list = np.append(y_list, int(y))
            z_list = np.append(z_list, int(z))
        scanners.append([x_list,y_list, z_list])
    scanners_ps = []
    abs_scanners = [curr_scanner:=scanners.pop(0)]
    beacons = set((x, y, z) for x, y, z in zip(curr_scanner[0], curr_scanner[1], curr_scanner[2]))
    while scanners:
        try:
            for scan_i, scanner in enumerate(scanners):
                # curr scanner represents one of the "found" scanners
                # scanner 0's coordinate system
                for curr_scanner in abs_scanners:
                    # c_systems represents all the possible coordinate system representations
                    # of the next coordinate system we are trying to match
                    c_systems = coord_sys_gen(scanner)
                    beacon_cords = list(zip(curr_scanner[0], curr_scanner[1], curr_scanner[2]))
                    for c_system in c_systems:
                        shared_beacons = 0
                        beacon_cords2 = list(zip(c_system[0], c_system[1], c_system[2]))
                        for x, y, z in beacon_cords:
                            for i, j, k in beacon_cords2:
                                diff = (x-i, y-j, z-k)
                                shared_beacons = 0
                                for i, (a, b, c) in enumerate(beacon_cords2):
                                    point_diff = (a+diff[0], b+diff[1], c+diff[2])
                                    c_system[0][i], c_system[1][i], c_system[2][i] = point_diff
                                    if point_diff in beacon_cords:
                                        shared_beacons +=1
                                if shared_beacons >= 12:
                                    beacons.update(list(zip(c_system[0], c_system[1], c_system[2])))
                                    abs_scanners.append(c_system)
                                    # scanners absolute position in scanner[0]'s system
                                    scanners_ps.append(diff)
                                    scanners.pop(scan_i)
                                    raise LoopBreaker
        except LoopBreaker:
            pass

    max_dist = 0
    for p1 in scanners_ps:
        for p2 in scanners_ps:
            mh = sum([abs(p1[0]-p2[0]), abs(p1[1]-p2[1]), abs(p1[2]-p2[2])])
            if mh > max_dist:
                max_dist = mh
    print(f"Part 1: {len(beacons)}, Part 2: {max_dist}")
        