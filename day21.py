import copy

file = "resources/day21"
rules = dict()
input = '.#./..#/###'


def reverse(input_list):
    begin = 0
    end = len(input_list) - 1

    while end > begin:
        temp = input_list[end]
        input_list[end] = input_list[begin]
        input_list[begin] = temp

        begin += 1
        end -= 1


def rotate(input_list):
    copy_list = copy.deepcopy(input_list)
    size = len(copy_list)
    max_x = size - 1
    max_y = size - 1
    min_x = 0
    min_y = 0

    while min_x < max_x and min_y < max_y:
        for i in range(min_y, max_y + 1):
            copy_list[i][max_y] = input_list[min_x][i]

        offset = max_y
        for i in range(min_x, max_x + 1):
            copy_list[max_x][offset - i] = input_list[i][max_y]

        for i in range(max_y, min_y - 1, -1):
            copy_list[min_y][i] = input_list[max_x][i]

        min_x += 1
        max_x -= 1
        min_y += 1
        max_y -= 1

    return copy_list


def convert_to_string(input_list):
    output = ''
    for each_list in input_list:
        output += '/'.join(each_list)

    return output[:-1]


def convert_to_array(input_string):
    split = input_string.split('/')
    return [[each for each in each_row] for each_row in split]


with open(file, "rt") as f:
    for line in f:
        split = line.split(' => ')
        rules[split[0]] = split[1].strip()

    for k, v in rules.items():
        as_array = convert_to_array(k)
        rotated = rotate(as_array)
        print(rotated)

