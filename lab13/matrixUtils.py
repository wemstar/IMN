from math import sqrt

__author__ = 'wemstar'

import numpy as np
imin=0
i1=30
i2=50
imax=80
jmin=0
j1=20
j2=30
jmax=50
def generateGid():

    grid=np.zeros([81,51])
    grid[0,j2:jmax]=36.0
    grid[imax,jmin:j1]=-5.0

    return grid
def recreateGrid(grid):
    h=grid.h
    grid[i2,j1:jmax]=grid[i2-1,j1:jmax]/(h+1)#E
    grid[i1,jmin:j2]=grid[i1-1,jmin:j2]/(h+1)#B
    grid[imin:i1,j2]=grid[imin:i1,j2+1]/(h+1)#A
    grid[i1:imax,jmin]=grid[i1:imax,jmin+1]/(h+1)#C
    grid[i2:imax,j1]=grid[i2:imax,j1-1]/(h+1)#D
    grid[imin:i2]=grid[imin:i2]/(h+1)#F
    grid[i2,jmax]=grid[i2-1,jmax-1]/(sqrt(2.0)*h+1)#F\E
    grid[i2,j1]=grid[i2-1,j1-1]/(sqrt(2.0)*h+1)#E\D
    grid[i1,j2]=grid[i1+1,j2+1]/(sqrt(2.0)*h+1)
    grid[i1,jmin]=grid[i1+1,jmin+1]/(sqrt(2.0)*h+1)
def computeGird(grid,pgrid,i1,i2,j1,j2):
    pass
def iterateGrid(grid,pgrid):
    error=1.0
    while error > 0.0000001:
        pass


