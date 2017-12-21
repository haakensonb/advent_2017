import math

def spiral_mem_1(access_port, target_num):

    grid = {'1':(0,0)}
    num = 2
    multiplier = 1
    index, x, y = 0, 0, 0
    # Right, Up, Left, Down
    directions = 'RULD'

    while num < target_num:
        if directions[index] == 'R':
            for _ in range(multiplier):
                x += 1
                # There has to be a more DRY way to write this
                key = str(num)
                grid[key] = (x, y)
                num += 1
        if directions[index] == 'U':
            for _ in range(multiplier):
                y += 1
                key = str(num)
                grid[key] = (x, y)
                num += 1
        if directions[index] == 'L':
            for _ in range(multiplier):
                x -= 1
                key = str(num)
                grid[key] = (x, y)
                num += 1
        if directions[index] == 'D':
            for _ in range(multiplier):
                y -= 1
                key = str(num)
                grid[key] = (x, y)
                num += 1

        if directions[index] == 'U' or directions[index] == 'D':
            multiplier += 1

        index = (index + 1) % 4
    access_string = str(access_port)
    target_string = str(target_num)
    p1 = grid[access_string][0]
    p2 = grid[access_string][1]

    q1 = grid[target_string][0]
    q2 = grid[target_string][1]

    return math.fabs(p1-q1) + math.fabs(p2-q2)

print(spiral_mem_1(1, 361527))