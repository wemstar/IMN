from math import cos, pi, sin, exp
import numpy as np
__author__ = 'wemstar'


def saveMatrix(filename, u):
    with open(filename, "w") as fp:
        for i in range(len(u)):
            for j in range(len(u[i])):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i / 200.0, j / 100.0, u[i][j]))
            fp.write("\n")

def analityczny(x,t):
    return cos(pi*t)*sin(pi*x)-0.5*cos(2.0*pi*t)*sin(2.0*pi*x)

def initial(v, u, a):
    v[0] = 0
    v[-1] = 0
    u[0] = 0
    u[-1] = 0
    a[0] = 0
    a[-1] = 0
def init(u):
    for i in range(len(u)):
        u[i] = exp(-100.0*((i/100.0)-0.5)**2.0)
def methodGrid(cykl,u,endT=4.0):
    v = np.zeros(101)

    a = np.zeros(101)


    t = 0.0
    dt = 1.0 / 200.0
    wynik=[np.copy(u)]
    while t < endT:
        cykl(v, u, a,t, dt, 0.01)
        t += dt
        wynik.append(np.copy(u))
    return wynik
