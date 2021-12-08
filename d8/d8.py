import os
instructions = open(os.getcwd() + "\input.txt").readlines()

code_to_dig = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9,
}

def get_num(m, str):
    result = ""
    for char in str:
        result += m[char]
    result = "".join(sorted(result))
    return code_to_dig[result]

def deduce(m, segs, code, chars):
    for char in code:
        for seg in segs:
            if char not in seg:
               m[char] = chars[0]
               other_char = code.replace(char, '')
               m[other_char] = chars[1]
               return
p1 = 0
outputs = []
for row in instructions:
    m = {}
    inp, out = row.split('|')
    inp = [digit.strip() for digit in inp.strip().split(' ')]
    inp = sorted(inp, key= lambda x: len(x))
    six_segs = [code for code in inp if len(code) == 6]
    five_segs = [code for code in inp if len(code) == 5]

    deduce(m, six_segs, inp[0], ['c', 'f'])

    a_seg = [char for char in inp[1] if char not in m.keys()]
    m[a_seg[0]] = 'a'

    four = ''.join([char for char in inp[2] if char not in m.keys()])
    deduce(m, five_segs, four, ['b', 'd'])

    eight = ''.join([char for char in inp[-1] if char not in m.keys()])
    deduce(m, six_segs, eight, ['e', 'g'])

    output = ""
    for digit in out.strip().split(' '):
        if len(digit.strip()) in (2, 4, 3, 7):
            p1 += 1
        output += str(get_num(m, digit))
    outputs.append(int(output))

print(f"Part 1: {p1}, part 2: {sum(outputs)}")