import re
rules = {}
strings = []

with open("19.txt") as f:
    sections = f.read().split("\n\n")
    for s in [x.strip() for x in sections[0].split("\n")]:
        index, r = s.split(":")
        index = int(index)
        r = r.strip().replace("\"", "")
        rules[index] = r
    strings = [x.strip() for x in sections[1].split("\n")]

def resolve(rules, i, p2=False, cache=None):
    if cache is None:
        cache = {}
    if i in cache:
        return cache[i]
    out = "("
    for c in rules[i].split(" "):
        if c.isdigit():
            ii = int(c)
            out += resolve(rules, ii, p2, cache)
            if p2 and i == 11:
                out += "{X}"
        else:
            out += c
    out = (out + ")").replace(" ", "")
    if p2 and i == 8:
        out += "+"
    cache[i] = out
    return out

def part1():
    part1_rules = {}
    for r in rules:
        part1_rules[r] = "^" + resolve(rules, r) + "$"
    regex_string = part1_rules[0]
    count = 0
    for s in strings:
        m = re.search("^" + regex_string + "$", s)
        if m:
            count += 1
    return count

def part2():
    part2_rules = {}
    for r in rules:
        part2_rules[r] = "^" + resolve(rules, r, p2=True) + "$"
    count = 0
    x = 1
    while True:
        last_count = count
        regex_string = part2_rules[0].replace("X", str(x))
        for s in strings:
            m = re.search("^" + regex_string + "$", s)
            if m:
                count += 1
        print("%d: %d" % (x, count - last_count))
        if count - last_count == 0:
            break
        last_count = count
        x += 1
    return count

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())