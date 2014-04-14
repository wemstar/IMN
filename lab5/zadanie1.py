__author__ = 'wemstar'

from constrant import *



def zadanie1():
    start = 0.0
    end = 10
    u0 = 0.0
    dt = 0.1
    num = RK2(start, end, u0, dt, 0.000001, function1)
    t = drange(start, end,dt)
    dok = [function1Roz(x) for x in t]
    with open("Zad1.txt", "w") as fp:
        for t, n, d in zip(t, num, dok):
            fp.write("{0:0.20f} {1.u:0.20f} {2:0.20f} {3:0.20f} {4:0.20f} {5:0.20f}\n".format(t, n, d,n.u-d,n.u1-d,n.u2-d))


def function1(t, u):
    return 4 * (t ** 3)


def function1Roz(t):
    return t ** 4


