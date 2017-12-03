with open("resources/day5", "rt") as f:
    instructions = []
    for line in f:
        instructions.append(int(line))

    found_exit = False
    current_index = 0
    count = 0
    while not found_exit:
        count = count + 1
        value = instructions[current_index]
        instructions[current_index] = value + 1
        current_index = current_index + value

        if current_index >= len(instructions) or current_index < 0:
            break

    print(count)
