__author__ = 'wemstar'

import numpy as np


def potencjal(i, j):
    x = rzutuj(i)
    y = rzutuj(j)
    return (x * 0.5) ** 2.0 - (y * 0.5) ** 2.0


def rzutuj(i):
    return i * 3.0 / 80.0 - 2.4


def metoda(matrix, k):
    error = 1.0
    (m,n)=matrix.shape
    pu = [a(matrix, k)]
    while error > 0.000000001:
        # matrix[k:-k:k, k:-k:k] = (matrix[:-2 * k:k, k:-k:k] + matrix[k:-k:k, :-2 * k:k]
        #                           + matrix[2 * k::k, k:-k:k] + matrix[k:-k:k, 2 * k::k]) / 4.0
        for i in range(k,m-k,k):
            for j in range(k,n-k,k):
                matrix[i][j]=(matrix[i-k][j]+matrix[i][j-k]+matrix[i+k][j]+matrix[i][j+k])/4.0
        pu.append(a(matrix, k))
        error = abs(pu[-1] - pu[-2])
    return pu[1:]


def a(matrix, k):
    return np.sum((matrix[k::k, :-k:k] + matrix[k::k, k::k] - matrix[:-k:k, :-k:k] - matrix[:-k:k, k::k]) ** 2.0 +
                  (matrix[:-k:k, k::k] + matrix[k::k, k::k] - matrix[:-k:k, :-k:k] - matrix[k::k, :-k:k]) ** 2.0) / 8.0


def newPoints(matrix, k):
    # matrix[k / 2:-k / 2:k, ::k] = (matrix[:-k:k, ::k] + matrix[k::k, ::k]) * 0.5
    # matrix[::k, k / 2:-k / 2:k] = (matrix[::k, :-k:k] + matrix[::k, k::k]) * 0.5
    # matrix[k / 2:-k / 2:k, k / 2:-k / 2:k] = (matrix[:-k:k, :-k:k] + matrix[k::k, :-k:k] + matrix[:-k:k, k::k] + matrix[
    #                                                                                                              k::k,
    #                                                                                                              k::k]) * 0.25
    (m,n)=matrix.shape
    nk=int(k/2)
    for i in range(nk,m-nk,nk):
        for j in range(nk,m-nk,nk):
            if (j % k) !=0:
                if (i % k) !=0:
                    matrix[i][j]=(matrix[i+nk][j+nk]+matrix[i+nk][j-nk]+matrix[i-nk][j-nk]+matrix[i-nk][j+nk])/4.0
                else:
                    matrix[i][j]=(matrix[i][j+nk]+matrix[i][j-nk])*0.5
            elif (i%k)!=0:
                matrix[i][j]=(matrix[i+nk][j]+matrix[i-nk][j])*0.5


    # for i in range(nk,m-nk,k):
    #     for j in range(nk,m-nk,k):
    #         matrix[i][j]=(matrix[i-nk][j]+matrix[i+nk][j]+matrix[i][j-nk]+matrix[i][j+nk])/4.0

    # print(matrix)
