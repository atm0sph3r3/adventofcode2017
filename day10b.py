with open("resources/day10", "rt") as f:
    for line in f:
        crypto_length = 256
        lengths = list()

        for i in range(len(line)):
            lengths.append(ord(line[i]))
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
        print(dense_hash)
        for item in dense_hash:
            output = output + "{:02x}".format(item)

        print(output)
