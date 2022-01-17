def product(list):
    prod = 1
    for el in list:
        prod *= el
    return prod

operations = {0: sum, 1: product, 2: min, 3: max,
              5: lambda x: int(x[0] > x[1]), 6: lambda x: int(x[0] < x[1]),
              7: lambda x: int(x[0] == x[1])}

def parse_hierarchy(bin, i=0, vers_sum=[]): 
    vers = int(bin[i:i+3], 2)
    type_id = int(bin[i+3:i+6], 2)
    vers_sum[0] += vers
    i += 6
    if type_id == 4:
        literal = bin[i+1:i+5]
        while True:
            if bin[i] == '0':
                i += 5
                break
            else:
                i += 5
                literal += bin[i+1:i+5]
        return int(literal, 2), i
    else:
        l_type_id = bin[i]
        op = operations[type_id]
        i += 1
        sub_packs, end_i = None, None
        if l_type_id == '1':
            length = 11
            sub_packs = int(bin[i:i+length], 2)
        else:
            length = 15
            sub_pack_length = int(bin[i:i+length], 2)
            end_i = i + sub_pack_length + length
        i += length
        vals = []
        while True:
            if (l_type_id == '0' and i >= end_i):
                break
            elif l_type_id == '1':
                if sub_packs == 0:
                    break
                else:
                    sub_packs -= 1
            val, i = parse_hierarchy(bin, i, vers_sum)
            vals.append(val)
        return op(vals), i

if __name__== '__main__':
    hex = open("input.txt").read().splitlines()[0]
    bin = ''.join([bin(int(hex_char, 16))[2:].zfill(4) for hex_char in hex])
    vers_sum = [0]
    val, _ = parse_hierarchy(bin, vers_sum=vers_sum)
    print(f"Part 1: {vers_sum[0]}, Part 2: {val}")
    