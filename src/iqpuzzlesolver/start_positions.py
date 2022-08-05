import numpy as np
from iqpuzzlesolver import pieces


def empty_grid():
    n_rows, n_cols = 5, 11
    return np.zeros((n_rows, n_cols), dtype=np.uint8)


def start_position(num):
    if num == 0:
        # Return an empty grid and all pieces
        grid = empty_grid()
        available_pieces = [
            pieces.pink(),
            pieces.red(),
            pieces.dark_red(),
            pieces.blue(),
            pieces.light_blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.light_green(),
            pieces.dark_green(),
            pieces.purple(),
            pieces.yellow(),
            pieces.orange(),
        ]
        return grid, available_pieces

    if num == 1:
        # Starting position 1
        grid = empty_grid()
        grid[:, :7] = 1
        grid[0, :9] = 1
        grid[3, :8] = 1
        grid[4, :9] = 1

        available_pieces = [
            pieces.red(2),
            pieces.green(3),
            pieces.purple(4)
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces

    if num == 25:
        # Starting position 25
        grid = empty_grid()
        grid[0, :] = 15
        grid[1, [0, 1, 4, 5, 6, 8, 9, 10]] = 15
        grid[2, [0, 1, 5]] = 15
        grid[3, 1] = 15

        available_pieces = [
            pieces.red(),
            pieces.dark_red(),
            pieces.blue(),
            pieces.dark_blue(),
            pieces.green(),
            pieces.dark_green(),
            pieces.orange(),
        ]
        available_pieces.sort(key=lambda x: (x.variants[0] != 0).sum())
        return grid, available_pieces
