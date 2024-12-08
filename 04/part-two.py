import contextlib

import aoc_helper

input = aoc_helper.get_input(2024, 4)

total = 0

input = [list(line) for line in input.splitlines()]

for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] != "A" or j < 1 or i < 1:
            continue

        diagonal_right, diagonal_left = [], []

        with contextlib.suppress(IndexError):
            diagonal_left = [input[i + k][j - k] for k in range(-1, 2)]
            diagonal_right = [input[i + k][j + k] for k in range(-1, 2)]

        total += (
            1
            if all(
                "".join(i) in ["MAS", "SAM"] for i in (diagonal_right, diagonal_left)
            )
            else 0
        )

print(total)
