__author__ = 'wemstar'
import utils
import numpy as np
from sys import stdout
def initialize():
    matrix=np.zeros((241,81))

#     lewy,prawy
    for i in range(81):
        matrix[0][i]=i
        matrix[240][i]=i
#     Gora dol
    for i in range(241):
        matrix[i][0]=0
        matrix[i][80]=80
    matrix[100:141,:19]=0
    matrix[100:141,62:]=80

    return matrix

def metoda(matrix):
    error=1
    pa=[utils.a(matrix,1)]
    while error >0.000001:
    # for i in range(1000):
        utils.iterate(matrix)
        pa.append(utils.a(matrix,1))
        error=abs(pa[-1]-pa[-2])
        stdout.write("\r{0:0.20f}    ".format(error))
        stdout.flush()
    print(" ")
    return pa

def zadanie1():
    matrix=initialize()
    pa=metoda(matrix)
    (m,n)=matrix.shape
    with open("Zadanie1.1.txt","w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i,j,matrix[i][j]))
            fp.write("\n")
    with open("Zadanie1.2.txt","w") as fp:
        for x,e in enumerate(pa):
            fp.write("{0:0.20f} {1:0.20f}\n".format(x,e))
    return matrix
