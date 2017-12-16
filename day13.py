import copy

class Layer(object):
    def __init__(self, layer, size):
        self.layer = layer
        self.size = size
        self.current_position = 0
        self.direction = 1


def get_caught(layers):
    caught = 0

    for i in range(len(layers)):
        if layers[i].current_position == 0:
            caught += layers[i].size * layers[i].layer
        move(layers, 1)
    return caught


def move(layers_input, times):
    for _ in range(times):
        for j in range(len(layers_input)):
            if layers_input[j].size == 0:
                continue
            next_position = layers_input[j].current_position + layers_input[j].direction

            if next_position == layers_input[j].size:
                layers_input[j].current_position -= 1
                layers_input[j].direction = -1
            elif next_position == -1:
                layers_input[j].current_position += 1
                layers_input[j].direction = 1
            else:
                layers_input[j].current_position = next_position


with open("resources/testing", "rt") as f:
    layers = []
    count = 0
    for line in f:
        split = line.split(': ')
        while int(split[0]) > count:
            layers.append(Layer(count, 0))
            count += 1

        layers.append(Layer(int(split[0]), int(split[1])))
        count += 1

    layers_copy = copy.deepcopy(layers)
    caught = get_caught(layers_copy)
    print(caught)

    offset = 0
    while caught != 0:
        new_layers = copy.deepcopy(layers)
        move(new_layers, offset)
        caught = get_caught(new_layers)
        offset += 1

    print(offset)


