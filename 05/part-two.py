import aoc_helper

input = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

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

    changed = False

    for index, i in enumerate(ints):
        if i in ruleset:
            for j in ruleset[i]:
                if j in ints:
                    if j not in ints[:index]:
                        ints.remove(j)
                        ints.insert(index, j)
                        changed = True

    if changed:
        total += ints[len(ints) // 2]

print(total)
