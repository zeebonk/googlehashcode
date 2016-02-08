import nppicture
from painter import Painter


def algorithm(picture, args):
    """
    Paint each cell with a single command resulting in a score 0
    """
    painter = Painter(nppicture.empty_copy(picture))

    for i in range(picture.shape[0]):
        for j in range(picture.shape[1]):
            if picture[i][j]:
                painter.paint_square(i, j, 0)

    return painter
