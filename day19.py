maze = list()
up = "up"
down = "down"
left = "left"
right = "right"
change = '+'
last_letter = ''
horizontal = '-'
vertical = '|'
letters = list()
direction = down

with open("resources/day19", "rt") as f:
    for line in f:
        maze.append([character.strip() for character in line.rstrip('\n')])

    row = 0
    column = 0
    steps = 0
    for each in range(len(maze[0])):
        if maze[0][each] == '|':
            column = each

    while True:
        if row < 0 or row >= len(maze) or column < 0 or column >= len(maze[row]) or not maze[row][column]:
            break

        current_char = maze[row][column]
        if len(current_char) > 0:
            steps += 1
        if current_char.isalpha():
            last_letter = current_char
            letters.append(current_char)

        if maze[row][column] == change:
            if direction == up or direction == down:
                if column - 1 >= 0 and len(maze[row]) > column \
                        and (maze[row][column - 1] == horizontal or maze[row][column-1].isalpha()):
                    direction = left
                    column -= 1
                else:
                    direction = right
                    column += 1
            else:
                if row - 1 >= 0 and len(maze[row - 1]) > column \
                        and (maze[row - 1][column] == vertical or maze[row-1][column].isalpha()):
                    direction = up
                    row -= 1
                else:
                    direction = down
                    row += 1
        elif direction == down:
            row += 1
        elif direction == up:
            row -= 1
        elif direction == right:
            column += 1
        elif direction == left:
            column -= 1

    print(''.join(letters))
    print(steps)

