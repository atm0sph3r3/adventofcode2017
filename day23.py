def read_instructions(registers, instructions):
    current_instruction = 0
    mul_count = 0

    while current_instruction < len(instructions):
        print(current_instruction)
        action = instructions[current_instruction][0]
        register = instructions[current_instruction][1]

        if len(instructions[current_instruction]) == 3:
            value = instructions[current_instruction][2]
        else:
            value = instructions[current_instruction][1]

        value = get_value(registers, value)

        if action == 'set':
            registers[register] = value
        elif action == 'sub':
            registers[register] -= value
        elif action == 'mul':
            registers[register] *= value
            mul_count += 1
        elif action == 'jnz':
            if (register.isdigit() and int(register) != 0) or registers[register] != 0:
                current_instruction += value
            else:
                current_instruction += 1

        if action != 'jnz':
            current_instruction += 1

    return registers['h']


def get_value(registers, value):
    if value.startswith('-') or value.isdigit():
        new_value = int(value)
    else:
        new_value = registers[value]

    return new_value


registers = dict()
instructions = list()

with open("resources/day22", "rt") as f:
    for line in f:
        split = line.split()
        instructions.append(split)
        if split[1].isalpha():
            if split[1] == 'a':
                registers['a'] = 1
            else:
                registers[split[1]] = 0

    print(read_instructions(registers, instructions))
