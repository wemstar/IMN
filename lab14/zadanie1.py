from math import sin, pi, cos
import utils
__author__ = 'wemstar'

import numpy as np



def cykl(v, u, a, dt, dx):
    utils.initial(v, u, a)
    v[:] = v[:] + dt / 2.0 * a[:]
    u[:] = u[:] + dt * v[:]
    a[1:-1] = (u[2:] + u[:-2] - 2.0 * u[1:-1]) / (dx ** 2.0)
    v[:] += dt / 2.0 * a[:]


def method(steps):
    v = np.zeros(101)
    u = np.zeros(101)
    a = np.zeros(101)
    for i, x in enumerate(u):
        u[i] = analityczny(i/100.0,0.0)

    t = 0.0
    dt = 1.0 / 200.0
    while t < 2.0:
        cykl(v, u, a, dt, 0.01)
        if round(t,4) in steps:
            yield u
        t += dt
def analityczny(x,t):
    return cos(pi*t)*sin(pi*x)-0.5*cos(2.0*pi*t)*sin(2.0*pi*x)


def zadanie1():
    time=[0.0,0.25,0.5,0.75,1.0,1.25,1.50,1.75,2.0]
    for i,w in enumerate(method(time)):
        with open("Zadanie1.{0}.txt".format(i),"w") as fp:
            for x,u in enumerate(w):
                fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(x/100.0,u,analityczny(x/100.0,time[i])))