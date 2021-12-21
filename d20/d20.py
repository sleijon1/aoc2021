from itertools import product

""" Could be optimized a lot but, in boring ways, leaving it clean and slow :) - ok, i optimized. """

def adjacent(image, point):
    x, y = point
    # write em out to not have to use a sort method 
    adj_i = [(-1, -1), (0, -1), (1, -1), (-1, 0), 
            (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    adj_string = ''
    for i, j in adj_i:
        try: 
            adj_string += image[(x+i, y+j)]
        except KeyError:
            # the padded border should be the same mark as adjacent if it
            adj_string += image[(x, y)]
    return adj_string
            
def enhance(image, algo, steps=50):
    for _ in range(steps):
        new_marks = {}
        for (x, y) in list(image.keys()):
            binary = adjacent(image, (x, y))
            algo_i = int(binary, 2)
            new_marks[(x, y)] = algo[algo_i]
        for (x, y), val in new_marks.items():
            image[(x, y)] = val
    return image

def num_lit(image_dict):
    return len([val for val in image_dict.values() if val=='1'])

if __name__ == '__main__':
    algo, image = open("input.txt").read().split('\n\n')
    # convert now to not need to convert every time later
    algo = algo.replace('.', '0').replace('#', '1')
    image_dict = {}
    image = image.splitlines()
    padding = 65
    rule = {'#': '1', '.': '0'}
    for y in range(-padding, len(image)-1+padding):
        for x in range(-padding, len(image[0])-1+padding):
            if y >= 0 and x >= 0 and x < len(image[0]) and y < len(image):
                image_dict[(x, y)] = rule[image[y][x]]
            else:
                image_dict[(x, y)] = '0'
    p1, p2 = num_lit(enhance(image_dict.copy(), algo, 2)), num_lit(enhance(image_dict.copy(), algo))
    print(f"Part 1: {p1}, part 2: {p2}")