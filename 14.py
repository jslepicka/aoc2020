input = []

with open("14.txt") as f:
    input = [x.strip() for x in f.readlines()]

def mask_val(val, mask):
    for bit, m in enumerate(reversed(mask)):
        if m == "0":
            val &= ~(1 << bit)
        elif m == "1":
            val |= (1 << bit)
    return val

def part1():
    mem = {}
    mask = ""
    for i in input:
        command, _, val = i.split(" ")
        if command == "mask":
            mask = val
        elif "mem" in command:
            address = int(command.split("[")[1].split("]")[0])
            val = int(val)
            val = mask_val(val, mask)
            mem[address] = val
    
    return sum(mem.values())

def part2():
    mem = {}
    mask = ""
    address_mask = 0
    mask_bits = 0
    for i in input:
        command, _, val = i.split(" ")
        if command == "mask":
            mask = val
            mask_bits = mask.count("X")
            address_mask = 0
        elif "mem" in command:
            address = int(command.split("[")[1].split("]")[0])
            val = int(val)
            for _ in range(2**mask_bits):
                new_address = address
                am = address_mask
                for bit, v in enumerate(reversed(mask)):
                    if v == "X":
                        if (am & 1):
                            new_address |= ((am & 1) << bit)
                        else:
                            new_address &= ~(1 << bit)
                        am >>= 1
                    elif v == "1":
                        new_address |= (1 << bit)
                mem[new_address] = val
                address_mask += 1
    return sum(mem.values())

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())