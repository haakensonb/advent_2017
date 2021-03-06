# maze = [0, 3, 0, 1, -3]
with open('./day_5/input.txt') as f:
    maze = f.readlines()
f.close
maze = [int(line.strip()) for line in maze]

# I think I will just expand on the original functions
# from now on rather than separating part one from two
def escape_maze(maze):
    end = len(maze) - 1
    step_counter = 0
    offset = 0

    while True:
        cur_index = offset
        offset = offset + maze[cur_index]
        if maze[cur_index] >= 3:
            maze[cur_index] = maze[cur_index] - 1
        else:
            maze[cur_index] = maze[cur_index] + 1
        step_counter += 1
        if offset > end:
            return step_counter


print(escape_maze(maze))