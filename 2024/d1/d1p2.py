import os
from collections import Counter
file_path = os.path.join(os.path.dirname(__file__), "d1.txt")

left_nums, right_nums = [], []
similarity = 0

with open(file_path, "r") as file:
    for line in file:
        left, right = line.split('   ')
        left_nums.append(int(left))
        right_nums.append(int(right))

left_count = Counter(left_nums)
similarity = sum(num * left_count[num] for num in right_nums)

print(similarity)
