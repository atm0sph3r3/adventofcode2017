def swap(start, end, programs):
    temp = programs[start]
    programs[start] = programs[end]
    programs[end] = temp


with open("resources/day16", "rt") as f:
    for line in f:
        programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
        original = list(programs)
        split = line.split(',')
        repeats = 0
        rearranged = list()
        for each_round in range(1000000000 % 24):
            for each in split:
                action = each[0]
                if action == 's':
                    number = int(each[1:])
                    temp = list()
                    for last in range(len(programs) - number, len(programs)):
                        temp.append(programs[last])
                    for first in range(0, len(programs) - number):
                        temp.append(programs[first])
                    programs = temp
                elif action == 'x':
                    programs_split = each.split('/')
                    start = int(programs_split[0][1:])
                    end = int(programs_split[1])
                    swap(start, end, programs)
                elif action == 'p':
                    programs_split = each.split('/')
                    start = programs_split[0][1:]
                    end = programs_split[1]
                    start_index = -1
                    end_index = -1
                    for index in range(len(programs)):
                        if start == programs[index]:
                            start_index = index
                        elif end == programs[index]:
                            end_index = index
                    swap(start_index, end_index, programs)
        print(''.join(programs))


