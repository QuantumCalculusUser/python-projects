# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/train/python
def find_neighbour(point, ships, direction=None, l=None):
    if l is None:
        l = [point]          # include starting point

    if direction == 0:
        if [point[0] + 1, point[1]] in ships:
            l.append([point[0] + 1, point[1]])
            return find_neighbour([point[0] + 1, point[1]], ships, 0, l)
        return l

    elif direction == 1:
        if [point[0], point[1] + 1] in ships:
            l.append([point[0], point[1] + 1])
            return find_neighbour([point[0], point[1] + 1], ships, 1, l)
        return l

    else:
        right = [point[0] + 1, point[1]]
        down = [point[0], point[1] + 1]

        if right in ships and down in ships:
            return None      # L-shape

        if right in ships:
            l.append(right)
            return find_neighbour(right, ships, 0, l)

        if down in ships:
            l.append(down)
            return find_neighbour(down, ships, 1, l)

        return l


def validate_battlefield(field):

    # diagonal touching check
    for y in range(10):
        for x in range(10):
            if field[y][x]:

                for dx, dy in ((1,1),(-1,1),(1,-1),(-1,-1)):
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < 10 and 0 <= ny < 10:
                        if field[ny][nx]:
                            return False

    ships = []

    for y in range(10):
        for x in range(10):
            if field[y][x]:
                ships.append([x + 1, y + 1])

    visited = []
    groups = []

    for ship in ships:
        if ship not in visited:

            group = find_neighbour(ship, ships)

            if group is None:
                return False

            groups.append(group)

            for cell in group:
                visited.append(cell)

    battleship = 0
    cruisers = 0
    destroyers = 0
    submarines = 0

    for group in groups:

        if len(group) == 4:
            battleship += 1

        elif len(group) == 3:
            cruisers += 1

        elif len(group) == 2:
            destroyers += 1

        elif len(group) == 1:
            submarines += 1

        else:
            return False

    return (
        battleship == 1 and
        cruisers == 2 and
        destroyers == 3 and
        submarines == 4
    )
