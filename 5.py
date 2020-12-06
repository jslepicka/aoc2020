input = []
with open("5.txt") as f:
    input = [x.strip() for x in f.readlines()]

def decode(pass_number):
    if len(pass_number) != 10:
        return None
    row = 0
    col = 0
    row_range = 128
    col_range = 8
    for x in pass_number[:7]:
        row_range >>= 1
        if x == 'B':
            row += row_range
    for x in pass_number[-3:]:
        col_range >>= 1
        if x == 'R':
            col += col_range
    return (row, col)

def part1():
    max_id = 0
    for i in input:
        r,c = decode(i)
        seat_id = r * 8 + c
        if seat_id > max_id:
            max_id = seat_id
    return max_id

def part2():
    assignments = [decode(i) for i in input]
    seat_ids = sorted([r * 8 + c for r,c in assignments])
    start = seat_ids[0]
    end = seat_ids[-1]
    #set supports difference operation, so create a set and
    #diff with the seat list
    s = set(range(start, end+1))
    missing_seats = sorted(s.difference(seat_ids))
    missing_seat = missing_seats[0]
    return missing_seat

print("Part 1 highest seat id: %d" % part1())
print("Part 2 missing seat: %d" % part2())