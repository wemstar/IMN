__author__ = 'wemstar'
import numpy as np
import utils
from sys import stdout
def initialize():
    matrix=np.zeros((241,81))

    (m,n)=matrix.shape
    for i in range(m):
        for j in range(n):
            if ((i >=100 and i<=140) and (j<=18 or j >=62)):
                continue
            matrix[i][j]=i


    return matrix
def prepareMatrix(matrix):
    # Dol
    matrix[:101,0]=matrix[:101,1]
    matrix[140:,0]=matrix[140:,1]
    # Gora
    matrix[:101,80]=matrix[:101,79]
    matrix[140:,80]=matrix[140:,79]
    # przeszkoda dolna
    matrix[140,:19]=matrix[141,:19]
    matrix[100,:19]=matrix[99,:19]
    matrix[100:141,18]=matrix[100:141,19]
    # przeskoda gorna
    matrix[140,62:]=matrix[141,62:]
    matrix[100,62:]=matrix[99,62:]
    matrix[100:141,62]=matrix[100:141,61]

    matrix[100,62]=(matrix[99,62]+matrix[100,61])/2.0
    matrix[140,62]=(matrix[141,62]+matrix[140,61])/2.0
    matrix[100,18]=(matrix[99,18]+matrix[100,19])/2.0
    matrix[140,18]=(matrix[141,18]+matrix[140,19])/2.0


def metoda(matrix):
    error=1
    pa=[utils.a(matrix,1)]
    while error >0.000001:
    # for i in range(1000):
        prepareMatrix(matrix)
        utils.iterate(matrix)
        pa.append(utils.a(matrix,1))
        error=abs(pa[-1]-pa[-2])
        stdout.write("\r{0:0.20f}     ".format(error))
        stdout.flush()
    print(" ")
    return pa

def zadanie2():
    matrix=initialize()
    pa=metoda(matrix)
    (m,n)=matrix.shape
    with open("Zadanie2.1.txt","w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i,j,matrix[i][j]))
            fp.write("\n")
    with open("Zadanie2.2.txt","w") as fp:
        for x,e in enumerate(pa):
            fp.write("{0:0.20f} {1:0.20f}\n".format(x,e))
    return matrix