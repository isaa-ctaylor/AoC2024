import re

import aoc_helper

input = aoc_helper.get_input(2024, 3)

input = input.replace("\n", "")

mul = re.findall(r"(mul)\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", input)

do_mul = True
total = 0

for i in mul:
    if i[0] == "mul":
        if do_mul:
            total += int(i[1]) * int(i[2])
    elif i[3] == "do":
        do_mul = True
    elif i[4] == "don't":
        do_mul = False

print(total)
