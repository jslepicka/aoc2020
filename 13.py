timestamp = 0
ids = []

with open("13.txt") as f:
    timestamp = int(f.readline())
    ids = f.readline().split(",")

print(timestamp)
print(ids)

def part1():
    shortest_wait = 999
    shortest_wait_id = 0
    for i in [int(x) for x in ids if x != "x"]:
        wait = i - (timestamp % i)
        if wait < shortest_wait:
            shortest_wait = wait
            shortest_wait_id = i

    return shortest_wait * shortest_wait_id

"""
Had to google for answers on part 12.  I don't fully understand the Chinese Remainder Theroem, but here's my
undertanding of how it's used to solve this.

All bus numbers are prime

time     bus 7   bus 13  bus 59  bus 31  bus 19
1068773    .       .       .       .       .
1068774    D       .       .       .       .
1068775    .       .       .       .       .
1068776    .       .       .       .       .
1068777    .       .       .       .       .
1068778    .       .       .       .       .
1068779    .       .       .       .       .
1068780    .       .       .       .       .
1068781    D       .       .       .       .
1068782    .       D       .       .       .
1068783    .       .       .       .       .
1068784    .       .       .       .       .
1068785    .       .       D       .       .
1068786    .       .       .       .       .
1068787    .       .       .       D       .
1068788    D       .       .       .       D
1068789    .       .       .       .       .
1068790    .       .       .       .       .
1068791    .       .       .       .       .
1068792    .       .       .       .       .
1068793    .       .       .       .       .
1068794    .       .       .       .       .
1068795    D       D       .       .       .
1068796    .       .       .       .       .
1068797    .       .       .       .       .

At t=1068781:
t % 7 = 0
t % 13 = 12 (13 - delay of 1)
t % 59 = 55 (59 - delay of 4)
t % 31 = 25 (31 - delay of 6)
t % 19 = 12 (31 - delay of 7)

- Increment time by 7 until we find a time where t % 13 == 12
- Now 7 and 13 meet the criteria at this timestamp.  This will happen again at LCM(7, 13) = 91 intervals; the next
  occurence is at timestamp + 91.  So for the next search we can increment by 91.
- Check if t % 59 == 55.  If not, increment by 91.
- When we find a match, we can now increment by the LCM(91, 59) = 5369
- Repeat until all busses are in the right position

This is the Chinese Remainder Theorem search by sieving method.

Note: for the LCM operations, the numbers are coprime (which is a requirement for the CRT to work), so this
      can be done by simply multiplying them together.

"""

def part2():
    time = 0
    step = 1
    periods = [int(x) for x in ids if x != "x"]
    remainders = [-i % int(v) for i, v in enumerate(ids) if v != "x"]

    print(periods)
    print(remainders)

    for period, remainder in zip(periods, remainders):
        while time % period != remainder:
            time += step
        step *= period
        print("time: %d step: %d" % (time, step))
    return time

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
