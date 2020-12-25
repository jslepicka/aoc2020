public_keys = []

with open("25.txt") as f:
    public_keys = [int(x.strip()) for x in f.readlines()]

def part1():
    #https://en.wikipedia.org/wiki/Modular_exponentiation
    #We only need one loop value, so it really doesn't matter which public key
    #we use for this first step.  The second one completes faster, so that's
    #the one we'll use.
    mod = 20201227
    n = 1
    while True:
        if pow(7, n, mod) == public_keys[1]:            
            break
        n += 1
    #now use the loop val with the other public key to get the encryption key
    return pow(public_keys[0], n, mod)

def part1a():
    #forego the modular exponentiation stuff
    mod = 20201227
    n = 0
    x = 1
    while x != public_keys[1]:
        x = (x * 7) % mod
        n += 1
    #now use the loop val with the other public key to get the encryption key
    return pow(public_keys[0], n, mod)

print("Part 1: %d" % part1())
print("Part 1: %d" % part1a())
