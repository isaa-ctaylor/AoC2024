from turtle import update

import aoc_helper

input = aoc_helper.get_input(2024, 5)

rules, updates = input.split("\n\n")

ruleset: dict[int, list[int]] = {}

for i in rules.splitlines():
    before, after = [int(i) for i in i.split("|")]

    if after not in ruleset:
        ruleset[after] = []

    ruleset[after].append(int(before))

total = 0

for u in updates.splitlines():
    ints = [int(i) for i in u.split(",")]

    for index, i in enumerate(ints):
        if i in ruleset:
            for j in ruleset[i]:
                if j in ints:
                    if j not in ints[:index]:
                        break
            else:
                continue
            break
    else:
        total += ints[len(ints) // 2]

print(total)
