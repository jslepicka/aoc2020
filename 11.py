from collections import defaultdict
layout = defaultdict(lambda: None)
layout_width = 0
layout_height = 0
with open("11.txt") as f:
    for l in [x.strip() for x in f.readlines()]:
        x = 0
        for loc in l:
            layout[(x, layout_height)] = loc
            x+= 1
        layout_height += 1
        layout_width = len(l)

def print_layout(layout):
    x = 0
    y = 0
    for y in range(layout_height):
        out = ""
        for x in range(layout_width):
            out += layout[(x,y)]
        print(out)
            
#return number of occupied (#) neighbors adjacent to x,y (U, D, L, R + diagonals)
def get_nei_count(layout, x, y):
    count = 0
    modifiers = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for xx, yy in modifiers:
        if layout[(x + xx, y + yy)] == "#":
          count += 1
    return count

def get_vis_nei_count(layout, x, y):
    count = 0
    modifiers = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]
    for xmod, ymod in modifiers:
        xx = x
        yy = y
        while xx >= 0 and xx < layout_width and yy >= 0 and yy < layout_height:
            xx += xmod
            yy += ymod
            if layout[(xx, yy)] == "#":
                count += 1
                break
            elif layout[(xx, yy)] == "L":
                break
    return count

def apply_rule(layout, occupied_rule, tolerance):
    changed = False
    new_layout = defaultdict(lambda: ".")
    for y in range(layout_height):
        for x in range(layout_width):
            if layout[(x,y)] == "L" and occupied_rule(layout, x, y) == 0:
                new_layout[(x,y)] = "#"
            elif layout[(x,y)] == "#" and occupied_rule(layout, x, y) >= tolerance:
                new_layout[(x,y)] = "L"
            else:
                new_layout[(x,y)] = layout[(x,y)]
            if new_layout[(x,y)] != layout[(x,y)]:
                changed = True
    return (new_layout, changed)

def part1():
    layout1 = layout.copy()
    while True:
        layout2, changed = apply_rule(layout1, get_nei_count, 4)
        if not changed:
            break
        layout1 = layout2
    return sum([x == "#" for x in layout1.values()])

def part2():
    layout1 = layout.copy()
    while True:
        layout2, changed = apply_rule(layout1, get_vis_nei_count, 5)
        if not changed:
            break
        layout1 = layout2
    return sum([x == "#" for x in layout1.values()])


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())

