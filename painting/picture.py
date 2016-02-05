class Picture:
    def __init__(self, filename=None, width=None, height=None):
        if filename:
            with open(filename) as f:
                self.height, self.width = map(int, f.readline().split())
                self.data = [[c == '#' for c in line] for line in f]
        elif width and height:
            self.width = width
            self.height = height
            self.data = [[False for i in range(width)] for j in range(height)]

    def __eq__(self, other):
        return isinstance(other, Picture) and self.data == other.data

    def __str__(self):
        return (''.join([''.join(['#' if c else '.' for c in row])+'\n' for row in self.data]))
