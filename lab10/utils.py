__author__ = 'wemstar'
import numpy as np


def iterate(matrix):
    (m,n)=matrix.shape
    for x in range(1,m-1):
        for y in range(1,n-1):
            if ((x >=100 and x<=140) and (y<=18 or y >=62)):
                continue
            matrix[x][y]=(matrix[x-1][y]+matrix[x][y-1]+matrix[x+1][y]+matrix[x][y+1])/4.0


def a(matrix, k):
    sum=0
    (m,n)=matrix.shape
    for x in range(1,m-1):
        for y in range(1,n-1):
            if ((x >=100 and x<=140) and (y<=18 or y >=62)):
                continue
            sum+=((matrix[x+1][y]-matrix[x-1][y])**2.0+(matrix[x][y+1]-matrix[x][y-1])**2.0)
    return sum/8.0












