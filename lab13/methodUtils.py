__author__ = 'dom'
from matrixUtils import *
import numpy as np


def iterateGrid(grid, pgrid, h):
    error = 1.0
    while error > 0.0000001:
    # for z in range(200):
        recreateGrid(grid, h)
        error1 = computeError(grid)
        computeGird(grid, pgrid, imin + 1, i2, j2+1, jmax)
        computeGird(grid, pgrid, i1 +1, i2, jmin+1, j2+1)
        computeGird(grid, pgrid, i2, imax, jmin + 1, j1)
        error2 = computeError(grid)
        error = abs(error1 - error2)


def method(grid, h):
    pgrid = np.copy(grid)
    error=1.0
    t=0.0
    streqm1=[]
    stream2=[]
    while error >0.00000004:
        iterateGrid(grid, pgrid, h)
        error=abs(computeError(grid)-computeError(pgrid))
        pgrid = np.copy(grid)
        t+=1
        streqm1.append(stream(grid,imin+1,j2,jmax))
        stream2.append(stream(grid,imax-1,jmin,j1))
        print(error)
    return streqm1,stream2


def computeError(grid):
    return np.sum(np.absolute(grid))

def stream(grid,i,j1,j2):
    return np.sum(grid[i,j1:j2])