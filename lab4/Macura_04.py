from subprocess import call
from math import exp, cos, sin, pi

__author__ = 'wemstar'


class PointZad2:
    X = float()
    V = float()
    DT = float()
    t = float()

    @property
    def x(self):
        return self.X

    @x.setter
    def x(self, value):
        self.X = value

    @property
    def v(self):
        return self.V

    @v.setter
    def v(self, value):
        self.V = value

    @property
    def e(self):
        return (self.X2 + self.V2) * 0.5

    @property
    def dt(self):
        return self.DT

    @dt.setter
    def dt(self, value):
        self.DT = value

    @property
    def V2(self):
        return self.v ** 2.0

    @property
    def X2(self):
        return self.x ** 2.0


def function1Zad1(t, u1, u2):
    return 98.0 * u1 + 198.0 * u2


def function2Zad1(t, u1, u2):
    return -99.0 * u1 - 199.0 * u2


def function1Zad2(t, u1, u2, dt):
    return -(u1 * (50.0 * (dt ** 2.0) - 297.0 * dt - 2) - 396.0 * u2 * dt) / (50.0 * (dt ** 2.0) + 101.0 * dt + 2.0)


def function2Zad2(t, u1, u2, dt):
    return -(198.0 * u1 * dt + u2 * (50.0 * (dt ** 2) + 297.0 * dt - 2.0)) / (50.0 * (dt ** 2.0) + 101.0 * dt + 2.0)


def function1Zad2Roz(t):
    return 2.0 * exp(-t) - exp(-100.0 * t)


def function2Zad2Roz(t):
    return exp(-100.0 * t) - exp(-t)


def function1Zad3(t, u):
    return -150.0 * (u + cos(t)) + sin(t)


def function2Zad3(t, u, dt):
    return (u - dt * (150.0 * cos(t + dt) - sin(t + dt))) / (1.0 + 150.0 * dt)


def iterateEquasion(method, function1, function2, start, end, dts, s, f10, f20, tol):
    p0 = PointZad2()
    p0.x = f10
    p0.v = f20
    p0.dt = dts

    pu = [p0]
    n = method.n
    t = start
    dt = dts
    while t < end:
        u11, u12 = method(function1, function2, t - 2.0*dt, pu[-1].x, pu[-1].v,  2.0*dt)
        u21, u22 = method(function1, function2, t - 2.0 * dt, pu[-1].x, pu[-1].v, dt)
        u21, u22 = method(function1, function2, t - dt, u21, u22, dt)

        e1 = error(u11, u21, n)
        e2 = error(u12, u22, n)
        er = max(e1, e2);
        dt *= ((s * tol) / (abs(er))) ** (1.0 / n)

        if er < tol:
            t +=  2.0*dt
            p = PointZad2()
            p.x = u21
            p.v = u22
            p.dt = dt
            p.t = t


            pu.append(p)
    return pu


def richardson(method, function, start, end, dts, s, y0, tol):
    p0 = PointZad2()
    p0.x = y0

    p0.dt = dts

    pu = [p0]
    n = method.n
    t = start
    dt = dts
    while t < end:
        u11 = method(function, t - 2.0*dt, pu[-1].x,  2.0*dt)
        u21 = method(function, t - 2.0* dt, pu[-1].x, dt)
        u21 = method(function, t - dt, u21, dt)

        er = error(u11, u21, n)

        dt *= ((s * tol) / (abs(er))) ** (1.0 / n)

        if er < tol:

            p = PointZad2()
            p.x = u21
            p.dt = dt
            p.t = t
            t += 2.0* dt

            pu.append(p)
    return pu


def error(u1, u2, n):
    return abs((u2 - u1) / (2.0 ** (n - 1.0) - 1.0))


def RK4(function1, function2, pt, pu1, pu2, dt):
    k11 = function1(pt, pu1, pu2)
    k21 = function2(pt, pu1, pu2)

    k12 = function1(pt + 0.5 * dt, pu1 + 0.5 * dt * k11, pu2 + 0.5 * dt * k21)
    k22 = function2(pt + 0.5 * dt, pu1 + 0.5 * dt * k11, pu2 + 0.5 * dt * k21)

    k13 = function1(pt + 0.5 * dt, pu1 + 0.5 * dt * k12, pu2 + 0.5 * dt * k22)
    k23 = function2(pt + 0.5 * dt, pu1 + 0.5 * dt * k12, pu2 + 0.5 * dt * k22)

    k14 = function1(pt + dt, pu1 + dt * k13, pu2 + dt * k23)
    k24 = function2(pt + dt, pu1 + dt * k13, pu2 + dt * k23)

    u1 = pu1 + dt / 6.0 * (k11 + 2.0 * k12 + 2.0 * k13 + k14)
    u2 = pu2 + dt / 6.0 * (k21 + 2.0 * k22 + 2.0 * k23 + k24)

    return u1, u2


