from math import ceil, sqrt
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

def bsgs(g, a, p):
    # To solve g^e mod p = a and find e
    m = ceil(sqrt(p-1))
    # Baby Step
    lookup_table = {pow(g, i, p): i for i in range(m)}
    # Giant Step Precomputation c = g^(-m) mod p
    c = pow(g, m*(p-2), p)
    # Giant Step
    for j in range(m):
        x = (a*pow(c, j, p)) % p
        if x in lookup_table:
            return j*m + lookup_table[x]
    return None

def part1b():
    #discrete logarithm problem.  solve using the baby step giant step algorithm.
    #https://masterpessimistaa.wordpress.com/2018/01/14/dlp-and-baby-step-giant-step-algorithm/
    mod = 20201227
    n = bsgs(7, public_keys[0], mod)
    return pow(public_keys[1], n, mod)

print("Part 1: %d" % part1())
print("Part 1a: %d" % part1a())
print("Part 1b: %d" % part1b())
