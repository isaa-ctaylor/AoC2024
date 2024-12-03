import re

import aoc_helper

input = aoc_helper.get_input(2024, 2)

total = 0


def is_safe(nums: list[int]):
    differences = [int(nums[i]) - int(nums[i - 1]) for i in range(1, len(nums))]
    if any((i == 0) or (abs(i) > 3) for i in differences):
        return False
    return True


def is_in_order(nums: list[int]):
    return sorted(nums) == nums or sorted(nums, reverse=True) == nums


def check(nums: list[int], *, depth: int = 0):
    if is_safe(nums) and is_in_order(nums):
        return True

    if depth == 0:
        for i in range(len(nums)):
            altered = nums.copy()
            del altered[i]
            if check(altered, depth=1):
                return True

    return False


for line in input.splitlines():
    nums = [int(i) for i in re.findall(r"(\d+)", line)]

    if check(nums):
        total += 1

print(total)
