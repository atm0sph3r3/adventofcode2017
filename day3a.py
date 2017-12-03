def get_square_size(square):
    return (2 * square - 1) + 4


with open('resources/day3', 'rt') as f:
    number = int(f.readline())
    found_square = False
    squares = list()
    square = 1
    previous = 1

    squares.append({'min': previous, 'max': previous, 'size': 1, 'square': square})
    while found_square is False:
        size = 8 * square
        max = previous + size
        squares.append({'min': previous + 1, 'max': max, 'size': size})
        previous = max

        if number <= max:
            found_square = True
        else:
            square = square + 1

    square_of_interest = squares[len(squares) - 1]

    n = square * 2
    y = n
    x = n
    numbers = [_ for _ in range(square_of_interest['min'], square_of_interest['max'] + 1)]

    for i in range(len(numbers) - 1, -1, -1):
        if numbers[i] == number:
            break

        if x == n and y == n:
            x = n
            y = y - 1
        elif x == n and y != 0:
            y = y - 1
            x = n
        elif x == n and y == 0:
            y = 0
            x = x - 1
        elif x == 0 and y == 0:
            x = 0
            y = y + 1
        elif x != n and y == 0:
            x = x - 1
            y = 0
        elif x == 0 and y != n:
            x = 0
            y = y + 1
        elif x == 0 and y == n:
            x = x + 1
            y = n
        elif x != n and y == n:
            x = x + 1
            y = y

    print (abs(x - square) + abs(y - square))
