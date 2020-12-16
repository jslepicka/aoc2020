import time
input = []
with open("15.txt") as f:
    input = f.readline().split(",")

def part1(limit):
    hist = [-1] * (limit + 1)
    last = limit
    
    for i, val in enumerate(input):
        val = int(val)
        hist[val] = i + 1
        speak = val
    
    i = len(input) + 1
    while i < limit + 1:
        if hist[last] == -1:
            speak = 0
        else:
            speak = i - hist[last] - 1
        hist[last] = i-1
        last = speak
        i += 1
    return speak

print("Part 1: %d" % part1(2020))

start = time.time()
print("Part 1: %d" % part1(30000000))
print(time.time() - start)


