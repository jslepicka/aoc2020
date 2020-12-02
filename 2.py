import re

input = []

with open("2.txt") as f:
    input = [x.strip() for x in f.readlines()]

def part1():
    valid = 0
    for line in input:
        m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        if m is not None:
            min_count = int(m.group(1))
            max_count = int(m.group(2))
            letter = m.group(3)
            password = m.group(4)
            letter_count = password.count(letter)
            if letter_count >= min_count and letter_count <= max_count:
                valid += 1
    return valid

def part2():
    valid = 0
    for line in input:
        m = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        if m is not None:
            pos1 = int(m.group(1)) - 1
            pos2 = int(m.group(2)) - 1
            letter = m.group(3)
            password = m.group(4)
            try:
                if (password[pos1] == letter) ^ (password[pos2] == letter):
                    valid += 1
            except IndexError:
                continue
    return valid

print("Part 1 valid passwords: %d" % part1())
print("Part 2 valid passwords: %d" % part2())

