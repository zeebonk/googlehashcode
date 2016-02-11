import sys
from random import randint

import numpy as np

from painter import Painter


def find_largest_rectangle(working, target):
    max_rect = None
    max_rect_size = -1

    remaining = np.logical_and(target, np.logical_not(working))
    # print(len(remaining.nonzero()[0]))

    for i, (row, col) in enumerate(zip(*remaining.nonzero())):
        # Find maximum height
        height = 0
        for j in range(row, remaining.shape[0]):
            if remaining[j, col]:
                height += 1
            else:
                break

        # Find maximum rectangle by increasing width to the right
        col_max = col
        for j in range(col, remaining.shape[1]):
            if remaining[row:row + height, col:j].all():
                col_max = j
            else:
                break

        # Find maximum rectangle by increasing width to the left
        col_min = col
        for j in range(col, -1, -1):
            if remaining[row:row + height, j:col].all():
                col_min = j
            else:
                break

        size = height * (col_max - col_min)
        if size > max_rect_size:
            max_rect = (row, col_min, height, col_max - col_min)
            max_rect_size = size

    return max_rect


def paint_rectangle(painter, r1, c1, r2, c2):
    picture = painter.picture[r1:r2 + 1, c1:c2 + 1]
    height, width = picture.shape
    wider = width > height
    long_side, short_side = (width, height) if wider else (height, width)

    xshort_side = short_side - (1 - (short_side % 2))
    if xshort_side * xshort_side <= long_side:
        # Rectangles that can be optimally filled using just lines
        # Fill every line
        for i in range(short_side):
            if wider:
                painter.paint_line(r1+i, c1+0, r1+i, c1+long_side-1)
            else:
                painter.paint_line(r1+0, c1+i, r1+long_side-1, c1+i)
    else:
        # Rectangles that must be filled with squares and lines

        # Make sure the rectangle has an uneven hight for better filling with
        # square by filling in the bottom row with a line
        if short_side % 2 == 0:
            if wider:
                painter.paint_line(r1+short_side-1, c1+0, r1+short_side-1, c1+long_side-1)
            else:
                painter.paint_line(r1+0, c1+short_side-1, r1+long_side-1, c1+short_side-1)
            short_side -= 1

        # Fill remaining space non-overlapping squares
        offset = short_side / 2
        size = (short_side - 1) / 2
        for i in range(long_side // short_side):
            if wider:
                painter.paint_square(r1 + offset, c1 + offset + short_side * i, size)
            else:
                painter.paint_square(r1 + offset + short_side * i, c1 + offset, size)

        # Fill remaining space with one overlapping square
        if long_side % short_side != 0:
            if wider:
                painter.paint_square(r1 + offset, c1 + long_side - offset, size)
            else:
                painter.paint_square(r1 + long_side - offset, c1 + offset, size)


def algorithm(picture, args):
    painter = Painter(picture.empty_copy())

    while True:
        rect = find_largest_rectangle(painter.picture, picture)
        if not rect:
            break
        row, col, height, width = rect
        paint_rectangle(painter, row, col, row + height - 1, col + width - 1)

    return painter
