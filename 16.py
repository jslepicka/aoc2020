import re

fields = {}
tickets = [] #tickets[0] is my ticket
valid_tickets = []

section = None
with open("16.txt") as f:
    for l in [x.strip() for x in f.readlines()]:
        if l == "":
            continue
        elif l == "your ticket:":
            section = "my_ticket"
            continue
        elif l == "nearby tickets:":
            section = "nearby_tickets"
            continue
        elif section is None: #restrictions
            m = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', l)
            if m:
                field = m.group(1)
                fields[field] = {}
                fields[field]["ranges"] = [(int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))]
        else:
            tickets.append([int(x) for x in l.split(",")])

def part1():
    #get a list of tuples of valid ranges
    res = []
    for field in fields:
        for r in fields[field]["ranges"]:
            res.append(r)
    #sort the list by the first value in the tuple
    sorted_res = sorted(res, key=lambda x: x[0])
    #merge the ranges
    res = []
    for r in sorted_res:
        if len(res) > 0:
            if r[0] <= res[-1][1]:
                if r[1] > res[-1][1]:
                    res[-1]= (res[-1][0], r[1])
            else:
                res.append(r)
        else:
            res.append(r)
    
    #put all valid numbers in a list
    search_list = []
    for r in res:
        for l in list(range(r[0], r[1] + 1)):
            search_list.append(l)

    #create a list of invalid numbers (numbers that are not in search_list)
    invalid = []
    for t in tickets[1:]:
        valid = True
        for f in t:
            if f not in search_list:
                valid = False
                invalid.append(f)
        if valid:
            valid_tickets.append(t)

    return sum(invalid)

def part2():
    num_fields = len(fields.keys())
    print("There are %d fields" % num_fields)
    #initialize of list of possible indices for every field
    for field in fields:
        fields[field]["possible"] = [x for x in range(0, num_fields)]
    #Go through each ticket's numbers and check them against each range.
    #If a range prohibits the value, remove the number's index from the list
    #of possibilities.
    for t in valid_tickets:
        for i, val in enumerate(t):
            for field in fields:
                valid = False
                for r in fields[field]["ranges"]:
                    if val >= r[0] and val <= r[1]:
                        valid = True
                        break
                if not valid:
                    fields[field]["possible"].remove(i)
    
    #Search through the fields, ordered by number of possible indices.
    #When we find an available index, set that as the field's index and add it to the list
    #of found indices.  Multiply ans by our ticket's number in that index if the field
    #starts with "departure".
    ans = 1
    found = []
    for r in sorted(fields.items(), key=lambda k_v: len(k_v[1]["possible"])):
        field = r[0]
        possible = r[1]['possible']
        print(field, possible)
        for p in possible:
            if p not in found:
                found.append(p)
                fields[field]["index"] = p
                if "departure" in field:
                    ans *= tickets[0][p]
                break
    for r in sorted(fields.items(), key=lambda k_v: k_v[1]["index"]):
        print("%d: %s" % (r[1]["index"], r[0]))
    return ans


print("Part 1: %d" % part1())
print("Part 2: %d" % part2())
