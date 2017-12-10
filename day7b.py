from queue import Queue

adjacent = dict()
weights = dict()
calc_weights = dict()
discs = dict()
programs = []


def get_weight(program):
    if program not in discs:
        return weights[program]
    elif program in calc_weights.keys():
        return calc_weights[program]
    else:
        weight = weights[program]
        for each_program in discs[program]:
            weight = weight + get_weight(each_program)
        return weight

with open('resources/day7', 'rt') as f:
    for line in f:
        split = line.split('->')
        name_weight = split[0].split()
        name = name_weight[0]
        programs.append(name)
        weight = name_weight[1][1:len(name_weight[1]) - 1]
        weights[name] = int(weight)
        if len(split) == 2:
            programs_on_top = split[1].split(', ')
            programs_on_top = [item.strip() for item in programs_on_top]
            discs[name] = programs_on_top
            for program in programs_on_top:
                if program not in adjacent:
                    adjacent[program] = []
                for adjacent_program in programs_on_top:
                    if program != adjacent_program:
                        adjacent[program].append(adjacent_program)

    for item in programs:
        if item not in adjacent.keys():
            print("Root: {}".format(item))
        calc_weights[item] = get_weight(item)

    for k, v in adjacent.items():
        if calc_weights[k] != calc_weights[v[0]]:
            print("program: {}, calc weight: {}, weight: {}, difference: {}".format(k, calc_weights[k], weights[k], calc_weights[k] - calc_weights[v[0]]))

