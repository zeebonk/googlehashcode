import numpy as np

from painter import Painter


class Shape:
    def __init__(self, row, column, size):
        self.row = row
        self.column = column
        self.size = size

    def area(self):
        return self.size

    def __str__(self):
        return "<%s row=%d column=%d, size=%d, area=%d>" % (self.__class__.__name__, self.row, self.column, self.size, self.area())


class Square(Shape):
    def area(self):
        return (2 * self.size + 1) * (2 * self.size + 1)

    def paint(self, painter):
        painter.paint_square(self.row, self.column, self.size)


class Horizontal(Shape):
    def paint(self, painter):
        painter.paint_line(self.row, self.column, self.row, self.column + self.size)


class Vertical(Shape):
    def paint(self, painter):
        painter.paint_line(self.row, self.column, self.row + self.size, self.column)


def algorithm(picture, args):
    """
    Keep placing the biggest shape possible
    """
    painter = Painter(picture.empty_copy())

    while True:
        shape = find_largest_possible_shape(picture, painter.picture)
        if not shape:
            break
        # print(type(shape), shape)
        shape.paint(painter)

    return painter


def find_largest_possible_shape(picture, painter_picture):
    max_shape = Shape(-1, -1, -1)

    for row, column in painter_picture.positions_to_paint(picture):
        max_square = None
        max_vertical = None
        max_horizontal = None

        max_radius = min(
            picture.shape[0] - row,
            picture.shape[1] - column,
            row + 1,
            column + 1,
        )

        for i in range(0, max_radius):
            if picture[row - i:row + i + 1, column - i:column + i + 1].all():
                max_square = Square(row, column, i)
            else:
                break

        length = 0
        for i in range(column + 1, picture.shape[1]):
            if picture[row][i]:
                length += 1
            else:
                break
        max_horizontal = Horizontal(row, column, length)

        length = 0
        for i in range(row + 1, picture.shape[0]):
            if picture[i][column]:
                length += 1
            else:
                break
        max_vertical = Vertical(row, column, length)

        max_shape = max(max_shape, max_square, max_vertical, max_horizontal, key=lambda x: x.area())

    if max_shape.area() == -1:
        return None

    return max_shape
