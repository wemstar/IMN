__author__ = 'wemstar'
from matrixUtils import *
from methodUtils import *

def zadanie1():
    grid=generateGrid()
    recreateGrid(grid,0.0)
    saveGrid("Zadanie1.1.txt",grid)
    method(grid,0.0)
    saveGrid("Zadanie1.2.txt",grid)
    print("Hura")
