def get_distance(position):
    dx = position[0] - 0
    dy = position[1] - 0
    dxy = dy - dx
    values = [abs(dx), abs(dy), abs(dxy)]
    return max(values)


with open("resources/day11", "rt") as f:
    furthest = None
    position = list()
    # x
    position.append(0)
    # y
    position.append(0)
    for line in f:
        split = line.split(',')

        for each in split:
            if each == 'ne':
                position[0] += 1
                position[1] += 1
            if each == 'nw':
                position[0] -= 1
                position[1] += 0
            elif each == 'n':
                position[0] += 0
                position[1] += 1
            elif each == 'se':
                position[0] += 1
                position[1] += 0
            if each == 'sw':
                position[0] -= 1
                position[1] -= 1
            elif each == 's':
                position[0] += 0
                position[1] -= 1

            if furthest is None:
                furthest = get_distance(position)
            else:
                current_distance = get_distance(position)
                if current_distance > furthest:
                    furthest = current_distance

        print("Distance at end: {}".format(get_distance(position)))
        print("Furthest distance: {}".format(furthest))
    
