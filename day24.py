class Port(object):
    def __init__(self, left, right):
        self.ports = [left, right]
        self.total = right + left


ports = list()
ports_dict = dict()


def get_max(previous, output, results_list):
    connections = [each for each in ports_dict[output] if each not in previous]

    if not connections:
        results_list.append([sum(item.total for item in previous), len(previous)])
        return

    for each_connection in connections:
        previous_copy = previous[:]
        previous_copy.append(each_connection)

        if each_connection.ports[0] == output and each_connection.ports[1] == output:
            next_output_port = output
        elif each_connection.ports[0] != output:
            next_output_port = each_connection.ports[0]
        else:
            next_output_port = each_connection.ports[1]

        get_max(previous_copy, next_output_port, results_list)


with open("resources/day24", "rt") as f:
    for line in f:
        split = line.split('/')
        port_1 = int(split[0])
        port_2 = int(split[1])
        ports_dict[port_1] = list()
        ports_dict[port_2] = list()
        ports.append(Port(port_1, port_2))

    for key in ports_dict.keys():
        for port in ports:
            if key in port.ports:
                ports_dict[key].append(port)

    results = list()
    for start in ports_dict[0]:
        for port in start.ports:
            if port != 0:
                get_max([start], port, results)

    strongest = -1
    longest = -1
    for result in results:
        total = result[0]
        length = result[1]
        if length > longest:
            longest = length
            strongest = total
        elif length == longest:
            if total > strongest:
                strongest = total

    print(strongest)
    print(longest)

