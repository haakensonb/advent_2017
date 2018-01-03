# maze = [0, 3, 0, 1, -3]
with open('./day_5/input.txt') as f:
    maze = f.readlines()
f.close
maze = [int(line.strip()) for line in maze]

def escape_maze(maze):
    end = len(maze) - 1
    step_counter = 0
    offset = 0

    while True:
        cur_index = offset
        offset = offset + maze[cur_index]
        maze[cur_index] = maze[cur_index] + 1
        step_counter += 1
        if offset > end:
            return step_counter

print(escape_maze(maze))