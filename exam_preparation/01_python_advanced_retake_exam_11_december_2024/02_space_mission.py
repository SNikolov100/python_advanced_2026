n = int(input())
grid_space = []
resource = set()
meteor = set()
ship = None
planet_b = None
units = 100


maper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1)
}

for row in range(n):
    grid_space.append(input().split())
    for col in range(n):
        if grid_space[row][col] == "S":
            ship = (row, col)
        elif grid_space[row][col] == "M":
            meteor.add((row, col))
        elif grid_space[row][col] == "P":
            planet_b = (row, col)
        elif grid_space[row][col] == "R":
            resource.add((row, col))

while True:
    direction = input()
    r, c = ship
    add_r, add_c = maper[direction]
    new_row, new_col = r + add_r, c + add_c
    if 0<= new_row < n and 0<= new_col < n:

        if grid_space[r][c] != "R":
            grid_space[r][c] = "."
        if grid_space[new_row][new_col] != "R" and grid_space[new_row][new_col] != "P":
            grid_space[new_row][new_col] = "S"
        units -= 5

        if (new_row, new_col) in meteor:
            units -= 5
            meteor.remove((new_row, new_col))
            grid_space[new_row][new_col] = "."
        elif (new_row, new_col) in resource:
            units += 10
            if units > 100:
                units = 100

        if (new_row, new_col) == planet_b:
            print(f"Mission accomplished! The spaceship reached Planet B with {units} resources left.")
            break

        if units < 5:
            print(f"Mission failed! The spaceship was stranded in space.")
            break

        ship = (new_row, new_col)
    else:
        grid_space[r][c] = "S"
        print("Mission failed! The spaceship was lost in space.")
        break

if ship == planet_b:
    grid_space[ship[0]][ship[1]] = "P"
for row in range(n):
    print(f"{' '.join(x for x in grid_space[row])}")