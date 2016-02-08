class Painter(object):
    def __init__(self, picture):
        self.picture = picture
        self.commands = []

    def paint_square(self, r, c, s):
        if r-s < 0 or r+s >= self.picture.shape[0] or c-s < 0 or c+s >= self.picture.shape[1]:
            raise ValueError

        self.picture[r-s:r+s+1, c-s:c+s+1] = True

        self.commands.append("PAINT_SQUARE %d %d %d" % (r, c, s))

    def paint_line(self, r1, c1, r2, c2):
        if not (r1 == r2 or c1 == c2):
            raise ValueError

        self.picture[r1:r2+1, c1:c2+1] = True

        self.commands.append("PAINT_LINE %d %d %d %d" % (r1, c1, r2, c2))

    def erase_cell(self, r, c):
        self.picture[r][c] = False

        self.commands.append("ERASE_CELL %d %d" % (r, c))

    def get_output(self):
        return "%d\n%s" % (len(self.commands), '\n'.join(self.commands))
