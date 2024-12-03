import re

import aoc_helper

input = aoc_helper.get_input(2024, 2)

total = 0

for line in input.splitlines():
    nums = [int(i) for i in re.findall(r"(\d+)", line)]

    if sorted(nums) == nums or sorted(nums, reverse=True) == nums:
        differences = [int(nums[i]) - int(nums[i - 1]) for i in range(1, len(nums))]
        if any((i == 0) or (abs(i) > 3) for i in differences):
            continue
        total += 1

print(total)
