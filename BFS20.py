from collections import deque

def bfs_path(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    
    # Dictionary to store the parent of each cell
    parent = {start: None}

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct path from end to start
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Reverse to get path from start to end

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_cell[0] < len(maze) and
                0 <= next_cell[1] < len(maze[0]) and
                maze[next_cell[0]][next_cell[1]] != '#' and
                next_cell not in visited):
                
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    return None  # No path found

# Example maze
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

path = bfs_path(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path exists.")
    
    
#Output
#s@23:~$ python3 BFS20.py
#Path found: [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)]

