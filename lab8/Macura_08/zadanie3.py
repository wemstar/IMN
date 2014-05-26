import numpy as np
from math import exp, sqrt




def zadanie3():
    file="Zadanie3_{0}.txt"
    tabRo=generateRo()
    for omega in [0.5,0.75,0.9,1.0]:
        matrix,pa=polason(omega,tabRo)
        with open(file.format(omega), "w") as fp:
            (m, n) = matrix.shape
            for i in range(m):
                for j in range(n):
                    fp.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, matrix[i][j]))
                fp.write("\n")
        with open(file.format(str(omega)+"_iter"),"w") as fp:
            for i,x in enumerate(pa):
                fp.write("{0:0.20f} {1:0.20f}\n".format(i,x))
    return matrix,tabRo


def polason(omega,roTab):
    error = 1
    pa =[1]
    matrix = np.zeros((121, 121))
    

    while error > 0.000000001:

        pa.append(a(matrix,roTab))
        matrix=metoda(matrix,omega,roTab)

        error = abs(pa[-1] - pa[-2])
    return matrix,pa

def metoda(matrix, omega,roTab):
    (m, n) = matrix.shape
    newMatrix = np.zeros((121, 121))
    newMatrix[1:-1,1:-1]=((1-omega)*matrix[1:-1,1:-1]+omega*0.25*(matrix[:-2,1:-1]+matrix[2:,1:-1]+matrix[1:-1,:-2]+matrix[1:-1,2:]+roTab[1:-1,1:-1]))
    # for i in range(1,m-1):
    #     for j in range(1,n-1):
    #         newMatrix[i][j]=(1-omega)*matrix[i][j]+omega*0.25*(matrix[i-1][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i][j-1]+roTab[i][j])

    return newMatrix 
def generateRo():

    tabRo= np.zeros((121, 121))
    (m, n) = tabRo.shape
    for i in range(1,m-1):
        for j in range(1,n-1):
            tabRo[i][j]=ro(i-60,j-60)
    return tabRo




def ro(x, y):
    return exp(-((sqrt((x * 0.1) ** 2.0 + (y * 0.1) ** 2) - 2.0) ** 2.0))


def a(matrix,roTab): 
    return np.sum((((matrix[2:,1:-1]-matrix[:-2,1:-1])*0.5)**2.0+((matrix[1:-1,2:]-matrix[1:-1,:-2])*0.5)**2.0)*0.5-matrix[1:-1,1:-1]*roTab[1:-1,1:-1])
    





