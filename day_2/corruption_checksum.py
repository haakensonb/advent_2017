def format_input():
    with open('./day_2/input.txt') as f:
        spreadsheet = f.read().strip().splitlines()
    f.closed
    return [[int(x) for x in row.split()] for row in spreadsheet]

def checksum(spreadsheet):
    sum = 0
    for row in spreadsheet:
        sum += max(row) - min(row)
    return sum

spreadsheet = format_input()
print(checksum(spreadsheet))