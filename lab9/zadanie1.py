__author__ = 'wemstar'
import numpy as np

def zadanie1():
    matrix = np.zeros((129, 129))
    (m,n)=matrix.shape
    for k in range(m):
        matrix[0][k]=potencjal(0,k)
        matrix[k][0]=potencjal(k,0)
        matrix[m-1][k]=potencjal(m-1,k)
        matrix[k][m-1]=potencjal(k,m-1)
    pa=metoda(matrix)
    with open("Zadanie1.1.txt","w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(rzutuj(i),rzutuj(j),matrix[i][j]))
            fp.write("\n")
    with open("Zadanie1.2.txt","w") as fp:
        for i,x in enumerate(pa):
            fp.write("{0:0.20f} {1:0.20f}\n".format(i+1,x))



def potencjal(i,j):
    x=rzutuj(i)
    y=rzutuj(j)
    return (x*0.5)**2.0-(y*0.5)**2.0
def rzutuj(i):
    return i*3.0/80.0-2.4

def metoda(matrix):
    error=1.0
    (m,n)=matrix.shape
    pu=[a(matrix,1)]
    while error > 0.000000001:
        matrix[1:-1,1:-1]=(matrix[:-2,1:-1]+matrix[1:-1,:-2]+matrix[2:,1:-1]+matrix[1:-1,2:])/4.0
        pu.append(a(matrix,1))
        error=abs(pu[-1]-pu[-2])
    return pu


def a(matrix,k):
    return np.sum((matrix[1+k:,1:-1]+matrix[1+k:,1+k:]-matrix[1:-1,1:-1]-matrix[1:-1,1+k:])**2.0+
    (matrix[1:-1,1+k:]+matrix[1+k:,1+k:]-matrix[1:-1,1:-1]-matrix[1+k:,1:-1])**2.0)/8.0