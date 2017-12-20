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

with open("resources/testing", "rt") as f:
    for line in f:
        maze.append([character for character in line])

    row = 0
    column = 0
    steps = 0
    for each in range(len(maze[0])):
        if maze[0][each] == '|':
            column = each

    while True:
        if row < 0 or row >= len(maze) or column < 0 or column >= len(maze[row]):
            break

        if maze[row][column].isalpha():
            last_letter = maze[row][column]
            letters.append(maze[row][column])

        if maze[row][column] == change:
            if direction == up or direction == down:
                if column - 1 >= 0 and len(maze[row]) > column and maze[row][column - 1] == horizontal:
                    direction = left
                    column -= 1
                else:
                    direction = right
                    column += 1
            else:
                if row - 1 >= 0 and len(maze[row - 1]) > column and maze[row - 1][column] == vertical:
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

        steps += 1

    print(''.join(letters))
    print(steps)

