def read_instructions(registers, instructions):
    current_instruction = 0

    while current_instruction < 8:
        action, register, value = instructions[current_instruction]
        value = get_value(registers, value)

        if action == 'set':
            registers[register] = value
        elif action == 'sub':
            registers[register] -= value
        elif action == 'mul':
            registers[register] *= value
        elif action == 'jnz':
            if get_value(registers, register) != 0:
                current_instruction += value
                continue

        current_instruction += 1

    h = 0
    for b in range(registers['b'], registers['c'] + 1, 17):
        f = 1
        h += any(b % x == 0 for x in range(2, b))
        '''
        for d in range(2, b + 1, 1):
            for e in range(2, b + 1, 1):
                # b must be a factor of d and e so it can't be prime
                g = d * e - b
                if g == 0:
                    f = 0
        if f == 0:
            h += 1
        '''
    return h


def get_value(registers, value):
    if value.startswith('-') or value.isdigit():
        new_value = int(value)
    else:
        new_value = registers[value]

    return new_value


registers = {'a': 1, 'b': 0, 'c': 0}
instructions = list()

with open("resources/day23", "r") as f:
    for line in f:
        split = line.split()
        instructions.append(split)

print(read_instructions(registers, instructions))






