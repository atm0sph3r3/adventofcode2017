start_of_group = '{'
end_of_group = '}'
start_of_garbage = '<'
end_of_garbage = '>'
cancel = '!'

with open("resources/day9", "rt") as f:
    total = 0
    level = 0
    in_garbage = False
    skip_next = False
    for line in f:
        for i in range(len(line)):
            char = line[i]

            if skip_next:
                skip_next = False
            elif char == cancel:
                skip_next = True
            elif not in_garbage:
                if char == start_of_garbage:
                    in_garbage = True
                elif char == start_of_group:
                    level = level + 1
                    total = total + level
                elif char == end_of_group:
                    level = level - 1
            elif in_garbage:
                if char == end_of_garbage:
                    in_garbage = False

        print(total)
