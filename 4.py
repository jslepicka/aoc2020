import re
input = {}

record = 0
input[0] = {}
with open("4.txt") as f:
    for l in [x.strip() for x in f.readlines()]:
        if l == "":
            record += 1
            input[record] = {}
        else:
            for i in l.split(" "):
                j = i.split(":")
                input[record][j[0]] = j[1]

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

def part1():
    valid_count = 0
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for record in input:
        valid = True
        for rf in required_fields:
            if rf not in input[record]:
                valid = False
                break
        if valid:
            valid_count += 1
    return valid_count
        

"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def rule_byr(x):
    x = int(x)
    return x >= 1920 and x <= 2002
def rule_iyr(x):
    x = int(x)
    return x >= 2010 and x <= 2020
def rule_eyr(x):
    x = int(x)
    return x >= 2020 and x <= 2030
def rule_hgt(x):
    m = re.match(r'^(\d+)((cm|in))$', x)
    if m:
        val = int(m[1])
        unit = m[2]
        if unit == "in":
            if val >= 59 and val <= 76:
                return True
        elif unit == "cm":
            if val >= 150 and val <= 193:
                return True
    return False
def rule_hcl(x):
    m = re.match(r'^#[0-9a-f]{6}$', x)
    if m:
        return True
    return False
def rule_ecl(x):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if x in valid_colors:
        return True
    return False
def rule_pid(x):
    m = re.match(r'^\d{9}$', x)
    if m:
        return True
    return False

def part2():
    rules = {
        "byr": rule_byr,
        "iyr": rule_iyr,
        "eyr": rule_eyr,
        "hgt": rule_hgt,
        "hcl": rule_hcl,
        "ecl": rule_ecl,
        "pid": rule_pid,
    }
    valid_count = 0
    for record in input:
        valid = True
        for rule in rules:
            if rule not in input[record]:
                valid = False
                break
            if rules[rule](input[record][rule]) == False:
                valid = False
                break
        if valid:
            valid_count += 1
    return valid_count


print("Part 1 valid passports: %d" % part1())
print("Part 2 valid passports: %d" % part2())