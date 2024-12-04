import os

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

word = "XMAS"
grid = []
word_count = 0
directions = [(0, 1), (1, 0), (1, 1), (1, -1)]


def check_word(x, y, dx, dy, word):
    sequence = ""
    for k in range(len(word)):
        new_x = x + k * dx
        new_y = y + k * dy
        if new_x < 0 or new_x >= len(grid) or new_y < 0 or new_y >= len(grid[new_x]):
            return 0
        sequence += grid[new_x][new_y]
    return 1 if sequence == word else 0


with open(file_path, "r") as file:
    for line in file:
        grid.append(line.strip())

for x in range(len(grid)):
    for y in range(len(grid[x])):
        for dx, dy in directions:
            word_count += check_word(x, y, dx, dy, word)
            word_count += check_word(x, y, dx, dy, word[::-1])

print(word_count)
