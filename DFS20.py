def dfs_path_visual(maze, start, end):
    stack = [start]
    visited = set()
    parent = {start: None}

    while stack:
        position = stack.pop()
        x, y = position

        if position == end:
            # Reconstruct the path
            path = []
            while position:
                path.append(position)
                position = parent[position]
            path = path[::-1]  # start -> end

            # Visualize the path on the maze
            maze_visual = [row[:] for row in maze]  # Copy maze
            for px, py in path:
                if maze_visual[px][py] != 0:  # Keep start/end as is
                    continue
                maze_visual[px][py] = '*'  # Mark path

            return path, maze_visual

        visited.add(position)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            new_pos = (new_x, new_y)

            if (0 <= new_x < len(maze) and
                0 <= new_y < len(maze[0]) and
                maze[new_x][new_y] == 0 and
                new_pos not in visited):
                
                stack.append(new_pos)
                parent[new_pos] = position

    return None, None  # No path found


# Example maze
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path, maze_visual = dfs_path_visual(maze, start, end)

if path:
    print("Path found:", path)
    print("Maze with path:")
    for row in maze_visual:
        print(' '.join(str(cell) for cell in row))
else:
    print("No path exists.")


#Output
#s@23:~$ python3 DFS20.py
#Path found: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]
#Maze with path:
#* 1 * * *
#* 1 * 1 *
#* * * 1 *
#1 1 1 1 *
#0 0 0 0 *

