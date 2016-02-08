import numpy as np


def from_file(path):
    with open(path) as f:
        f.readline()
        return np.array([[c == '#' for c in line] for line in f])


def empty_copy(picture):
	return np.zeros(picture.shape, dtype=bool)


def to_string(picture):
    return (''.join([''.join(['#' if c else '.' for c in row])+'\n' for row in picture]))


def positions_to_paint(working_picture, target_picture):
	return zip(*np.logical_xor(working_picture, target_picture).nonzero())
