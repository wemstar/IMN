from math import exp

__author__ = 'wemstar'

import utils
import numpy as np

def cykl(v, u, a,t, dt, dx):
    beta = cykl.beta
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]
    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0) - 2 * beta * v[1:-1]
    v[:] += dt / 2.0 * a[:]


def zadanie3():
    u=np.zeros(101)
    for i, x in enumerate(u):
        u[i] = exp(-100.0*((i/100.0)-0.5)**2.0)
    for beta in [0.2, 1.0, 3.0]:
        cykl.beta = beta
        z = utils.methodGrid(cykl,np.copy(u))
        utils.saveMatrix("Zadanie3.{0}.txt".format(beta), z)
