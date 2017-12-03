def get_square_size(square):
    return (2 * square - 1) + 4


with open('resources/day3', 'rt') as f:
    number = int(f.readline())
    square = 1
    sum = 0

    while sum <= number:
        sum = sum + get_square_size(square)
        square = square + 1

    grid = [[0 for __ in range(square + 1)] for _ in range(square + 1)]

    grid[int(square / 2)][int(square / 2)] = 1

    start_row = square / 2
    start_column = square / 2 + 1

    current_square = 1
    value = 2
    while True:
        square_size = get_square_size(current_square)
        for i in range(start_row, -1):
            grid[i][start_column] = value
        start_column = start_column - 1
