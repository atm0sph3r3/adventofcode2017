with open('resources/day1', 'r') as f:
    line = f.readline()
    last = len(line) - 1
    sum = 0
    next = 0

    for i in range(len(line)):
        if i == last:
            next = int(line[0])
        else:
            next = int(line[i+1])

        if int(line[i]) == next:
            sum = sum + next

    print(sum)
