import contextlib

import aoc_helper

input = aoc_helper.get_input(2024, 4)

total = 0

input = [list(line) for line in input.splitlines()]

for i in input:
    print(i)

for i in range(len(input)):
    for j in range(len(input[i])):
        across, down, diagonal_right, diagonal_left = [], [], [], []

        with contextlib.suppress(IndexError):
            across = input[i][j : j + 4]
            down = [input[k][j] for k in range(i, i + 4)]
            diagonal_left = (
                [input[k][j - k + i] for k in range(i, i + 4)] if j >= 3 else []
            )
            diagonal_right = [input[k][j + k - i] for k in range(i, i + 4)]

        total += sum(
            1
            for i in (across, down, diagonal_right, diagonal_left)
            if "".join(i) in ["XMAS", "SAMX"]
        )

print(total)
