from math import sin, pi, cos, exp

__author__ = 'wemstar'

import numpy as np


def initial(v, u, a):
    v[0] = 0
    v[-1] = 0
    u[0] = 0
    u[-1] = 0
    a[0] = 0
    a[-1] = 0


def cykl(v, u, a, dt, dx,beta):
    initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]
    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0) - 2*beta * v[1:-1]
    v[:] += dt / 2.0 * a[:]



def method(beta):
    v = np.zeros(101)
    u = np.zeros(101)
    a = np.zeros(101)
    for i, x in enumerate(u):
        u[i] = exp(-100.0*((i/100.0)-0.5)**2.0)

    t = 0.0
    dt = 1.0 / 200.0
    wynik=[np.copy(u)]
    while t < 4.0:
        cykl(v, u, a, dt, 0.01,beta)
        t += dt
        wynik.append(np.copy(u))

    return wynik
def analityczny(x,t):
    return cos(pi*t)*sin(pi*x)-0.5*cos(2.0*pi*t)*sin(2.0*pi*x)


def zadanie3():
    for beta in [0.2,1.0,3.0]:
        u=method(beta)
        with open("Zadanie3.{0}.txt".format(beta),"w") as fp:
            for i in range(len(u)):
                for j in range(len(u[i])):
                    fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i/200.0,j/100.0,round(u[i][j],3)))
                fp.write("\n")
