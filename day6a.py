with open("resources/day6", "rt") as f:
    for line in f:
        original = [int(each) for each in line.split()]
        count = 0
        seen = list()
        seen.append(list(original))

        while True:
            count = count + 1
            max_value = -1
            max_index = -1
            for i in range(len(original)):
                if original[i] > max_value:
                    max_value = original[i]
                    max_index = i

            original[max_index] = 0
            current_index = (max_index + 1) % len(original)
            for i in range(max_value, 0, -1):
                original[current_index] = original[current_index] + 1
                current_index = (current_index + 1) % len(original)

            found = False
            for item in seen:
                if item == original:
                    found = True
                    break

            if found:
                print(count)
                break

            seen.append(list(original))
