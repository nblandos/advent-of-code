import os
from collections import defaultdict
from itertools import product

file_path = os.path.join(os.path.dirname(__file__), "input.txt")

operators = ['+', '*', '||']
total_calibration_res = 0
possible = defaultdict(list)


def check_valid(key, values):
    for ops in product(operators, repeat=len(values)-1):
        result = values[0]
        for i, op in enumerate(ops):
            next_val = values[i+1]
            if op == '+':
                result += next_val
            elif op == '*':
                result *= next_val
            elif op == '|':
                result = int(str(result) + str(next_val))
        if result == key:
            return True
    return False
                    
    
with open(file_path, "r") as file:
    for line in file:
        key, values = line.strip().split(":")
        key = int(key)
        values = list(map(int, values.strip().split()))

        if check_valid(key, values):
            total_calibration_res += key

        
print(total_calibration_res)
