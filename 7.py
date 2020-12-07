import re
bags = {}

with open("7.txt") as f:
   for l in [x.strip() for x in f.readlines()]:
        m = re.match(r'(\w+ \w+) bags contain', l)
        bag_color = m[1]
        bags[bag_color] = {}
        m = re.findall(r'(\d+) (\w+ \w+)', l)
        for x in m:
            bags[bag_color][x[1]] = int(x[0])

#can bag contain color
def can_contain(bag, color):
    if color in bags[bag]:
        return True
    else:
        for c in bags[bag]:
            if can_contain(c, color):
                return True
    return False

def count_children(color):
    child_count = 0
    for child in bags[color]:
        x = count_children(child)
        child_count += x * bags[color][child]
    return child_count + 1

def part1():
    count = 0
    for color in bags:
        if can_contain(color, "shiny gold"):
            count += 1
    return count

def part2():
    return count_children("shiny gold") - 1

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())