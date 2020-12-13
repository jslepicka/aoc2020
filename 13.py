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
all bus numbers are prime

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
t % 13 = 12 (13 - delay of 1)
t % 59 = 55 (59 - delay of 4)
t % 31 = 25 (31 - delay of 6)
t % 19 = 12 (31 - delay of 7)

"""

def part2():
    #Couldn't figure this out and had to google for solutions.
    #This is some kind of implementation of the chinese remainder theorem, but I don't really understand it.
    time = 0
    step = 1
    periods = [int(x) for x in ids if x != "x"]
    remainders = [-i%int(v) for i, v in enumerate(ids) if v != "x"]

    print(periods)
    print(remainders)

    for period, remainder in zip(periods, remainders):
        #if time % period does not equal remainder, this isn't a possible time for the period
        while time % period != remainder:
            time += step

        #Satisfying all previous conditions can only happen at LCMs of the previous steps.
        #This is the LCM of step and the period.  This may only work if they are coprime?
        #factors of the new step are equal to all previous periods multiplied by each other
        #e.g.:
        # step starts at 1
        # 7 meets criteria, step changes to 7
        # 13 meets criteria at time 77, step changes to 7 x 13 = 91
        # 59 meets criteria at time 350, step changes to 91 x 59 = 5369
        # 31 meets criteria at time 70147, step changes to 5369 x 31 = 166439
        # 19 meets criteria at time 1068781 = 7 x 13 x 59 x 31
        step *= period
        print("time: %d step: %d" % (time, step))
    return time

print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
