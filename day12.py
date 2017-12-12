programs = dict()

with open("resources/day12", "rt") as f:
    for line in f:
        initial_split = line.split(' <-> ')
        connected = initial_split[1].split(', ')
        connected = set([item.strip() for item in connected])
        programs[initial_split[0]] = connected

    for k, v in programs.items():
        for i in v:
            for j in v:
                programs[i].add(j)

    print(len(programs['0']))

    groups = set()
    for k, v in programs.items():
        groups.add(str(sorted(list(v))))

    print(len(groups))

