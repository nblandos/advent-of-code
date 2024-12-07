import os
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

num_safe = 0

with open(file_path, "r") as file:
    for line in file:
        level = list(map(int, line.strip().split()))

        n = len(level)

        if n < 2:
            num_safe += 1
            continue

        increasing = level[0] < level[1]
        is_safe = True

        for i in range(n - 1):
            diff = level[i + 1] - \
                level[i] if increasing else level[i] - level[i + 1]
            if not (1 <= diff <= 3):
                is_safe = False
                break

        if is_safe:
            num_safe += 1

print(num_safe)
