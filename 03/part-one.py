import re

import aoc_helper

input = aoc_helper.get_input(2024, 3)

input = input.replace("\n", "")

mul = re.findall(r"mul\((\d+),(\d+)\)", input)

total = sum(int(i[0]) * int(i[1]) for i in mul)

print(total)
