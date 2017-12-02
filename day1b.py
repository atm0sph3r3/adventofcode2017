with open('resources/day1', 'r') as f:
    line = f.readline()
    total = 0
    line_length = len(line)
    next_distance = int(line_length / 2)

    for i in range(line_length):
        to_check = (i + next_distance) % line_length
        if line[i] == line[to_check]:
            total = total + int(line[to_check])

    print(total)
