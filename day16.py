programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
places = dict()
for i in range(len(programs)):
    places[programs[i]] = i

with open("resources/testing", "rt") as f:
    for line in f:
        split = line.split(',')
        for each in split:
            action = each[0]
            if action == 's':
                number = int(each[1:])
                temp = list()
                for i in range(len(programs) - number, len(programs)):
                    temp.append(programs[i])
                for i in range(0, len(programs) - number):
                    temp.append(programs[i])
            elif action == 'x':
                pass

            elif action == 'p':
                pass