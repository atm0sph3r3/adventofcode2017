input = 386
inputs = 2017
buffer = [None for _ in range(inputs)]
current_position = 0

buffer[0] = 0
for i in range(1, inputs):
    next = ((current_position + input) % i) + 1

    if buffer[next] is None:
        buffer[next] = i
    else:
        replacement_value = i
        for replace in range(next, i - 1):
            temp = buffer[replace]
            buffer[replace] = replacement_value
            replacement_value = temp

    current_position = next

for i in range(len(buffer)):
    if buffer[i] == 0:
        print(buffer[i+1])

buffer = [0 for _ in range(2)]
current_position = 0
inputs = 50000001
for i in range(1, inputs):
    next = ((current_position + input) % i) + 1
    if next == 1:
        buffer[1] = i

    current_position = next

print(buffer[1])




