active_cubes = {}

with open("17.txt") as f:
    for y, l in enumerate([x.strip() for x in f.readlines()]):
        for x, v in enumerate(l):
            if v == "#":
                active_cubes[(x,y,0,0)] = 1

def part1(cycles, use_w=False):
    cubes = active_cubes
    for _ in range(cycles):
        temp = {}
        neighbor_counts = {}

        #Go through every active cube and increment the neighbor count for all adjacent cubes
        for cube in cubes:
            x, y, z, w = cube
            wmin = w - 1 if use_w else 0
            wmax = w + 2 if use_w else 1
            for nx in range(x-1, x+2):
                for ny in range(y-1, y+2):
                    for nz in range(z-1, z+2):
                        for nw in range(wmin, wmax):
                            if (nx,ny,nz,nw) != cube:
                                if (nx, ny, nz, nw) not in neighbor_counts:
                                    neighbor_counts[(nx, ny, nz, nw)] = 1
                                else:
                                    neighbor_counts[(nx, ny, nz, nw)] += 1
        
        #Go through all cubes in neighbor_counts and check for conditions to mark cube active.
        for cube in neighbor_counts:
            neighbor_count = neighbor_counts[cube]
            if neighbor_count == 3 or (cube in cubes and neighbor_count == 2):
                    temp[cube] = 1
        cubes = temp
    return len(cubes)


print("Part 1: %d" % part1(6))
print("Part 2: %d" % part1(6, use_w=True))
