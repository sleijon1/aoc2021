def shift_positive(beac_dist: list):
    x, y = beac_dist
    min_x, min_y = min(x), min(y)
    if min_x < 0:
        beac_dist[0] = [val+abs(min_x) for val in x]
    if min_y < 0:
        beac_dist[1] = [val+abs(min_y) for val in y]
    #if min_z < 0:
    #    beac_dist[0] = [val+abs(min_z) for val in z]

def coord_sys_gen(beac_dist: list):
    
    yield None

if __name__=='__main__':
    beac_dists = open("input.txt").read().split('\n\n')
    scanners = []
    for beac_dist in beac_dists:
        x_list, y_list, z_list = [], [], []
        scanners.append([x,y])
        for dist in beac_dist.split('\n')[1:]:
            x, y = dist.split(',')
            x_list.append(int(x))
            y_list.append(int(y))

    curr_scanner = shift_positive(scanners[0])
    beacons = set()
    scanners_add = 0
    while True:
        if scanners_add == len(scanners):
            break
        for scanner in scanners:
            c_systems = coord_sys_gen(scanner)
            beacon_cords = [(x, y) for x, y in zip(curr_scanner[0], curr_scanner[1])]
            shared_beacons = 0
            for c_system in c_systems:
                shift_positive(c_system)
                beacon_cords2 = [(x, y) for x, y in zip(c_system[0], c_system[1])]
                for cord in beacon_cords2:
                    if cord in beacon_cords:
                        shared_beacons += 1
                if shared_beacons >= 12:
                    beacons.add(cord)
                    curr_scanner = c_system
                    scanners_add += 1
                    break
    print(f"Part 1: {len(beacons)}")
        