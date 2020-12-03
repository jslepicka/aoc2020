input = []
with open("3.txt") as f:
    input = [x.strip() for x in f.readlines()]

width = len(input[0])
height = len(input)

def part1(right_slope, down_slope):
    x = 0
    y = 0
    trees = 0
    while y < height:
        if input[y][x] == "#":
            trees += 1
        x = (x  + right_slope) % width
        y += down_slope
    return trees

print("Part 1: %d" % part1(3, 1))
product = 1
for i in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    product *= part1(i[0], i[1])
print("Part 2: %d" % product)