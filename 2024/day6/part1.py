import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

grid = []
guard_pos = None
direction_idx = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left

with open(file_path, "r") as file:
    for x, line in enumerate(file):
        row = []
        for y, char in enumerate(line):
            if char == "^":
                guard_pos = (x, y)
            row.append(char)
        grid.append(row)
        
        
def move_guard(pos, direction_idx):
    visited = set()
    x, y = pos
    
    while True:
        visited.add((x, y))
        dx, dy = directions[direction_idx]
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])):
            break

        if grid[new_x][new_y] != '#':
            x, y = new_x, new_y
        else:
            direction_idx = (direction_idx + 1) % 4 
            
    return visited

        
print(len(move_guard(guard_pos, direction_idx)))
