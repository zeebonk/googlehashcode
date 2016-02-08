import numpy as np


class Picture(np.ndarray):
    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            f.readline()
            return np.array([[c == '#' for c in line] for line in f]).view(Picture)

    def empty_copy(self):
        return np.zeros(self.shape, dtype=bool).view(Picture)


    def __str__(self):
        return (''.join([''.join(['#' if c else '.' for c in row])+'\n' for row in self]))

    def positions_to_paint(self, target_picture):
        return zip(*np.logical_xor(self, target_picture).nonzero())
