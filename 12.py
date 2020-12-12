input = []
with open("12.txt") as f:
    input = [x.strip() for x in f.readlines()]

class ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 90
    
    def move(self, action, value):
        if action == "N":
            self.y -= value
        elif action == "S":
            self.y += value
        elif action == "E":
            self.x += value
        elif action == "W":
            self.x -= value
        elif action == "L":
            self.dir = (self.dir - value) % 360
        elif action == "R":
            self.dir = (self.dir + value) % 360
        elif action == "F":
            if self.dir == 0:
                self.move("N", value)
            elif self.dir == 90:
                self.move("E", value)
            elif self.dir == 180:
                self.move("S", value)
            elif self.dir == 270:
                self.move("W", value)

class ship2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wp_x = 10
        self.wp_y = -1

    def rotate_wp(self, angle):
        #translate relative to 0,0
        x = self.wp_x - self.x
        y = self.wp_y - self.y
        #genaralize to 90 degree clockwise rotations
        while angle > 0:
            #rotate around 0,0
            x, y = -y, x
            angle -= 90
        #translate back to ship coordinate origin
        self.wp_x = x + self.x
        self.wp_y = y + self.y
    
    def move(self, action, value):
        if action == "N":
            self.wp_y -= value
        elif action == "S":
            self.wp_y += value
        elif action == "E":
            self.wp_x += value
        elif action == "W":
            self.wp_x -= value
        elif action == "L":
            self.rotate_wp(360 - value)
        elif action == "R":
            self.rotate_wp(value)
        elif action == "F":
            #move to waypoint
            diff_x = self.wp_x - self.x
            diff_y = self.wp_y - self.y

            for _ in range(value):
                self.x = self.wp_x
                self.y = self.wp_y
                self.wp_x += diff_x
                self.wp_y += diff_y

def part1():
    s = ship()
    for ins in input:
        action = ins[:1]
        value = int(ins[1:])
        s.move(action, value)
    md = abs(s.x) + abs(s.y)
    return md

def part2():
    s = ship2()
    for ins in input:
        action = ins[:1]
        value = int(ins[1:])
        s.move(action, value)
    md = abs(s.x) + abs(s.y)
    return md

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
