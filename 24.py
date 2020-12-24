import re

input = []
with open("24.txt") as f:
    input += [x.strip() for x in f.readlines()]

#q, r axial coordinates: https://www.redblobgames.com/grids/hexagons/

def move(q, r, moves):
    dirs = re.findall(r'(e|w|s.|n.)', moves)
    for dir in dirs:
        if dir == "e":
            q += 1
        elif dir == "w":
            q -= 1
        elif dir == "se":
            r += 1
        elif dir == "sw":
            q -= 1
            r += 1
        elif dir == "ne":
            q += 1
            r -= 1
        elif dir == "nw":
            r -= 1
    return (q, r)

def part1():
    grid = {}
    for i in input:
        q, r = move(0, 0, i)
        if (q,r) not in grid or grid[(q, r)] == "white":
            grid[(q, r)] = "black"
        else:
            grid[(q, r)] = "white"
    count = sum(1 for x in grid.values() if x == "black")
    return count, grid

def part2(grid, iterations):
    for _ in range(iterations):
        neighbor_counts = {}
        g = grid.copy()
        for loc in [k for k, v in grid.items() if v == "black"]:
            if loc not in neighbor_counts:
                neighbor_counts[loc] = 0
            neighbors = [(1, 0), (-1, 0), (0, 1), (-1, 1), (1, -1), (0, -1)]
            for n in neighbors:
                qq, rr = loc[0] + n[0], loc[1] + n[1]
                if (qq, rr) not in neighbor_counts:
                    neighbor_counts[(qq, rr)] = 1
                else:
                    neighbor_counts[(qq, rr)] += 1
        for loc in neighbor_counts:
            if (loc not in grid or grid[loc] == "white") and neighbor_counts[loc] == 2:
                g[loc] = "black"
            elif neighbor_counts[loc] == 0 or neighbor_counts[loc] > 2:
                g[loc] = "white"
        grid = g
    return sum(1 for x in grid.values() if x == "black")
        
count, grid = part1()
print("Part 1: %d" % count)
print("Part 2: %d" % part2(grid, 100))
