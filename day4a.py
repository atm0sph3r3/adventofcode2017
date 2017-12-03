with open("resources/day4", "rt") as f:
    valid_passphrases = 0
    for line in f:
        split_phrase = line.split()
        split_phrase_as_set = set(split_phrase)

        if len(split_phrase) == len(split_phrase_as_set):
            valid_passphrases = valid_passphrases + 1

    print(valid_passphrases)