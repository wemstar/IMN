from math import sqrt

__author__ = 'wemstar'

import numpy as np

imin = 0
i1 = 30
i2 = 50
imax = 80
jmin = 0
j1 = 20
j2 = 30
jmax = 50


def generateGrid():
    grid = np.zeros([81, 51])
    grid[0, j2:jmax] = 36.0
    grid[imax, jmin:j1] = -5.0

    return grid


def recreateGrid(grid, h):
    grid[i2, j1:jmax] = grid[i2 - 1, j1:jmax] / (h + 1)  # E
    grid[i1, jmin:j2] = grid[i1 + 1, jmin:j2] / (h + 1)  # B
    grid[imin:i1, j2] = grid[imin:i1, j2 + 1] / (h + 1)  # A
    grid[i1:imax, jmin] = grid[i1:imax, jmin + 1] / (h + 1)  # C
    grid[i2:imax, j1] = grid[i2:imax, j1 - 1] / (h + 1)  # D
    grid[imin:i2, jmax] = grid[imin:i2, jmax - 1] / (h + 1)  # F
    # grid[i2, jmax] = grid[i2 - 1, jmax - 1] / (sqrt(2.0) * h + 1)  # F\E
    # grid[i2, j1] = grid[i2 - 1, j1 - 1] / (sqrt(2.0) * h + 1)  # E\D
    # grid[i1, j2] = grid[i1 + 1, j2 + 1] / (sqrt(2.0) * h + 1)
    # grid[i1, jmin] = grid[i1 + 1, jmin + 1] / (sqrt(2.0) * h + 1)


# def computeGird(grid, pgrid, i1, i2, j1, j2):
# for i in range(i1, i2):
# for j in range(j1, j2):
# grid[i, j] = (pgrid[i, j] + 5.0 * (
# pgrid[i, j - 1] + pgrid[i, j + 1] + pgrid[i - 1, j] + pgrid[i + 1, j] - 4.0 * pgrid[i, j]
#             + grid[i, j - 1] + grid[i, j + 1] + grid[i - 1, j] + grid[i + 1, j])) / 21.0

def computeGird(grid, pgrid, i1, i2, j1, j2):
    grid[i1:i2, j1:j2] = (pgrid[i1:i2, j1:j2] + 5.0 * (
        pgrid[i1:i2, j1 - 1:j2 - 1] + pgrid[i1:i2, j1 + 1:j2 + 1] + pgrid[i1 - 1:i2 - 1, j1:j2] +
        pgrid[i1 + 1:i2 + 1, j1:j2] - 4.0 * pgrid[i1:i2, j1:j2]
        + grid[i1:i2, j1 - 1:j2 - 1] + grid[i1:i2, j1 + 1:j2 + 1] + grid[i1 - 1:i2 - 1, j1:j2]
        + grid[i1 + 1:i2 + 1, j1:j2])) / 21.0


def saveGrid(filename, grid):
    (m, n) = grid.shape
    with open(filename, "w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n ".format(i, j, grid[i, j]))
            fp.write("\n")


