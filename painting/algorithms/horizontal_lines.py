from painter import Painter


def algorithm(picture, args):
    """
    Try to use horizontal lines for each cell
    """
    painter = Painter(picture.empty_copy())

    for row, column in painter.picture.positions_to_paint(picture):
        if painter.picture[row][column]:
            continue

        length = 0

        for i in range(column + 1, picture.shape[1]):
            if picture[row][i]:
                length += 1
            else:
                break

        painter.paint_line(row, column, row, column + length)

    return painter
