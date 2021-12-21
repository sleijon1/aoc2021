from itertools import product
from collections import defaultdict

""" Could be optimized a lot but, in boring ways, leaving it clean and slow :) """

def adjacent(image, point):
    x, y = point
    adj_i = sorted(product((-1, 0, 1), (-1, 0, 1)), key=lambda x: (x[1], x[0]))
    # the padded border should be the same mark as adjacent if it
    return ''.join([image[(x+i, y+j)] if (x+i, y+j) in image.keys() else image[(x, y)] for i,j in adj_i])
            
            
def hashtag_convert(binary):
    # convert #, . to 1, 0
    rule = {'#': '1', '.': '0'}
    return ''.join([rule[char] for char in binary])

def enhance(image, algo, steps=50):
    for _ in range(steps):
        new_marks = {}
        for (x, y) in list(image.keys()):
            binary = adjacent(image, (x, y))
            algo_i = int(hashtag_convert(binary), 2)
            new_marks[(x, y)] = algo[algo_i]
        for (x, y), val in new_marks.items():
            image[(x, y)] = val
    return image

def num_lit(image_dict):
    return len([val for val in image_dict.values() if val=='#'])

if __name__ == '__main__':
    algo, image = open("input.txt").read().split('\n\n')
    image_dict = {}
    image = image.splitlines()
    padding = 70
    for y in range(-padding, len(image)-1+padding):
        for x in range(-padding, len(image[0])-1+padding):
            if y >= 0 and x >= 0 and x < len(image[0]) and y < len(image):
                image_dict[(x, y)] = image[y][x]
            else:
                image_dict[(x, y)] = '.'
    p1, p2 = num_lit(enhance(image_dict.copy(), algo, 2)), num_lit(enhance(image_dict.copy(), algo))
    print(f"Part 1: {p1}, part 2: {p2}")