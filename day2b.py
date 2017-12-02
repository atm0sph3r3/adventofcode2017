with open('resources/day2', 'rt') as f:
    total = 0

    for line in f:
        row = line.split()
        sorted_ints = sorted([int(item) for item in row])
        len_row = len(sorted_ints)

        for i in range(len_row):
            for j in range(i + 1, len_row):
                if sorted_ints[j] % sorted_ints[i] == 0:
                    total = total + (sorted_ints[j] / sorted_ints[i])
                    break

    print(total)
