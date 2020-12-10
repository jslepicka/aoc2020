import numpy as np
from numpy.linalg import matrix_power
input = []
with open("10.txt") as f:
   input = [int(x.strip()) for x in f.readlines()]

def part1():
    joltages = sorted(input)
    source = 0
    diff_1 = 0
    diff_3 = 0
    while source < joltages[-1]:
        if source+1 in joltages:
            source = joltages[joltages.index(source+1)]
            diff_1 += 1
        elif source+3 in joltages:
            source = joltages[joltages.index(source+3)]
            diff_3 += 1

    return diff_1 * (diff_3 + 1)

def part2():
    #Per https://www.cs.sfu.ca/~ggbaker/zju/math/paths.html
    #create an adjacency matrix and raise it to x powers to find number of x len paths
    #between i and j.  I have no idea what I'm doing with numpy...
    m = []
    jolt = sorted(input)
    jolt.insert(0, 0)
    jolt.append(jolt[-1] + 3)
    l = len(jolt)
    for i, val in enumerate(jolt):
        a = [0] * l
        for k, j in enumerate(jolt[i+1:]):
            if j-val <= 3:
                a[i+1+k] = 1
        m.append(a)

    paths = 0

    for i in range(1,l+1):
        #needs to be 64-bit to avoid overflow with matrix_power
        mm = np.array(m, dtype=np.uint64)
        mm = matrix_power(mm, i)
        n = mm[0,l-1]
        paths += n
    return paths

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
