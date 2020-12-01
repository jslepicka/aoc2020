input = []
with open("1.txt") as file:
    input = [int(x.strip()) for x in file.readlines()]

def part1():
    print("Part 1")
    a = sorted(input)
    b = a.copy()

    while True:
        sum = [a[i] + b[i] for i in range(len(a))]
        if 2020 in sum:
            i = sum.index(2020)
            a_val = a[i]
            b_val = b[i]
            print("%d + %d = 2020" % (a_val, b_val))
            print("%d * %d = %d" % (a_val, b_val, a_val * b_val))
            return
        a.pop(0)
        b.pop(-1)

def part2():
    print("Part 2")
    a = sorted(input)
    b = a.copy()
    c = a.copy()
    a_len = len(a)
    r = range(0, a_len)

    rotate_b = 0
    rotate_c = 0
    while True:
        bb = b[rotate_b:] + b[:rotate_b]
        cc = c[rotate_c:] + c[:rotate_c]
        sum = [a[i] + bb[i] + cc[i] for i in r]
        if 2020 in sum:
            i = sum.index(2020)
            a_val = a[i]
            b_val = bb[i]
            c_val = cc[i]
            print("%d + %d + %d = 2020" % (a_val, b_val, c_val))
            print("%d * %d * %d = %d" % (a_val, b_val, c_val, a_val * b_val * c_val))
            return
        else:
            rotate_c += 1
            if rotate_c == a_len:
                rotate_c = 0
                rotate_b += 1

part1()
part2()