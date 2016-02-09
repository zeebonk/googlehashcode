import numpy as np

from painter import Painter


def print_labels(labels):
    for line in labels:
        print(''.join([str(d) if d else ' ' for d in line]))


def component_labeling(data):
    labels = np.zeros(data.shape, dtype=int)
    curlab = 1
    queue = []

    height, width = data.shape

    for y in range(height):
        for x in range(width):
            if data[y][x] and not labels[y][x]:
                labels[y][x] = curlab
                queue.append((y, x))

                while queue:
                    yy, xx = queue.pop()

                    if yy-1 >= 0 and not labels[yy-1][xx] and data[yy-1][xx]:
                        labels[yy-1][xx] = curlab
                        queue.append((yy-1, xx))
                    if xx-1 >= 0 and not labels[yy][xx-1] and data[yy][xx-1]:
                        labels[yy][xx-1] = curlab
                        queue.append((yy, xx-1))
                    if xx+1 < width and not labels[yy][xx+1] and data[yy][xx+1]:
                        labels[yy][xx+1] = curlab
                        queue.append((yy, xx+1))
                    if yy+1 < height and not labels[yy+1][xx] and data[yy+1][xx]:
                        labels[yy+1][xx] = curlab
                        queue.append((yy+1, xx))

                curlab += 1

    return labels, curlab-1

def paint_biggest_square(painter, picture, r, c):
    pass

def paint_longest_horizontal_line(painter, picture, r, c):
    length = 0
    for i in range(c + 1, painter.picture.shape[1]):
        if picture[r][i]:
            length += 1
        else:
            break
    p = painter.copy()
    p.paint_line(r, c, r, c + length)
    return p
    
def paint_longest_vertical_line(painter, picture, r, c):
    length = 0

    for i in range(r + 1, picture.shape[0]):
        if picture[i][c]:
            length += 1
        else:
            break
    p = painter.copy()
    p.paint_line(r, c, r + length, c)
    return p


def least_commands_needed(picture):
    queue = [Painter(picture.empty_copy())]
    height, width = picture.shape

    i = 0
    while queue:
        i+=1
        print(i, len(queue))
        new_queue = []
        for painter in queue:
            for r, c in painter.picture.positions_to_paint(picture):
                s = False
                if picture[r][c] and not painter.picture[r][c]:
                    # biggest square
                    #p = paint_biggest_square(painter, picture, r, c)
                    #if np.array_equal(p.picture, picture):
                    #    return p

                    # longest horizontal line
                    if c-1 >= 0 and not picture[r][c-1]:
                        s = True
                        p = paint_longest_horizontal_line(painter, picture, r, c)
                        if np.array_equal(p.picture, picture):
                            return p
                        new_queue.append(p)

                    # longest vertical line
                    if r-1 >= 0 and not picture[r-1][c]:
                        s = True
                        p = paint_longest_vertical_line(painter, picture, r, c)
                        if np.array_equal(p.picture, picture):
                            return p
                    new_queue.append(p)
                if s:
                    break
        queue =  new_queue

    print("---> SOMETHING HORRIBLE WENT WRONG <---")
    quit()

def algorithm(picture, args):
    pictures = []
    labels, no_labels = component_labeling(picture)

    commands = []
    
    for label in range(1, no_labels+1):
        p = picture.empty_copy()
        p[labels==label] = True
        print(p)
        pictures.append(p)
        painter = least_commands_needed(p)
        print(painter.commands)

        #commands.extend(painter.commands)

        break

    
    #print("%d\n%s" % (len(commands), '\n'.join(commands)))
    quit()

    return Painter(picture.empty_copy())
