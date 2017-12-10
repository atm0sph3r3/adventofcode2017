with open("resources/day10", "rt") as f:
    for line in f:
        crypto_length = 256
        split = line.split(',')
        lengths = [int(item) for item in split]
        skip_size = 0
        crypto = [i for i in range(crypto_length)]
        starting_index = 0

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

    print(crypto)
