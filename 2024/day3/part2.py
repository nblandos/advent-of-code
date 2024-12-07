import os
import re
file_path = os.path.join(os.path.dirname(__file__), "input.txt")

res = 0
enabled = True
pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

with open(file_path, "r") as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            if match == "do()":
                enabled = True
            elif match == "don't()":
                enabled = False
            else:
                if enabled:
                    a, b = re.findall(r"\d{1,3}", match)
                    res += int(a) * int(b)

print(res)
