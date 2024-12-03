import os
import re
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

res = 0

pattern = r"mul\(\d{1,3},\d{1,3}\)"

with open(file_path, "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            a, b = re.findall(r"\d{1,3}", match)
            res += int(a) * int(b)

print(res)
