import os
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

num_safe = 0


def is_safe(level):
    n = len(level)

    if n < 2:
        return True

    increasing = level[0] < level[1]

    for i in range(n - 1):
        diff = level[i + 1] - \
            level[i] if increasing else level[i] - level[i + 1]
        if not (1 <= diff <= 3):
            return False
    return True


with open(file_path, "r") as file:
    for line in file:
        level = list(map(int, line.strip().split()))

        if is_safe(level):
            num_safe += 1
            continue

        for i in range(len(level)):
            if is_safe(level[:i] + level[i + 1:]):
                num_safe += 1
                break

print(num_safe)
