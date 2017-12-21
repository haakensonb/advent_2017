import math

def spiral_mem_1(access_port, target_num):
    grid = [[1, (0,0)]]
    counter = 2
    index, x, y = 0, 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    multiplier = 1

    while counter < target_num:
        for _ in range(multiplier):
            x += dx[index]
            y += dy[index]
            grid.append([counter, (x, y)])
            counter += 1

        if dy[index] == 1 or dy[index] == -1:
            multiplier += 1

        index = (index + 1) % 4
    
    q1, q2, p1, p2 = 0, 0, 0, 0
    for pair in grid:
        if pair[0] == access_port:
            p1 = pair[1][0]
            p2 = pair[1][1]
        if pair[0] == target_num:
            q1 = pair[1][0]
            q2 = pair[1][1]

    # Formula for Manhattan Distance
    return math.fabs(p1-q1) + math.fabs(p2-q2)

print(spiral_mem_1(1, 361527))

def check_adjacent(grid, current_square):
    adjacent_values = []
    x = current_square[0]
    y = current_square[1]
    # Coordinates for all adjacent squares
    ax = [1, 1, 0, -1, -1, -1, 0, 1]
    ay = [0, 1, 1, 1, 0, -1, -1, -1]

    for pair in grid:
        for i in range(len(ax)):
            temp = (x + ax[i], y + ay[i])
            if pair[1] == temp:
                adjacent_values.append(pair[0])

    return adjacent_values

def spiral_mem_2(target_num):
    grid = [[1, (0,0)]]
    counter = 2
    index, x, y = 0, 0, 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    square_val = 0
    multiplier = 1

    while True:
        for _ in range(multiplier):
            x += dx[index]
            y += dy[index]
            square_val = sum(check_adjacent(grid, (x, y)))
            grid.append([square_val, (x, y)])

            if square_val > target_num:
                return square_val

            counter += 1

        if dy[index] == 1 or dy[index] == -1:
            multiplier += 1

        index = (index + 1) % 4

print(spiral_mem_2(361527))