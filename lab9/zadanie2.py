__author__ = 'wemstar'
import numpy as np
import utils
def zadanie2():
    matrix = np.zeros((129, 129))
    (m,n)=matrix.shape
    for k in range(m):
        matrix[0][k]=utils.potencjal(0,k)
        matrix[k][0]=utils.potencjal(k,0)
        matrix[m-1][k]=utils.potencjal(m-1,k)
        matrix[k][m-1]=utils.potencjal(k,m-1)
    pa=[]
    for k in [16,8,4,2,1]:
        pa.extend(utils.metoda(matrix,k))
        with open("Zadanie2.1.{0}.txt".format(k),"w") as fp:
            for i in range(0,m,k):
                for j in range(0,n,k):
                    fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(utils.rzutuj(i),utils.rzutuj(j),matrix[i][j]))
                fp.write("\n")
        if k ==1:
            break
        utils.newPoints(matrix,k)
    with open("Zadanie2.2.txt","w") as fp:
        for i,x in enumerate(pa):
            fp.write("{0:0.20f} {1:0.20f}\n".format(i+1,x))