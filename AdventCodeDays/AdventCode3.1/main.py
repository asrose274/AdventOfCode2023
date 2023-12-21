grid = open("input.txt").read().splitlines()
coordinates = set()

for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch.isdigit() or ch == ".":
            continue
        for current_row in [r - 1, r, r + 1]:
            for current_column in [c - 1, c, c + 1]:
                if current_row < 0 or current_row >= len(grid) or current_column < 0 or current_column >= len(grid[current_row]) or not grid[current_row][current_column].isdigit():
                    continue
                while current_column > 0 and grid[current_row][current_column - 1].isdigit():
                    current_column-= 1
                coordinates.add((current_row, current_column))

number_list = []

for r, c in coordinates:
    s = ""
    while c < len(grid[r]) and grid[r][c].isdigit():
        s += grid[r][c]
        c += 1
    number_list.append(int(s))

print(sum(number_list))