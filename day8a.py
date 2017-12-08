with open('resources/day8', 'rt') as f:
    registers = dict()
    for line in f:
        split = line.split()
        register = split[0]
        action = split[1]
        amount = int(split[2])
        condition_register = split[4]
        condition = split[5]
        condition_amount = int(split[6])
        meets_condition = False

        if register not in registers:
            registers[split[0]] = 0

        if condition_register not in registers:
            registers[condition_register] = 0

        if condition == ">=" and registers[condition_register] >= condition_amount:
            meets_condition = True
        elif condition == "<=" and registers[condition_register] <= condition_amount:
            meets_condition = True
        elif condition == "==" and registers[condition_register] == condition_amount:
            meets_condition = True
        elif condition == "!=" and registers[condition_register] != condition_amount:
            meets_condition = True
        elif condition == "<" and registers[condition_register] < condition_amount:
            meets_condition = True
        elif condition == ">" and registers[condition_register] > condition_amount:
            meets_condition = True

        if meets_condition:
            if action == 'dec':
                registers[register] = registers[register] - amount
            else:
                registers[register] = registers[register] + amount

    max_value = None
    for k, v in registers.items():
        if max_value is None:
            max_value = v
        else:
            if v > max_value:
                max_value = v

    print(max_value)
