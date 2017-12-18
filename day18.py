registers = dict()
instructions = list()

with open("resources/day18", "rt") as f:
    for line in f:
        split = line.split()
        instructions.append(split)
        registers[split[1]] = 0

    current_instruction = 0
    recovered_frequency = 0
    done = False
    while not done:
        action = instructions[current_instruction][0]
        register = instructions[current_instruction][1]
        value = 0
        if len(instructions[current_instruction]) == 3:
            value = instructions[current_instruction][2]
            if str(value).startswith('-') or value.isdigit():
                value = int(value)
            else:
                value = registers[value]

        if action == 'snd':
            recovered_frequency = registers[register]
        elif action == 'set':
            registers[register] = value
        elif action == 'add':
            registers[register] += value
        elif action == 'mul':
            registers[register] *= value
        elif action == 'mod':
            registers[register] %= value
        elif action == 'rcv':
            if registers[register] != 0:
                done = True
        elif action == 'jgz':
            if registers[register] > 0:
                current_instruction += value
            else:
                current_instruction += 1
        else:
            raise RuntimeError('Invalid instruction')

        if not done and action != 'jgz':
            current_instruction += 1

    print(recovered_frequency)

