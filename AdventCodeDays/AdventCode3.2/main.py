grid = open("input.txt").read().splitlines()
total = 0

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch != "*":
            continue

        coordinates = set()

        for current_row in [r - 1, r, r + 1]:
            for current_column in [c - 1, c, c + 1]:
                if current_row < 0 or current_row >= len(grid) or current_column < 0 or current_column >= len(grid[current_row]) or not grid[current_row][current_column].isdigit():
                    continue
                while current_column > 0 and grid[current_row][current_column - 1].isdigit():
                    current_column-= 1
                coordinates.add((current_row, current_column))

        if len(coordinates) != 2:
            continue

        number_list = []

        for cr, cc in coordinates:
            s = ""
            while cc < len(grid[cr]) and grid[cr][cc].isdigit():
                s += grid[cr][cc]
                cc += 1
            number_list.append(int(s))

        total += number_list[0] * number_list[1]

print(total)