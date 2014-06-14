from math import exp, cos, pi

__author__ = 'wemstar'
import utils
import numpy as np
def cykl(v, u, a,t, dt, dx):
    beta = cykl.beta
    baseForce=cykl.baseForce
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]

    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0) - 2 * beta * v[1:-1]+cos(t*pi/2.0)*baseForce[1:-1]
    v[:] += dt / 2.0 * a[:]
def zadanie4():
    cykl.beta = 1.0
    baseForce=np.zeros(101)
    for i in range(len(baseForce)):
        baseForce[i]=exp(-100000*(i/100.0-0.5)**2.0)
    cykl.baseForce=baseForce
    u=np.zeros(101)
    u = utils.methodGrid(cykl,u,10.0)
    utils.saveMatrix("Zadanie4.txt", u)
