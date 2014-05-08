__author__ = 'wemstar'
import numpy as np
import utils
def zadanie1():
    matrix = np.zeros((129, 129))
    (m,n)=matrix.shape
    for k in range(m):
        matrix[0][k]=utils.potencjal(0,k)
        matrix[k][0]=utils.potencjal(k,0)
        matrix[m-1][k]=utils.potencjal(m-1,k)
        matrix[k][m-1]=utils.potencjal(k,m-1)
    pa=utils.metoda(matrix,1)
    with open("Zadanie1.1.txt","w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(utils.rzutuj(i),utils.rzutuj(j),matrix[i][j]))
            fp.write("\n")
    with open("Zadanie1.2.txt","w") as fp:
        for i,x in enumerate(pa):
            fp.write("{0:0.20f} {1:0.20f}\n".format(i+1,x))



