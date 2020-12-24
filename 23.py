cup_input = None
cups = None

with open("23.txt") as f:
    l = f.readline().strip()
    ll = [int(x) for x in l]
    cup_input = ll
    cups = list(range(0, len(l) + 1))
    cups[0] = 0
    for i, val in enumerate(ll):
        cups[val] = ll[(i+1) % len(ll)]

def part1(cups, iterations):
    starting_cup = cup_input[0]
    max_cup = max(cups)
    for _ in range(iterations):
        pickup = []
        n = starting_cup
        for _ in range(3):
            n = cups[n]
            pickup.append(n)
        dest = starting_cup - 1
        while True:
            if dest == 0:
                dest = max_cup
            if dest in pickup:
                dest -= 1
            else:
                break
        cups[starting_cup] = cups[pickup[2]]
        cups[pickup[2]] = cups[dest]
        cups[dest] = pickup[0]
        starting_cup = cups[starting_cup]
    ret = ""
    n = cups[1]
    while n != 1:
        ret += str(n)
        n = cups[n]
    return ret

def part2():
    n = len(cup_input) + 1
    cups[cup_input[-1]] = n
    while n <= 1_000_000:
        cups.append(n + 1)
        n += 1
    cups[-1] = cup_input[0]
    part1(cups, 10_000_000)
    r = cups[1]
    return r * cups[r]

print("Part 1: %s" % part1(cups.copy(), 100))
print("Part 2: %d" % part2())
