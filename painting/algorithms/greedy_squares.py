import numpy as np

import nppicture
from painter import Painter


class Square:
    def __init__(self, row, column, size):
        self.row = row
        self.column = column
        self.size = size

    def __str__(self):
        return "<Square row=%d column=%d, size=%d>" % (self.row, self.column, self.size)


def algorithm(picture, args):
    """
    Keep placing the biggest square possible
    """
    painter = Painter(nppicture.empty_copy(picture))

    square = Square(-1, -1, 100000)
    while True:
        square = get_largest_unpainted_square(picture, painter, square.size)
        if not square:
            break
        painter.paint_square(square.row, square.column, square.size)

    return painter


def get_largest_unpainted_square(picture, painter, prev_size):
    largest_square = Square(-1, -1, -1)
    for row, column in nppicture.positions_to_paint(painter.picture, picture):
        max_radius = min(
            picture.shape[0] - row,
            picture.shape[1] - column,
            row + 1,
            column + 1,
            prev_size + 1,
        )

        for i in range(largest_square.size + 1, max_radius):
            if picture[row - i:row + i + 1, column - i:column + i + 1].all():
                largest_square = Square(row, column, i)
            else:
                break

    if largest_square.size == -1:
        return None

    return largest_square
