from math import ceil


def reduce(expr):
    depth = 0
    red_more, search_exp = False, True
    for _ in range(2):
        for i, val in enumerate(expr):
            if val == ',':
                continue
            elif val == '[':
                depth += 1
            elif val == ']':
                depth -= 1
            else:
                if depth == 5 and search_exp:
                    right_add = expr[i+2]
                    for k in range(i-2, 0, -1):
                        if type(expr[k]) == int:
                            expr[k] += val
                            break
                    for j in range(i+4, len(expr)):
                        if type(expr[j]) == int:
                            expr[j] += right_add
                            
                            break
                    new_expr = expr[:i-1] + [0] + expr[i+4:]
                    expr = new_expr
                    red_more = True
                    break
                elif val >= 10 and not search_exp:
                    split = ['[', val//2, ',', ceil(val/2), ']']
                    new_expr = expr[:i] + split + expr[i+1:]
                    expr = new_expr
                    red_more = True
                    break
        if red_more:
            break
        else:
            search_exp = False
    if red_more:
        return reduce(expr)
    else:
        return expr

def create_num(plain):
    first_num = []
    for char in plain:
        try:
            char = int(char)
        except ValueError:
            pass
        first_num.append(char)
    return first_num

def create_list(string):
    expr = []
    for char in string:
        if char == '[':
            expr.append([])
        if char == ']':
            if len(expr) == 1:
                return expr.pop()
            expr[-2].append(expr.pop())
        elif type(char) == int:
            expr[-1].append(char)

def magnitude(list_expr):
    left_expr, right_expr = list_expr
    if type(left_expr) == int and type(right_expr) == int:
        return left_expr*3 + right_expr*2
    elif type(left_expr) == int and type(right_expr) != int:
        return left_expr*3 + magnitude(right_expr)*2
    elif type(left_expr) != int and type(right_expr) == int:
        return magnitude(left_expr)*3 + right_expr*2
    else:
        return magnitude(left_expr)*3 + magnitude(right_expr)*2

def calc_p2(nums):
    max_sum = 0
    for i, num in enumerate(nums):
        for j, other_num in enumerate(nums):
            if i != j:
                conc = ['['] + num + [','] + other_num + [']']
                res_list = create_list(reduce(conc))
                two_sum = magnitude(res_list)
                if two_sum > max_sum:
                    max_sum = two_sum
    return max_sum

if __name__== '__main__':
    instr = open("input.txt").read().splitlines()
    curr_num = create_num(instr[0])
    nums = [curr_num]
    for plain in instr[1:]:
        add_num = create_num(plain)
        nums.append(add_num)
        conc = ['['] + curr_num + [','] + add_num + [']']
        curr_num = reduce(conc)
    list_expr = create_list(curr_num)
    print(f"Part 1: {magnitude(list_expr)}, Part 2: {calc_p2(nums)}")
