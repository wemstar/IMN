from math import pi, sin, cos

__author__ = 'dom'

import numpy as np

class Punkt:
    def __init__(self,s,sigma):
        self.s=s
        self.sigma=sigma

    def __str__(self):
        return "{0.s:0.20f} {0.sigma:0.20f}\n".format(self)
def zadanie2():
    fileNames=("Zadanie2.0.txt","Zadanie2.1.txt","Zadanie2.2.txt","Zadanie2.3.txt","Zadanie2.4.txt")
    for x,i in zip(algorytm(),fileNames):
        with open(i,"w") as fp:
            for z in x:
                fp.write("{0}".format(z))






def algorytm():
    sigma=np.zeros(101)
    F=np.zeros(99)
    sigma[0]=pi*0.25
    ds=0.005
    J=np.zeros((99,99))
    error=1
    while error >0.000000000000001:
        for i in range(len(F)):
            F[i]=sigma[i]-2.0*sigma[i+1]+sigma[i+2]+8.0*(ds**2.0)*sin(sigma[i+1])
            J[i][i]=-2.0+8.0*(ds**2.0)*cos(sigma[i+1])
            if i > 0:
                J[i][i-1]=1
            if i<98:
                J[i][i+1]=1
        x=np.linalg.solve(J,-1.0*F)
        for i in range(1,len(sigma)-1):
            sigma[i]=sigma[i]+x[i-1]
        error=np.amax(abs(x))
        roz=[Punkt(i*ds,x) for x,i in zip(sigma,range(len(sigma)))]
        yield  roz
        print(F)
    return F