generator_a_start = 116
generator_a_multiple = 16807
generator_b_start = 299
generator_b_multiple = 48271
divisor = 2147483647
count = 5000000
matches = 0
pairs = 0
generator_a_matches = list()
generator_b_matches = list()

while len(generator_a_matches) <= count or len(generator_b_matches) <= count:
    generator_a_next_value = (generator_a_start * generator_a_multiple) % divisor
    generator_b_next_value = (generator_b_start * generator_b_multiple) % divisor

    if generator_a_next_value % 4 == 0:
        generator_a_matches.append(generator_a_next_value)
    if generator_b_next_value % 8 == 0:
        generator_b_matches.append(generator_b_next_value)

    generator_a_start = generator_a_next_value
    generator_b_start = generator_b_next_value

for i in range(count):
    if generator_a_matches[i] & 0xFFFF == generator_b_matches[i] & 0xFFFF:
        matches += 1


print(matches)
