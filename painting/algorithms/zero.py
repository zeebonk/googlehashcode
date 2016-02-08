import nppicture
from painter import Painter


def algorithm(picture, args):
    """
    Paint each cell with a single command resulting in a score 0
    """
    painter = Painter(nppicture.empty_copy(picture))

    for row, column in zip(*np.logical_xor(painter.picture, picture).nonzero()):
        painter.paint_square(row, column, 0)

    return painter
