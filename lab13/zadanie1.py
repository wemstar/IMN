__author__ = 'wemstar'
from matrixUtils import *
from methodUtils import *

def zadanie1():
    grid=generateGrid()
    recreateGrid(grid,0.0)
    stream1,stream2=method(grid,0.0,"Zadanie1.",[])
    saveGrid("Zadanie1.2.txt",grid)
    with open("Zadanie1.S.txt","w") as fp:
        for i,(s1,s2) in enumerate(zip(stream1,stream2)):
            fp.write("{0:0.20f} {1:0.20f} {2:0.20f} {3:0.20f}\n".format(i,s1,s2,s1-s2))

