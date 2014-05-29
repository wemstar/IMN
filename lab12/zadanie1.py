__author__ = 'wemstar'
import numpy as np
from utils import *
def zadanie1():
    u=prepareU(np.zeros([301, 91]))
    v=np.zeros([301, 91])
    mI=[]
    mIX=[]
    for x,ro in enumerate(leapfrog(u,v)):
        with open("Zadanie1.{0}.txt".format(x),"w") as fp:
            saveMatrix(fp,ro)
            # mI.append(I)
            # mIX.append(IX)

def prepareU(matrix):
    (m,n)=matrix.shape
    for i in range(n):
        y=i*0.01
        matrix[:,i]=-1.0/2.0*y*(y-0.9)
    return matrix