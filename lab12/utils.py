from math import exp

__author__ = 'wemstar'
import numpy as np


def ro(x, y):
    return exp(-25.0 * ((x - 0.4) ** 2.0 + (y - 0.45) ** 2.0))


def roMatrix(matrix):
    (m, n) = matrix.shape
    for i in range(m):
        for j in range(n):
            matrix[i][j] = ro(i * 0.01, j * 0.01)
    return matrix


def ro2Matrix(matrix, u, v, dt):
    (m, n) = matrix.shape

    for i in range(1,m-1):
        for j in range(1,n-1):
            matrix[i][j] = ro(i * 0.01 - u[i][j] * dt, j * 0.01 - v[i][j] * dt)
    return matrix
def I(matrix):
    return np.sum(matrix)*0.0001
def IX(matrix):
    sum=0
    (m,n)=matrix.shape
    for i in range(m):
        sum+=np.sum(i*matrix[i,:])
    return sum/I(matrix)*0.00001

def leapfrog(U, V,IC,IXC):
    dt = 0.01 / (4.0 * np.amax(np.sqrt(U ** 2 + V ** 2)))
    ro0 = roMatrix(np.zeros([301, 91]))
    ro1 = ro2Matrix(np.zeros([301, 91]), U, V, dt)
    ro2 =np.zeros([301,91])
    i=0
    t=0.0
    while t < 100.0:
        ro2[1:-1,1:-1]=ro0[1:-1,1:-1]-dt\
                *(U[1:-1,1:-1]*(ro1[2:,1:-1]-ro1[:-2,1:-1])/0.01
                +V[1:-1,1:-1]*(ro1[1:-1,2:]-ro1[1:-1,:-2])/0.01)

        ro2[0,1:-1]=ro0[0,1:-1]-dt*\
                 (U[0,1:-1]*(ro1[1,1:-1]-ro1[300,1:-1])/0.01+
                  V[0,1:-1]*(ro0[0,2:]-ro1[0,:-2])/0.01)
        ro2[300,1:-1]=ro0[300,1:-1]-dt*\
                 (U[300,1:-1]*(ro1[0,1:-1]-ro1[299,1:-1])/0.01+
                  V[300,1:-1]*(ro1[300,2:]-ro1[300,:-2])/0.01)
        IC.append(I(ro2))
        IXC.append(IX(ro2))
        if(i%800 == 0):
            yield  ro2

        ro0=np.copy(ro1)
        ro1=np.copy(ro2)
        i+=1
        t+=dt

def saveMatrix(file,matrix):
    (m,n)=matrix.shape
    with open(file,"w") as fp:
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i*0.01,j*0.01,matrix[i][j]))
            fp.write("\n")

