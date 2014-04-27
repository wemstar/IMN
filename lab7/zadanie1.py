from math import exp, pi

__author__ = 'dom'


class Point:
    def __init__(self, x, mi, E):
        self.x = x
        self.mi = mi
        self.E = E

    def __str__(self):
        return "{0.x:0.20f} {0.mi:0.20f} {0.E:0.20f}\n".format(self)


def zadanie1():
    roz = rozwiaz(4.0, 0.01)
    with open("Zadanie1.txt", "w") as fp:
        for r in roz:
            fp.write("{0}".format(r))
    roz = rozwiaz2(4.0, 0.01)
    with open("Zadanie1.2.txt", "w") as fp:
        for r in roz:
            fp.write("{0}".format(r))


def V(x):
    return 0.5 * (x ** 2.0)


def g(x, E):
    return 2.0 * (-V(x) + E)





def rozwiaz(L, dx):
    E = [x * 0.01 for x in range(0, 500)]
    roz = []

    for i in range(len(E)):
        pu2 = numerowa(L, dx, E[i])
        roz.append(Point(L, pu2[-1], E[i]))
    return roz


def numerowa(L, dx, E):
    x = -L

    p=[0.0,1.948525 * (10.0 ** -5.0)]
    x += 2.0 * dx
    while x <= L:
        pierwszy = 2.0 * (12.0 - 5.0 * (dx ** 2.0) * g(x - dx, E) ) * p[-1]
        drugi = (12.0 + dx ** 2.0 * g(x - 2.0 * dx, E) ) * p[-2]
        trzeci = 12.0 + (dx ** 2) * g(x, E)

        p.append((pierwszy - drugi) / trzeci)
        x += dx
    return p

def rozwiaz2(L, dx):
    e0=0.0
    e1=0.3
    p0=numerowa(L,dx,e0)[-1]
    while abs(p0) > 0.0000000001:
        p1=numerowa(L,dx,e1)[-1]
        e2 =e1- (p1*(e1 - e0)) / (p1 - p0)
        p0=p1
        e0=e1
        e1=e2
    print(e1)
    roz=[]
    p=numerowa(L,dx,e1)
    x=-L
    for el in p:
        roz.append(Point(x,el,analityczne(x)))
        x+=dx
    return roz

def analityczne(x):
    return exp(-0.5*(x**2.0))/pow(pi,0.25);


