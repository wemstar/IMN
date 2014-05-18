__author__ = 'wemstar'
import numpy as np
import utils
def initialize():
    matrix=np.zeros((241,81))

    (m,n)=matrix.shape
    for i in range(m):
        for j in range(n):
            matrix[i][j]=i


    return matrix
def prepareMatrix(matrix):
    matrix[:101,0]=matrix[:101,1]
    matrix[141:,0]=matrix[141:,1]

    matrix[141,:19]=matrix[142,:19]
    matrix[101,:19]=matrix[100,:19]
    matrix[101:142,19]=matrix[101:142,20]

    matrix[141,63:]=matrix[142,63:]
    matrix[101,63:]=matrix[100,63:]
    matrix[101:142,63]=matrix[101:142,64]

    matrix[101,63]=(matrix[100,63]+matrix[101,62])/2.0
    matrix[141,63]=(matrix[142,63]+matrix[101,62])/2.0
    matrix[101,19]=(matrix[100,19]+matrix[101,20])/2.0
    matrix[141,19]=(matrix[142,19]+matrix[101,20])/2.0


def metoda(matrix):
    error=1
    pa=[utils.a(matrix,1)]
    # while error >0.000001:
    for i in range(1000):
        prepareMatrix(matrix)
        utils.iterate(matrix)
        pa.append(utils.a(matrix,1))
        error=abs(pa[-1]-pa[-2])
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