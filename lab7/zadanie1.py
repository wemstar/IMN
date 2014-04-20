__author__ = 'dom'


class Potencja:
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


def V(x):
    return 0.5 * (x ** 2.0)


def g(x, E):
    return -2.0 * (-V(x) + E)


def rozwiaz(L, dx):
    E = [x * 0.01 for x in range(0, 500)]
    roz = []

    for i in range(len(E)):
        x = -L
        p = [Potencja(x, 0, E[i])]
        p.append(Potencja(x + dx, 1.948525 * (10.0 ** -5.0), E[i]))
        x += 2.0 * dx
        while x <= L:
            pierwszy = 2.0 * (12.0 - 5.0 * (dx ** 2.0) * g(p[-1].x, E[i]) )* p[-1].mi
            drugi = (12.0 + dx ** 2.0 * g(p[-2].x, E[i]) )* p[-2].mi
            trzeci = 12.0 + (dx ** 2) * g(x, E[i])
            po = Potencja(x, (pierwszy - drugi) / trzeci, E[i])
            p.append(po)
            x += dx
        roz.append(p[-1])
    return roz