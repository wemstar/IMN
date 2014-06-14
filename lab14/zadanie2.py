from math import exp
import utils
import numpy as np

def cykl1(v, u, a,t, dt, dx):
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]
    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0)
    v[:] += dt / 2.0 * a[:]


def cykl2(v, u, a,t, dt, dx):
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]
    a[1:75] = (u[2:76] + u[:74] - 2.0 * u[1:75]) / (dx ** 2.0)
    a[75:-1] = (u[76:] + u[74:-2] - 2.0 * u[75:-1]) / (dx ** 2.0) / 3.0
    v[:] += dt / 2.0 * a[:]


def zadanie2():
    u=np.zeros(101)
    for i, x in enumerate(u):
        u[i] = exp(-100.0*((i/100.0)-0.5)**2.0)
    utils.saveMatrix("Zadanie2a.txt", utils.methodGrid(cykl1,np.copy(u)))
    utils.saveMatrix("Zadanie2b.txt", utils.methodGrid(cykl2,np.copy(u)))