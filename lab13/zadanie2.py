__author__ = 'wemstar'
from matrixUtils import *
from methodUtils import *

def zadanie2():
    grid=generateGrid()
    recreateGrid(grid,0.03)
    saveGrid("Zadanie2.1.txt",grid)
    method(grid,0.03)
    saveGrid("Zadanie2.2.txt",grid)