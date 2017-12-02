with open('resources/day2', 'rt') as f:
    total = 0
    for line in f:
        row = line.split()
        row_as_ints = [int(item) for item in row]

        sorted_line = sorted(row_as_ints)
        total = total + (sorted_line[len(sorted_line) - 1] - sorted_line[0])

    print(total)
