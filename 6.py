#input = input[group][person] = response

input = {}

group = 0
person = 0
input[0] = {}
with open("6.txt") as f:
    for l in [x.strip() for x in f.readlines()]:
        if l == "":
            group += 1
            person = 0
            input[group] = {}
        else:
            input[group][person] = l
            person += 1

def part1():
    count = 0
    for group in input:
        responses = {}
        for person in input[group]:
            for response in input[group][person]:
                responses[response] = 1
        count += len(responses.keys())
    return count

def part2():
    count = 0
    for group in input:
        responses = {}
        group_size = len(input[group].keys())
        for person in input[group]:
            for response in input[group][person]:
                if response not in responses:
                    responses[response] = 1
                else:
                    responses[response] += 1
        count += list(responses.values()).count(group_size)
    return count


print("Part 1 sum of counts: %d" % part1())
print("Part 2 sum of counts: %d" % part2())