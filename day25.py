class Action(object):
    def __init__(self, value_to_write, move, next_state):
        self.next_state = next_state
        self.move = move
        self.value_to_write = value_to_write


class State(object):
    def __init__(self, name, action):
        self.action = action
        self.name = name


states = dict()
states['A'] = {0: Action(1, 1, 'B'), 1: Action(0, -1, 'C')}
states['B'] = {0: Action(1, -1, 'A'), 1: Action(1, 1, 'D')}
states['C'] = {0: Action(1, 1, 'A'), 1: Action(0, -1, 'E')}
states['D'] = {0: Action(1, 1, 'A'), 1: Action(0, 1, 'B')}
states['E'] = {0: Action(1, -1, 'F'), 1: Action(1, -1, 'C')}
states['F'] = {0: Action(1, 1, 'D'), 1: Action(1, 1, 'A')}

state = 'A'
steps = 12173597
values = dict()
values[0] = 0
current_position = 0
count = 0

for _ in range(steps):
    action_to_complete = states[state][values[current_position]]
    values[current_position] = action_to_complete.value_to_write
    current_position += action_to_complete.move
    state = action_to_complete.next_state

    if current_position not in values:
        values[current_position] = 0

for k, v in values.items():
    if v == 1:
        count += 1

print(count)


