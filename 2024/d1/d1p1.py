import os
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

left_nums, right_nums = [], []

with open(file_path, "r") as file:
    for line in file:
        left, right = line.split('   ')
        left_nums.append(int(left))
        right_nums.append(int(right))

zipped_nums = zip(sorted(left_nums), sorted(right_nums))
print(sum([abs(left - right) for left, right in zipped_nums]))
