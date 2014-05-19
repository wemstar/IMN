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
    # Doł
    matrix[:99,0]=matrix[:99,1]
    matrix[139:,0]=matrix[139:,1]
    # Góra
    matrix[:99,80]=matrix[:99,79]
    matrix[139:,80]=matrix[139:,79]
    # przeszkoda dolna
    matrix[140,:19]=matrix[139,:19]
    matrix[100,:19]=matrix[101,:19]
    matrix[100:141,19]=matrix[100:141,20]
    # przeskoda gorna
    matrix[140,62:]=matrix[141,62:]
    matrix[100,62:]=matrix[99,62:]
    matrix[100:141,62]=matrix[100:141,63]

    matrix[100,62]=(matrix[99,62]+matrix[100,61])/2.0
    matrix[140,62]=(matrix[141,62]+matrix[140,61])/2.0
    matrix[100,18]=(matrix[99,18]+matrix[100,19])/2.0
    matrix[140,18]=(matrix[141,18]+matrix[100,19])/2.0


def metoda(matrix):
    error=1
    pa=[utils.a(matrix,1)]
    # while error >0.000001:
    for i in range(5000):
        prepareMatrix(matrix)
        utils.iterate(matrix)
        pa.append(utils.a(matrix,1))
        error=abs(pa[-1]-pa[-2])
        print("{0:0.20f}\n".format(error))
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