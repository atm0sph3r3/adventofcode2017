class Layer(object):
    def __init__(self, layer, size):
        self.layer = layer
        self.size = size
        self.current_position = 0
        self.direction = 1


layers = []

with open("resources/day13", "rt") as f:
    count = 0
    for line in f:
        split = line.split(': ')
        while int(split[0]) > count:
            layers.append(Layer(count, 0))
            count += 1

        layers.append(Layer(int(split[0]), int(split[1])))
        count += 1

    caught = 0
    for i in range(len(layers)):
        current_layer = layers[i]
        if current_layer.current_position == 0:
            caught = current_layer.size * current_layer.layer

        for j in range(i+1, len(layers)):
            next_layer = layers[j]
            next_position = next_layer.current_position + next_layer.direction

            if next_position == next_layer.size:
                next_layer.current_position -= 1
                next_layer.direction = -1
            elif next_position == -1:
                next_layer.current_position += 1
                next_layer.direction = 1
            else:
                next_layer.current_position = next_position

    print(caught)


