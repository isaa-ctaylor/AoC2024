import aoc_helper

input = aoc_helper.get_input(2024, 6)

my_map = [list(line) for line in input.splitlines()]
guard_coordinates = []

for y, line in enumerate(my_map):
    for x, t in enumerate(line):
        if t in ["^", "v", ">", "<"]:
            guard_coordinates.append((x, y))
            break
    else:
        continue
    break

guard_states = {"^": ">", ">": "v", "v": "<", "<": "^"}
guard_movement = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

while True:
    x, y = guard_coordinates[-1]
    ox, oy = x, y
    dx, dy = guard_movement[my_map[y][x]]
    x += dx
    y += dy

    if x < 0 or x >= len(my_map[0]) or y < 0 or y >= len(my_map):
        break

    if my_map[y][x] == "#":
        x, y = guard_coordinates[-1]
        my_map[y][x] = guard_states[my_map[y][x]]
        continue

    my_map[y][x] = my_map[oy][ox]
    my_map[oy][ox] = "."

    guard_coordinates.append((x, y))

print(len(set(guard_coordinates)))
