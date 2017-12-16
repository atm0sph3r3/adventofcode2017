with open("resources/day13", "rt") as f:
    layers = dict()
    max_layer = 0
    caught = 1

    for line in f:
        split = line.split(': ')
        layers[int(split[0])] = int(split[1])
        max_layer = int(split[0])

    offset = 0
    while caught != 0:
        offset += 1
        caught = 0
        for i in range(max_layer + 1):
            if i in layers.keys():
                length = layers[i] * 2 - 2
                if (i + offset) % length == 0:
                    if i == 0:
                        caught += 1
                    else:
                        caught += i * layers[i]

    print(caught)
    print(offset)
