import numpy as np

import nppicture
from painter import Painter


def algorithm(picture, args):
    """
    Paint each cell with a single command resulting in a score 0
    """
    painter = Painter(nppicture.empty_copy(picture))

    for row, column in nppicture.positions_to_paint(painter.picture, picture):
        painter.paint_square(row, column, 0)

    return painter
