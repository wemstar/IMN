__author__ = 'wemstar'

import numpy as np
def potencjal(i,j):
    x=rzutuj(i)
    y=rzutuj(j)
    return (x*0.5)**2.0-(y*0.5)**2.0
def rzutuj(i):
    return i*3.0/80.0-2.4

def metoda(matrix,k):
    error=1.0
    (m,n)=matrix.shape
    pu=[a(matrix,k)]
    while error > 0.000000001:
        matrix[k:-k:k,k:-k:k]=(matrix[:-2*k:k,k:-k:k]+matrix[k:-k:k,:-2*k:k]+matrix[2*k::k,k:-k:k]+matrix[k:-k:k,2*k::k])/4.0
        pu.append(a(matrix,k))
        error=abs(pu[-1]-pu[-2])
    return pu


def a(matrix,k):
    return np.sum((matrix[2*k::k,k:-k:k]+matrix[2*k::k,2*k::k]-matrix[k:-k:k,k:-k:k]-matrix[k:-k:k,2*k::k])**2.0+
    (matrix[k:-k:k,2*k::k]+matrix[2*k::k,2*k::k]-matrix[k:-k:k,k:-k:k]-matrix[2*k::k,k:-k:k])**2.0)/8.0
