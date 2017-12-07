class Program(object):

    def __init__(self, name, weight, programs) -> None:
        self.name = name
        self.weight = weight
        self.programs = programs


with open('resources/day7', 'rt') as f:
    programs = set()
    for line in f:
        split = line.split('->')
        second_split = split[0].split()
        name = second_split[0]
        weight = second_split[1][1:len(second_split[1]) - 1]
        programs_on_top = list()
        if len(split) == 2:
            programs_on_top = split[1].split(', ')
            programs_on_top = [item.strip() for item in programs_on_top]

        programs.add(Program(name, int(weight), programs_on_top))

    for program in programs:
        if len(program.programs) != 0:
            found_program = True
            for comparison_program in programs:
                if comparison_program.name != program.name and program.name in comparison_program.programs:
                    found_program = False
                    break

            if found_program:
                print(program.name)

