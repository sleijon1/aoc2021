instructions = open("C:/Users/simon/Documents/aoc2021/d3/input.txt").readlines()

flip = {'0': '1', '1': '0'}

def most_comm(bit_i, bits_list):
    occ = {'0': 0, '1': 0}
    for bits in bits_list:
        occ[bits[bit_i]] += 1
    ret_val = '0' if occ['0'] > occ['1'] else '1'
    return ret_val

def part_1 ():
    gamma_bin = []
    for i in range(len(instructions[0].strip())):
        gamma_bin.append(most_comm(i, instructions))
    gamma_bin = ''.join(gamma_bin) 
    eps_bin = ''.join([flip[i] for i in gamma_bin])
    return gamma_bin, eps_bin

def ratings(bit_list, i, oxy):
    if len(bit_list) == 1:
        return bit_list[0].strip()
    filter = most_comm(i, bit_list)
    if not oxy:
        filter = flip[filter]
    bit_list = [bits for bits in bit_list if bits[i] == filter]
    return ratings(bit_list, i+1, oxy)

gamma_bin, eps_bin = part_1()
print(f"Solution part 1: {int(gamma_bin, 2)*int(eps_bin, 2)}")
oxy, co2 = ratings(instructions, 0, True), ratings(instructions, 0, False)
print(f"Solution part 2: {int(oxy, 2)*int(co2, 2)}")