"""
Kind of a messy solution. Hopefully I will be able
to come back to this later and reduce the amount of lines needed
"""
import itertools

def format_input():
    with open('./day_2/input.txt') as f:
        spreadsheet = f.read().strip().splitlines()
    f.closed
    return [[int(x) for x in row.split()] for row in spreadsheet]

def checksum_1(spreadsheet):
    sum = 0
    for row in spreadsheet:
        sum += max(row) - min(row)
    return sum

spreadsheet = format_input()
print(checksum_1(spreadsheet))

def checksum_2(spreadsheet):
    sum = 0
    possibilities = [[itertools.combinations(row, 2)] for row in spreadsheet]
    for rows in possibilities:
        for pairs in rows:
            for pair in pairs:
                if max(pair) % min(pair) == 0:
                    sum += max(pair) / min(pair)
    return sum

print(checksum_2(spreadsheet))