def RK2Eauasion(function1, function2, pt, pu1, pu2, dt):
    k11 = function1(pt, pu1, pu2)
    k21 = function2(pt, pu1, pu2)

    k12 = function1(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    k22 = function2(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    u1 = pu1 + dt * 0.5 * k11 + dt * 0.5 * k12
    u2 = pu2 + dt * 0.5 * k21 + dt * 0.5 * k22
    return u1, u2


def trapezEquasion(function1, function2, pt, pu1, pu2, dt):
    u1 = function1(pt, pu1, pu2, dt)
    u2 = function2(pt, pu1, pu2, dt)
    return u1, u2


def simpleEuera(function, t, pu, dt):
    return pu + dt * function(t +dt, pu)


def complicatedEuera(function, t, pu, dt):
    return function(t, pu, dt)


def lab4Zadanie1():
    v0 = 0.0
    x0 = 1.0
    S = 0.75
    start = 0.0
    end = 100.0
    files = ("Zadanie1.1.txt", "Zadanie1.2.txt")
    methods = (RK2Eauasion, RK4)
    oscilation = ('0.02', '0.0278')
    for file, method, osc in zip(files, methods, oscilation):
        ru = iterateEquasion(method, function1Zad1, function2Zad1, start, end, 0.01, S, x0, v0, 0.00001)
        with open(file, "w") as fp:
            for u1 in ru:
                fp.write(
                    "{0.t:0.20f} {0.x:0.20f} {0.v:0.20f} {0.dt:0.20f} {1:0.20f} {2:0.20f} {3}\n".format(
                        u1, function1Zad2Roz(u1.t), function2Zad2Roz(u1.t), osc))


def lab4Zadanie2():
    x0 = 1.0
    v0 = 0.0
    S = 0.75
    start = 0.0
    end = 100.0
    files = ("Zadanie2.1.txt", "Zadanie2.2.txt")
    ru = iterateEquasion(trapezEquasion, function1Zad2, function2Zad2, start, end, 0.001, S, x0, v0, 0.00001)
    with open(files[1], "w") as fp:
        for u1 in ru[:-1]:
            fp.write(
                "{0.t:0.20f} {0.x:0.20f} {0.v:0.20f} {0.dt:0.20f} {0.e:0.20f} {0.X2:0.20f} {0.V2:0.20f} {1:0.20f} {2:0.20f}\n".format(
                    u1, function1Zad2Roz(u1.t), function2Zad2Roz(u1.t)))


def lab4Zadanie3():
    x0 = 0.0
    start = 0.0
    end = 3.0 / 2.0 * pi
    tols = (0.01, 0.001, 0.0001)
    filenames = ("Zadanie3.1.txt", "Zadanie3.2.txt", "Zadanie3.3.txt")
    for file, tol in zip(filenames, tols):
        numerycznie = richardson(simpleEuera, function1Zad3, start, end, 0.1, 0.75, x0, tol)
        with open(file, "w") as fp:
            for u1 in numerycznie:
                fp.write(
                    "{0.t:0.20f} {0.x:0.20f} {0.dt:0.20f} {1:0.20f}\n".format(
                        u1, -cos(u1.t)))

    filenames2 = ("Zadanie3.4.txt", "Zadanie3.5.txt", "Zadanie3.6.txt")
    for file, tol in zip(filenames2, tols):
        numerycznie2 = richardson(complicatedEuera, function2Zad3, start, end, 0.1, 0.75, x0, tol)
        with open(file, "w") as fp:
            for u1 in numerycznie2:
                fp.write(
                    "{0.t:0.20f} {0.x:0.20f} {0.dt:0.20f} {1:0.20f}\n".format(
                        u1, -cos(u1.t)))


def main():
    simpleEuera.n = 2.0
    RK2Eauasion.n = 3.0
    RK4.n = 5.0
    trapezEquasion.n = 3.0
    complicatedEuera.n = 3.0
    lab4Zadanie1()
    lab4Zadanie2()
    lab4Zadanie3()

    call(["gnuplot", "Macura_04.gpl"])


main()