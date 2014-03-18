from math import exp

__author__ = 'wemstar'


def simpleEuera(function, pu, t, dt):
    return pu + dt * function(t, pu)


def RK2(function, pu, t, dt):
    k1 = function(t, pu)
    k2 = function(t + dt, pu + dt * k1)
    return pu + 0.5 * dt * (k1 + k2)


def iterate(method, function, ran, dt, y0):
    y = [y0]
    for t in ran:
        y.append(method(function, y[-1], t, dt))
    return y
def richardson(method,function,ran,dt,y0,n):
    y=[y0]
    for t in ran:
        y1=method(function,y[-1],t+2*dt,2*dt)
        y2=method(function,y[-1],t+dt,dt)
        y2=method(function,y2,t+2*dt,dt)
        y.append(y2+(y2-y1)/(2**(n-1)-1))
    return y


def function1(t, y):
    return 0.5 * y + 1 / 4 * t + 1 / 2


def function1Roz(t):
    return exp(t / 2) - t / 2 - 2


def lab3Zadanie1():
    dt = 0.05;
    ran1 = drange(0, 10, dt)
    ran2 = drange(0, 10, 2 * dt)
    euera1 = iterate(simpleEuera, function1, ran1, dt, -1)
    rk1 = iterate(RK2, function1, ran1, dt, -1)
    dok1 = [function1Roz(t) for t in ran1]
    with open("Zadanie1a.txt", "w") as fp:
        for t, e, r, d in zip(ran1, euera1, rk1, dok1):
            fp.write("{0:0.12f} {1:0.12f} {2:0.12f}\n".format(t, abs(d - e), abs(r - d)))
    euera2=richardson(simpleEuera,function1,ran2,dt,-1,2)
    rk2=richardson(RK2,function1,ran2,dt,-1,3)
    dok2 = [function1Roz(t) for t in ran2]
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
    lab3Zadanie1()


main()