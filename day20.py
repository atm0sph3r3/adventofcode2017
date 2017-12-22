file = "resources/day20"
position = list()
velocity = list()
acceleration = list()


def get_xyz(input):
    xyz = input.split('=')
    list_as_str = (xyz[1].strip()[1:-1]).split(',')
    return [int(each) for each in list_as_str]


with open(file, "rt") as f:
    for line in f:
        first_split = line.split(', ')
        position.append(get_xyz(first_split[0]))
        velocity.append(get_xyz(first_split[1]))
        acceleration.append(get_xyz(first_split[2]))

    positions = [0 for _ in range(len(position))]
    removed = [False for _ in range(len(position))]

    for _ in range(1000):
        for i in range(0, len(position)):
            velocity[i][0] += acceleration[i][0]
            velocity[i][1] += acceleration[i][1]
            velocity[i][2] += acceleration[i][2]
            position[i][0] += velocity[i][0]
            position[i][1] += velocity[i][1]
            position[i][2] += velocity[i][2]
            positions[i] = abs(position[i][0]) + abs(position[i][1]) + abs(position[i][2])

        for i in range(len(position)):
            if not removed[i]:
                for j in range(len(position)):
                    if not removed[j] and i != j:
                        if position[i] == position[j]:
                            removed[i] = True
                            removed[j] = True

    closest = 0
    closest_distance = positions[0]
    for i in range(1, len(positions)):
        this_distance = positions[i]
        if this_distance < closest_distance:
            closest_distance = this_distance
            closest = i

    print(closest)

    left = 0
    for each in removed:
        if not each:
            left += 1
    print(left)




