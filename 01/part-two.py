import collections
import re

import aoc_helper

matches = re.findall(r"((\d+) +(\d+))", aoc_helper.get_input(2024, 1))

nums = [], []

for match in matches:
    nums[0].append(int(match[1]))
    nums[1].append(int(match[2]))

nums = sorted(nums[0]), sorted(nums[1])

total = 0

count = collections.Counter(nums[1])
for i in nums[0]:
    total += i * count[i]

print(total)
