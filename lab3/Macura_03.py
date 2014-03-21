from math import exp, pi
from subprocess import call
__author__ = 'wemstar'


def simpleEuera(function, pu, t, dt):
    return pu + dt * function(t, pu)


def RK2(function, pu, t, dt):
    k1 = function(t,pu)
    k2 = function(t+dt, pu + dt * k1)
    return pu + 0.5 * dt * (k1 + k2)


def iterate(method, function, ran, dt, y0):
    y = [y0]
    for t in ran:
        y.append(method(function, y[-1], t, dt))
    return y


def iterateEquasion(method, function1, function2, start, end, dts, s, f10, f20, tol):
    pu1 = [f10]
    pu2 = [f20]
    t = start
    dt=dts
    while t < end:
        u11, u12 = method(function1, function2, t+dt , pu1[-1], pu2[-1],  dt)
        u21, u22 = method(function1, function2, t +0.5*dt, pu1[-1], pu2[-1],  0.5*dt)
        u21, u22 = method(function1, function2, t +dt, u21, u22,  0.5*dt)

        e1=error(u11,u21,3)
        e2=error(u12,u22,3)
        er=max(e1,e2);
        dt=((s*tol)/(abs(er)))**(1/3)*dt


        if(er<tol):
            t +=  dt
            pu1.append(u21)
            pu2.append(u22)
    return pu1, pu2


def lab3Zadanie2():
    v0 = 1
    x0 = 0
    S = 0.75
    start = 0.0
    end = 24.0
    tols = (10.0 ** (-1), 10.0 ** (-4), 10.0 ** (-6))
    ru1, ru2 = iterateEquasion(RK2Eauasion, function1Zad2, function2Zad2, start, end, 0.001, S, x0, v0, tols[0])
    with open("Zadanie2.txt", "w") as fp:
        for u1, u2 in zip(ru1, ru2):
            fp.write("{0:0.12f} {1:0.12f}\n".format(u1, u2))


def richardson(method, function, ran, dt, y0):
    y = [y0]
    n = method.n
    for t in ran:
        y1 = method(function, y[-1], t +dt, dt)
        y2 = method(function, y[-1], t +0.5*dt, 0.5*dt)
        y2 = method(function, y2, t+dt, 0.5*dt)
        y.append(y2 + error(y1, y2, n))
    return y


def error(u1, u2, n):
    return abs((u2 - u1) / (2 ** (n - 1) - 1))


def RK2Eauasion(function1, function2, pt, pu1, pu2, dt):
    k11 = function1(pt, pu1, pu2)
    k21 = function2(pt, pu1, pu2)

    k12 = function1(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    k22 = function2(pt + dt, pu1 + dt * k11, pu2 + dt * k21)

    u1 = pu1 + dt / 2.0 * k11 + dt / 2.0 * k12
    u2 = pu2 + dt / 2.0 * k21 + dt / 2.0 * k22
    return u1, u2


def functionZad1(t, y):
    return 0.5 * y + 0.25 * t + 0.5


def functionZad1Roz(t):
    return exp(t / 2.0) - t / 2.0 - 2.0


def function1Zad2(t, u1, u2):
    return 8.0 / 24.0 * pi * u2


def function2Zad2(t, u1, u2):
    return -8.0 / 24.0 * pi * u1


def lab3Zadanie1():
    dt = 0.05;
    ran1 = drange(0, 10, dt)
    ran2 = drange(0, 10, 2 * dt)
    euera1 = iterate(simpleEuera, functionZad1, ran1, dt, -1)
    rk1 = iterate(RK2, functionZad1, ran1, dt, -1)
    dok1 = [functionZad1Roz(t) for t in ran1]
    with open("Zadanie1a.txt", "w") as fp:
        for t, e, r, d in zip(ran1, euera1, rk1, dok1):
            fp.write("{0:0.12f} {1:0.12f} {2:0.12f}\n".format(t, abs(d - e), abs(r - d)))
    euera2 = richardson(simpleEuera, functionZad1, ran2, 2*dt, -1)
    rk2 = richardson(RK2, functionZad1, ran2, 2*dt, -1)
    dok2 = [functionZad1Roz(t) for t in ran2]
    with open("Zadanie1b.txt", "w") as fp:
        for t, e, r, d in zip(ran2, euera2, rk2, dok2):
            fp.write("{0:0.12f} {1:0.12f} {2:0.12f}\n".format(t, abs(d - e), abs(r - d)))


def drange(start, stop, step):
    a = []
    r = start
    while r <= stop:
        a.append(r)
        r += step
    return a


def main():
    simpleEuera.n = 2
    RK2.n = 3
    lab3Zadanie1()
    lab3Zadanie2()
    call(["gnuplot","Macura_03.gpl"])


main()