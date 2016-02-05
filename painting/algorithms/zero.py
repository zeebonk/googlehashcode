from picture import Picture
from painter import Painter

# Paint each cell with a single command resulting in a score 0
def algorithm(picture, args):
    painter = Painter(picture.width, picture.height)

    for j in range(picture.width):
        for i in range(picture.height):
            if picture.data[i][j]:
                painter.paint_square(i, j, 0)

    print(painter.get_output())
