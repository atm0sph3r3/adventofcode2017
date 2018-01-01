file = "resources/day21"
rules = dict()
input = '.#./..#/###'


def flip(input_list):
    return input_list[::-1]


def rotate(input_list):
    rotated = []
    for i in range(len(input_list)):
        row = []
        for j in range(len(input_list) - 1, -1, -1):
            row.append(input_list[j][i])
        rotated.append(row)

    return rotated


def convert_to_string(input_list):
    output = ''

    for each_list in input_list:
        output += ''.join(each_list)
        output += '/'

    return output[:-1]


def convert_to_array(input_string):
    split = input_string.split('/')
    return [[each for each in each_row] for each_row in split]


def get_value(block):
    for i in range(4):
        block = rotate(block)
        if convert_to_string(block) in rules:
            return rules[convert_to_string(block)]
        else:
            flipped = flip(block)
            if convert_to_string(flipped) in rules:
                return rules[convert_to_string(flipped)]

    return None


def divide_input(input_as_array):
    i_offset = 0

    if len(input_as_array) % 2 == 0:
        new_output = get_new_output(len(input_array), 2)
        for i in range(0, len(input_as_array), 2):
            j_offset = 0
            for j in range(0, len(input_as_array), 2):
                block = [[input_as_array[i][j], input_as_array[i][j + 1]],
                            [input_as_array[i+1][j], input_as_array[i+1][j+1]]]
                value = get_value(block)
                value_as_array = convert_to_array(value)

                for row in range(3):
                    for column in range(3):
                        new_output[i+row+i_offset][j+column+j_offset] = value_as_array[row][column]
                j_offset += 1
            i_offset += 1
        return new_output

    elif len(input_as_array) % 3 == 0:
        new_output = get_new_output(len(input_array), 3)
        for i in range(0, len(input_as_array), 3):
            j_offset = 0
            for j in range(0, len(input_as_array), 3):
                block = [[input_as_array[i][j], input_as_array[i][j + 1], input_as_array[i][j+2]],
                         [input_as_array[i+1][j], input_as_array[i+1][j+1], input_as_array[i+1][j+2]],
                         [input_as_array[i+2][j], input_as_array[i+2][j+1], input_as_array[i+2][j+2]]]
                value = get_value(block)
                value_as_array = convert_to_array(value)

                for row in range(4):
                    for column in range(4):
                        new_output[i+row+i_offset][j+column+j_offset] = value_as_array[row][column]
                j_offset += 1
            i_offset += 1

        return new_output


def get_new_output(length_input, divisible_by):
    new_size = int(length_input + (length_input / divisible_by))
    new_output = [[None for _ in range(new_size)] for _ in range(new_size)]
    return new_output


with open(file, "rt") as f:
    for line in f:
        split = line.split(' => ')
        rules[split[0]] = split[1].strip()

    input_array = convert_to_array(input)
    for i in range(5):
        input_array = divide_input(input_array)

    count = 0
    for row in range(len(input_array)):
        for column in range(len(input_array)):
            if input_array[row][column] == '#':
                count += 1

    print(count)

