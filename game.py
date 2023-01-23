def get_coordinates():
    return [
        [2, 3, 4, 5, 6, 4, 3, 2],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [2, 3, 4, 5, 6, 4, 3, 2]
    ]


def update_coordinates(coordinates, move_from, move_to):
    coordinates[move_to[0], move_to[1]] = coordinates[move_from[0], move_from[1]]
    coordinates[move_from[0], move_from[1]] = 0
