import numpy as np
from math import exp, sqrt


def zadanie1():
    matrix025,pa025=polason(0.25)
    matrix05,pa05=polason(0.5)
    matrix1,pa1=polason(1)
    matrix5,pa5=polason(1.5)
    matrix,pa=polason(1.95)
    with open("Zadanie1.txt", "w") as fp:
        (m, n) = matrix.shape
        for i in range(m):
            for j in range(n):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, matrix[i][j]))
            fp.write("\n")
    for a,file in zip([pa025,pa05,pa1,pa5,pa],["Zadanie1_025.txt","Zadanie1_05.txt","Zadanie1_1.txt","Zadanie1_15.txt","Zadanie1_195.txt"]):
        for i ,val in enumerate(a):
            with open(file,"w") as fp:
                fp.write("{0} {1}\n".format(i,val))


def polason(omega):
    error = 1
    pa =[1]
    matrix = np.zeros((121, 121))
    while error > 0.000000001:

        pa.append(a(matrix))
        metoda(matrix,omega)

        error = abs(pa[-1] - pa[-2])
    return matrix,pa

def metoda(matrix, omega):
    (m, n) = matrix.shape
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            matrix[i][j] = (1 - omega) * matrix[i][j] + omega * (
                matrix[i + 1][j] + matrix[i - 1][j] + matrix[i][j + 1] + matrix[i][j - 1] + ro(i-60, j-60)) * 0.25


def ro(x, y):
    return exp(-((sqrt((x * 0.1) ** 2.0 + (y * 0.1) ** 2) - 2.0) ** 2.0))


def a(matrix):
    suma = 0
    (m, n) = matrix.shape
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            pochodnax = (matrix[i + 1][j] - matrix[i - 1][j]) * 0.5
            pochodnay = (matrix[i][j + 1] - matrix[i][j - 1]) * 0.5
            trzeci = matrix[i][j] * ro(i - 60.0, j - 60.0)
            suma += (0.5 * (pochodnax ** 2.0 + pochodnay ** 2.0) - trzeci)
    return suma