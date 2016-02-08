from painter import Painter


def algorithm(picture, args):
    """
    Try to use vertical lines for each cell
    """
    painter = Painter(picture.empty_copy())

    for row, column in painter.picture.positions_to_paint(picture):
        if painter.picture[row][column]:
            continue

        length = 0

        for i in range(row + 1, picture.shape[0]):
            if picture[i][column]:
                length += 1
            else:
                break

        painter.paint_line(row, column, row + length, column)

    return painter
