input = []
with open("9.txt") as f:
   input = [int(x.strip()) for x in f.readlines()]

def hassum(num, preamble_start, preamble_len):
    for i in input[preamble_start:preamble_start+preamble_len]:
        r = num - i
        if r in input[preamble_start:preamble_start+preamble_len]:
            return True
    return False

def part1():
    preamble_pos = 0
    preamble_len = 25
    for i in input[preamble_len:]:
        if not hassum(i, preamble_pos, preamble_len):
            return i
        preamble_pos += 1
    return 0

def part2(target):
    l = [x for x in input if x < target]

    for i, val in enumerate(l):
        sum = val
        j = i+1
        while sum < target:
            sum += input[j]
            j+=1
        if sum == target:
            result = sorted(input[i:j])
            return (result[0] + result[-1])
            
    return None

part1 = part1()
print("Part 1: %d" % part1)
print("Part 2: %d" % part2(part1))
