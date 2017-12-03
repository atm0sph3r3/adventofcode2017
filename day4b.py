with open("resources/day4", "rt") as f:
    valid_passphrases = 0
    for line in f:
        split_phrase = line.split()

        phrase_set = set()
        for word in split_phrase:
            word_as_list = sorted(list(word))
            word_sorted = ''.join(word_as_list)
            phrase_set.add(word_sorted)

        if len(split_phrase) == len(phrase_set):
            valid_passphrases = valid_passphrases + 1

    print(valid_passphrases)

