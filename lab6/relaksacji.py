from math import exp, pi

__author__ = 'wemstar'


class Point:
    def __init__(self, r, f):
        self.r = r
        self.f = f

    @property
    def error(self):
        return function1Roz(self.r)-self.f

    def __str__(self):
        return "{0.r:0.20f} {0.f:0.20f} {1:0.20f} {0.error:0.20f} \n".format(self, function1Roz(self.r))


def function1Roz(r):
    return exp(-r) * (0.125 * (r ** 3) + 0.25 * (r ** 2) + 0.75 * r + 1.0) - 1.0


def nr(r):
    return -exp(-r) / (32.0 * pi) * (r ** 2 - 4.0 * r + 4.0)





def srodkowy(plik, zbieznosc,iterator,dr=0.1):
    a = generateGrid(0.0, 35.0, dr, 0.0, -1.0)
    warunek = False
    error2 = 10
    while not warunek:
        iterator(a,dr)
        iterator(a,dr)
        iterator(a,dr)
        iterator(a,dr)

        error1 = abs(sumError(a, dr))
        error = abs(error1 - error2)
        if (error < zbieznosc):
            warunek = True
        else:
            warunek = False
        error2 = error1
    with open(plik, "w") as fp:
        for x in a:
            fp.write("{0}".format(x))


def generateGrid(start, end, dr, r0, rn):
    r = start
    grid = [Point(start, r0)]
    while r < (end - dr):
        r += dr
        grid.append(Point(r, 0))
    grid.append(Point(end, rn))
    return grid


def sumError(a, dr):
    suma = 0.0
    for i in range(1, len(a) - 1):
        pierwszy = 0.5 * ((a[i + 1].f - a[i - 1].f) / (2.0 * dr)) ** 2.0
        drugi = 4.0 * pi * a[i].r * nr(a[i].r) * a[i].f
        suma += (pierwszy - drugi) * dr
    return suma
