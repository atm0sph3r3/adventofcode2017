input = "amgozmfv"
crypto_length = 256
used_map = {'0': 0, '1': 1, '2': 1, '3': 2, '4': 1, '5': 2, '6': 2, '7': 3, '8': 1, '9': 2,
            'a': 2, 'b': 3, 'c': 2, 'd': 3, 'e': 3, 'f': 4}

inputs = ["{}-{}".format(input, each) for each in range(128)]
hashes = list()
dense_hashes = list()
for row in inputs:
    lengths = list()

    for i in range(len(row)):
        lengths.append(ord(row[i]))
    for item in [17, 31, 73, 47, 23]:
        lengths.append(item)

    skip_size = 0
    crypto = [i for i in range(crypto_length)]
    starting_index = 0

    for _ in range(64):
        for length in lengths:
            initial_index = starting_index
            ending_index = (starting_index + length - 1) % crypto_length
            for _ in range(int(length / 2)):
                temp = crypto[starting_index]
                crypto[starting_index] = crypto[ending_index]
                crypto[ending_index] = temp
                starting_index = (starting_index + 1) % crypto_length
                ending_index = (ending_index - 1) % crypto_length

            starting_index = (initial_index + length + skip_size) % crypto_length
            skip_size = skip_size + 1

    dense_hash = list()
    each_hash = 0
    for i in range(crypto_length):
        if i % 16 == 0 and i != 0:
            dense_hash.append(each_hash)
            each_hash = crypto[i]
        else:
            each_hash = crypto[i] ^ each_hash
    dense_hash.append(each_hash)

    output = ""
    for item in dense_hash:
        output = output + "{:02x}".format(item)
    dense_hashes.append(dense_hash)
    hashes.append(output)

total_used = 0
for hash in hashes:
    for each in hash:
        total_used += used_map[each]
print(total_used)

board = [list() for _ in range(128)]
for i in range(len(dense_hashes)):
    for each in dense_hashes[i]:
        multiple = 128
        for bit in range(7, -1, -1):
            value = multiple & each
            value >>= bit
            board[i].append([value, None])
            multiple >>= 1


def find_group(board, i, j, group):
    if i + 1 <= 127 and board[i + 1][j][0] == 1 and board[i + 1][j][1] is None:
        board[i + 1][j][1] = group
        find_group(board, i + 1, j, group)
    if j + 1 <= 127 and board[i][j + 1][0] == 1 and board[i][j + 1][1] is None:
        board[i][j + 1][1] = group
        find_group(board, i, j + 1, group)
    if i - 1 >= 0 and board[i - 1][j][0] == 1 and board[i - 1][j][1] is None:
        board[i - 1][j][1] = group
        find_group(board, i - 1, j, group)
    if j - 1 >= 0 and board[i][j - 1][0] == 1 and board[i][j - 1][1] is None:
        board[i][j - 1][1] = group
        find_group(board, i, j - 1, group)


group = -1
for i in range(len(board)):
    for j in range(len(board)):
        if board[i][j][0] == 1 and board[i][j][1] is None:
            group += 1
            board[i][j][1] = group
            find_group(board, i, j, group)

print(group + 1)
