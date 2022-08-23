import numpy as np


def circle(
    size_x: int,
    size_y: int,
    origin_x: int,
    origin_y: int,
    radius: int,
) -> np.ndarray:

    x_grid = np.tile(np.arange(size_x), (size_y, 1))
    y_grid = np.tile(np.arange(size_y), (size_x, 1)).T

    np.subtract(x_grid, origin_x, out=x_grid)
    np.square(x_grid, out=x_grid)

    np.subtract(y_grid, origin_y, out=y_grid)
    np.square(y_grid, out=y_grid)

    np.add(x_grid, y_grid, out=x_grid)
    return (x_grid <= (radius * radius)).view(np.int8)
