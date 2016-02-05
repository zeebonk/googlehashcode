from picture import Picture


class Painter:
    def __init__(self, width, height):
        self.picture = Picture(width=width, height=height)
        self.commands = []

    def paint_square(self, r, c, s):
        if r-s < 0 or r+s >= self.picture.height or c-s < 0 or c+s >= self.picture.width:
            raise ValueError

        for i in range(r-s, r+s+1):
            for j in range(c-s, c+s+1):
                self.picture.data[i][j] = True

        self.commands.append("PAINT_SQUARE %d %d %d" % (r, c, s))

    def paint_line(self, r1, c1, r2, c2):
        if not (r1 == r2 or c1 == c2):
            raise ValueError

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                self.picture.data[i][j] = True

        self.commands.append("PAINT_LINE %d %d %d %d" % (r1, c1, r2, c2))

    def erase_cell(self, r, c):
        self.picture.data[r][c] = False

        self.commands.append("ERASE_CELL %d %d" % (r, c))

    def get_output(self):
        return "%d\n%s" % (len(self.commands), '\n'.join(self.commands))
