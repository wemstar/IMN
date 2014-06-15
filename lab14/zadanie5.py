from math import exp, cos, pi

__author__ = 'wemstar'
import utils
import numpy as np
def cykl(v, u, a,t, dt, dx):
    beta = cykl.beta
    baseForce=cykl.baseForce
    omega=cykl.omega
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]

    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0) - 2 * beta * v[1:-1]+cos(t*omega)*baseForce[1:-1]
    v[:] =v[:]+ dt / 2.0 * a[:]
def zadanie5():
    cykl.beta = 1.0
    baseForce=np.zeros(101)
    for i in range(len(baseForce)):
        baseForce[i]=exp(-100000*(i/100.0-0.5)**2.0)
    cykl.baseForce=baseForce
    u=np.zeros(101)
    omega=0.0
    b=[]
    while omega < 10.0*pi:
        cykl.omega=omega
        z=utils.method5(cykl,np.copy(u),40.0)
        b.append(z)
        omega+=0.1
    with open("Zadanie5.1.txt","w") as fp:
        for i,x in enumerate(b):
            fp.write("{0:0.20f} {1:0.20f}\n".format(i,x))
