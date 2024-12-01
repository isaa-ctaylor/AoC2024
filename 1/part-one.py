import re

import aoc_helper

matches = re.findall(r"((\d+) +(\d+))", aoc_helper.get_input(2024, 1))

nums = [], []

for match in matches:
    nums[0].append(int(match[1]))
    nums[1].append(int(match[2]))

nums = sorted(nums[0]), sorted(nums[1])

total = 0

for i in range(len(nums[0])):
    total += abs(nums[0][i] - nums[1][i])

print(total)
