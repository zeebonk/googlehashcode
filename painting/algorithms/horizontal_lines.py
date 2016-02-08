import nppicture
from painter import Painter


def algorithm(picture, args):
    """
    Try to use horizontal lines for each cell
    """
    painter = Painter(nppicture.empty_copy(picture))

    for j in range(picture.shape[1]):
        for i in range(picture.shape[0]):
            if painter.picture[i][j]:
                continue

            if picture[i][j]:
                length = 0

                for k in range(j+1, picture.shape[1]):
                    if picture[i][k]:
                        length += 1
                    else:
                        break

                painter.paint_line(i, j, i, j+length)

    return painter
