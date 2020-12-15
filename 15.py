import time
input = []
with open("15.txt") as f:
    input = f.readline().split(",")

def part1(limit):
    hist = {}
    last = None
    i = 1
    while i < limit + 1:
        if i < len(input) + 1:
            a = int(input[i-1])
            speak = a
        else:
            if last not in hist:
                speak = 0
            else:
                speak = i - hist[last] - 1
        if last is not None:
            hist[last] = i-1
        last = speak
        i += 1
    return speak

print("Part 1: %d" % part1(2020))
print("Part 1: %d" % part1(30000000))
