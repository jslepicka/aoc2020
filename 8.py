class machine:
    STATE_NONE = 0
    STATE_TERMINATED = 1
    def __init__(self, program = None, debug = False):
        self.program = program.copy()
        self.debug = debug
        self.reset()
        self.program_len = len(program)

    def reset(self):
        self.pc = 0
        self.a = 0
    def decode(self, pc):
        op, arg = self.program[pc].split(" ")
        arg = int(arg)
        return op, arg
    def run(self, single_step = False):
        while True:
            op, arg = self.decode(self.pc)
            if self.debug:
                print("%d: %s %d a=%d" % (self.pc, op, arg, self.a))
            if op == "acc":
                self.a += arg
                self.pc += 1
            elif op == "jmp":
                self.pc += arg
            elif op == "nop":
                self.pc += 1
            if self.pc == self.program_len:
                return self.STATE_TERMINATED
            elif single_step:
                return self.STATE_NONE


input = []
with open("8.txt") as f:
   input = [x.strip() for x in f.readlines()]


def part1():
    visited = {}
    m = machine(input, debug=False)
    while True:
        if m.pc in visited:
            return m.a
        visited[m.pc] = 1
        m.run(True)


def part2():
    patches = [(i, val.replace("nop", "jmp")) for i,val in enumerate(input) if val.startswith("nop")]
    patches += [(i, val.replace("jmp", "nop")) for i,val in enumerate(input) if val.startswith("jmp")]
 
    for patch in patches:
        visited = {}
        m = machine(input, debug=False)
        m.program[patch[0]] = patch[1]
        while True:
            if m.pc in visited:
                break
            visited[m.pc] = 1
            if m.run(True) == machine.STATE_TERMINATED:
                return m.a

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())