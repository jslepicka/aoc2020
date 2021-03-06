import math
import time

TOP, LEFT, BOTTOM, RIGHT = 0, 1, 2, 3

tiledata = {}

with open("20.txt") as f:
    tile_info = f.read().split("\n\n")
    for l in [x.strip() for x in tile_info]:
        tile_num = 0
        tile_data = []
        for ll in [x.strip() for x in l.split("\n")]:
            if ll.startswith("Tile"):
                tile_num = int(ll.split(" ")[1][:-1])
            else:
                tile_data.append(ll)
        tiledata[tile_num] = tile_data

map_d = int(math.sqrt(len(tiledata.keys())))

def get_edges(index, orientation):
    top = tiledata[index][0]
    bottom = tiledata[index][9]
    left = ""
    right = ""

    for i in range(10):
        left += tiledata[index][i][0]
        right += tiledata[index][i][9]

    if orientation == 0:
        ret = (top, left, bottom, right)
    elif orientation == 1: #rotate left 90
        ret = (right, top[::-1], left, bottom[::-1])
    elif orientation == 2: #rotate left 180
        ret = (bottom[::-1], right[::-1], top[::-1], left[::-1])
    elif orientation == 3: #rotate left 270
        ret = (left[::-1], bottom, right[::-1], top)
    elif orientation == 4: #flip horiz
        ret = (top[::-1], right, bottom[::-1], left)
    elif orientation == 5: #flip horiz, rotate left 90
        ret = (left, top, right, bottom)
    elif orientation == 6: #flip horiz, rotate left 180
        ret = (bottom, left[::-1], top, right[::-1])
    elif orientation == 7: #flip horiz, rotate left 270
        ret = (right[::-1], bottom[::-1], left[::-1], top[::-1])
    return ret

#return an array of the tile data in the requested orientation
def get_tiledata(index, orientation, remove_border = False):
    ret = []
    if orientation < 4: #rotated left 90
        for i, t in enumerate(tiledata[index]):
            if remove_border:
                if i == 0 or i == 9:
                    continue
                ret.append(t[1:-1])
            else:
                ret.append(t)
        ret = rotate_tile(ret, orientation)
    elif orientation < 8:
        for i, t in enumerate(tiledata[index]):
            if remove_border:
                if i == 0 or i == 9:
                    continue
                ret.append(t[::-1][1:-1])
            else:
                ret.append(t[::-1])
        ret = rotate_tile(ret, orientation-4)       
    return ret

def rotate_tile(tiledata, n):
    if n == 0:
        return tiledata
    temp = tiledata
    for _ in range(n):
        temp = list(zip(*temp))[::-1]
    ret = []
    for x in temp:
        ret.append("".join(x))
    return ret

def hflip_tile(tiledata):
    ret = []
    for l in tiledata:
        ret.append(l[::-1])
    return ret
        
def print_map(m, remove_border):
    ret = []
    tiles = {}
    for x, y in m:
        tile_index, tile_orientation = m[(x,y)]
        tiles[(x,y)] = get_tiledata(tile_index, tile_orientation, remove_border)
    
    tile_width = 8 if remove_border else 10
    tile_height = 8 if remove_border else 10

    for y in range(map_d * tile_height):
        line = ""
        for x in range(map_d * tile_width):
            line += tiles[(x//tile_width, y//tile_height)][y % tile_height][x % tile_width]
        ret.append(line)

    return ret

def overlay_dragons(m):
    width = 8 * map_d
    height = 8 * map_d
    count = 0
    dragon = [(-18, 1), (-13, 1), (-12, 1), (-7, 1), (-6, 1), (-1, 1), (0, 1), (1, 1), (-17, 2), (-14, 2), (-11, 2), (-8, 2), (-5, 2), (-2, 2)]

    for y in range(height):
        for x in range(width):
            if x >= 18 and y < (height - 2):
                if m[y][x] == "#":
                    if y == 2:
                        j = 1
                    dragon_here = True
                    for d in dragon:
                        if m[y + d[1]][x + d[0]] != "#":
                            dragon_here = False
                            break
                    if dragon_here:
                        print("found dragon at %d, %d" % (x, y))
                        count += 1
                        m[y] = m[y][:x] + "O" + m[y][x+1:]
                        for d in dragon:
                            m[y + d[1]] = m[y+d[1]][:x+d[0]] + "O" + m[y+d[1]][x+d[0]+1:]

    return count

def part1():
    edges_cache = {}

    for t in tiledata:
        for o in range(8):
            edges_cache[(t, o)] = get_edges(t, o)

    for tile_index in tiledata:
        stack = []
        for orientation in range(8):
            stack.append(  (tile_index, orientation, [tile_index], 0, 0, {(0, 0): (tile_index, orientation)})  )

        while len(stack) != 0:
            (t, o, visited, x, y, current_map) = stack.pop()
            #we are in position x, y, where a tile already exists, and now we want to find a tile that fits
            #in the next location, which is either one to the right, or at the start of the next row
            current_edges = edges_cache[(t, o)]
            current_right = current_edges[RIGHT]

            if x == map_d - 1:
                start_tile_id, start_tile_orientation = current_map[(0, y)]
                start_tile_bottom = edges_cache[(start_tile_id, start_tile_orientation)][BOTTOM]

            if y > 0 and x < map_d - 1:
                tile_above_id, tile_above_orientation = current_map[(x + 1, y-1)]
                tile_above_bottom = edges_cache[(tile_above_id, tile_above_orientation)][BOTTOM]

            for tt in tiledata.keys() - visited:
                for oo in range(8):
                    #check if tt, oo is a possible fit and if so add to stack
                    valid = False

                    #if we're in the top row, and not the last column, find a tile that fits to the right
                    proposed_edges = edges_cache[(tt, oo)]
                    proposed_left = proposed_edges[LEFT]
                    proposed_top = proposed_edges[TOP]

                    if x == map_d - 1: #in the last column, so we're checking in x=0 of the next row
                        if proposed_top == start_tile_bottom:
                            valid = True
                    elif y == 0: #top row, don't need to check above
                        if current_right == proposed_left:
                            valid = True
                    else:
                        if current_right == proposed_left and proposed_top == tile_above_bottom:
                            valid = True

                    if valid:
                        next_x = x + 1
                        next_y = y
                        if x == map_d - 1:
                            next_x = 0
                            next_y = y + 1
                        
                        new_map = current_map.copy()
                        new_map[(next_x, next_y)] = (tt, oo)
                        v = visited.copy()
                        v.append(tt)

                        stack.append( (tt, oo, v, next_x, next_y, new_map) )
                        if len(new_map.keys()) == map_d*map_d:
                            prod = 1
                            for a in [0, map_d-1]:
                                for b in [0, map_d-1]:
                                    prod *= new_map[a,b][0]
                            print("found valid map")
                            return new_map, prod
    return None, None

def part2(m):
    image = print_map(m, True)
    for o in range(8):
        print("testing orientation %d" % o)
        image = rotate_tile(image, o % 4)
        if o == 4:
            image = hflip_tile(image)
        count = overlay_dragons(image)
        if count > 0:
            hash_count = 0
            for i in image:
                hash_count += i.count("#")
            return hash_count
    return 0

start = time.time()
valid_map, ret = part1()
print("Part 1: %d" % ret)
print("Part 2: %d" % part2(valid_map))
print(time.time() - start)
