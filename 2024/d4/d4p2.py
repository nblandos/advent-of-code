import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

word = "MAS"
grid = []
word_count = 0
DOWN_RIGHT = (1, 1)
DOWN_LEFT = (1, -1)


def check_diagonal(x, y, dx, dy, word):
    sequence = ""
    for k in range(len(word)):
        new_x = x + k * dx
        new_y = y + k * dy
        if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[new_x]):
            return False
        sequence += grid[new_x][new_y]
    return sequence == word


with open(file_path, "r") as file:
    for line in file:
        grid.append(line.strip())

for x in range(len(grid)):
    for y in range(len(grid[x])):
        forward_diagonal = (check_diagonal(x, y, *DOWN_RIGHT, word) or
                            check_diagonal(x, y, *DOWN_RIGHT, word[::-1]))
        backward_diagonal = (check_diagonal(x, y + len(word) - 1, *DOWN_LEFT, word) or
                             check_diagonal(x, y + len(word) - 1, *DOWN_LEFT, word[::-1]))
        
        if forward_diagonal and backward_diagonal:
            word_count += 1

print(word_count)
