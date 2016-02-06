from picture import Picture
from painter import Painter

# Try to use horizontal lines for each cell
def algorithm(picture, args):
    painter = Painter(picture.width, picture.height)

    for j in range(picture.width):
        for i in range(picture.height):
            if painter.picture.data[i][j]:
                continue
            
            if picture.data[i][j]:
                length = 0

                for k in range(i+1, picture.height):
                    if picture.data[k][j]:
                        length += 1
                    else:
                        break

                painter.paint_line(i, j, i+length, j)

    print(painter.get_output())
