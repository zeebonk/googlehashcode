import numpy as np

from painter import Painter


def algorithm(picture, args):
    """
    Paint each cell with a single command resulting in a score 0
    """
    painter = Painter(picture.empty_copy())

    for row, column in painter.picture.positions_to_paint(picture):
        painter.paint_square(row, column, 0)

    return painter
