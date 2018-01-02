with open('resources/day23', 'r') as f:
    mapping = []
    for line in f:
        row = list(line.strip())
        mapping.append(row)

padded_mapping = []
infected = '#'
clean = '.'
weakened = 'w'
flagged = 'f'

direction = -1
count = 0

padding = 1000

for _ in range(padding):
    padded_mapping.append(['.'] * (padding * 2 + len(mapping)))

for each in mapping:
    row = ['.'] * padding
    row.extend(each)
    row.extend(['.'] * padding)
    padded_mapping.append(row)

for _ in range(padding):
    padded_mapping.append(['.'] * (padding * 2 + len(mapping)))


position = complex(len(padded_mapping) // 2, len(padded_mapping[0]) // 2)


def get_state():
    return padded_mapping[int(position.real)][int(position.imag)]


def set_state(state):
    padded_mapping[int(position.real)][int(position.imag)] = state


for _ in range(10_000_000):
    if get_state() == infected:
        direction *= -1j
        set_state(flagged)
    elif get_state() == clean:
        direction *= 1j
        set_state(weakened)
    elif get_state() == weakened:
        set_state(infected)
        count += 1
    elif get_state() == flagged:
        set_state(clean)
        direction *= -1
    else:
        print("this shouldn't happen")

    position += direction

print(count)
