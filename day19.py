with open("resources/day19", "r") as f:
    maze = []
    for line in f:
        maze.append(line[:-1])

letters = []
change_direction = '+'
empty_space = ' '
steps = 0

position = maze[0].find('|') + 0j
direction = 1j
current_char = maze[int(position.imag)][int(position.real)]

while current_char != ' ':
    steps += 1
    if current_char.isalpha():
        letters.append(current_char)
    elif current_char == change_direction:
        # rotate 90 degrees
        new_direction = direction * 1j
        new_position = position + new_direction
        try:
            if maze[int(new_position.imag)][int(new_position.real)] != ' ':
                direction = new_direction
            else:
                # rotate 90 degrees the other way
                direction *= -1j
        except IndexError:
            direction *= -1j

    position += direction
    current_char = maze[int(position.imag)][int(position.real)]

print(''.join(letters))
print(steps)
