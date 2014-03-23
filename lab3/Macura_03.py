from math import exp, pi
from subprocess import call

__author__ = 'wemstar'
class PointZad2:
    X=float()
    V=float()
    DT=float()
    t=float()
    @property
    def x(self):
        return self.X
    @x.setter
    def x(self,value):
        self.X=value
    @property
    def v(self):
        return self.V
    @v.setter
    def v(self,value):
        self.V=value
    @property
    def e(self):
        return (self.X2+self.V2)*0.5
    @property
    def dt(self):
        return self.DT
    @dt.setter
    def dt(self,value):
        self.DT=value
    @property
    def V2(self):
        return self.v**2
    @property
    def X2(self):
        return self.x**2


def simpleEuera(function, pu, t, dt):
    return pu + dt * function(t-dt, pu)


def RK2(function, pu, t, dt):
    k1 = function(t-dt,pu)
    k2 = function(t, pu + dt * k1)
    return pu + 0.5 * dt * (k1 + k2)
def RK4(function1, function2, pt, pu1, pu2, dt):
    k11=function1(pt,pu1,pu2)
    k21=function2(pt,pu1,pu2)

    k12=function1(pt+0.5*dt,pu1+0.5*dt*k11,pu2+0.5*dt*k21)
    k22=function2(pt+0.5*dt,pu1+0.5*dt*k11,pu2+0.5*dt*k21)

    k13=function1(pt+0.5*dt,pu1+0.5*dt*k12,pu2+0.5*dt*k22)
    k23=function2(pt+0.5*dt,pu1+0.5*dt*k12,pu2+0.5*dt*k22)

    k14=function1(pt+dt,pu1+dt*k13,pu2+dt*k23)
    k24=function2(pt+dt,pu1+dt*k13,pu2+dt*k23)

    u1=pu1+dt/6.0*(k11+2.0*k12+2.0*k13+k14)
    u2=pu2+dt/6.0*(k21+2.0*k22+2.0*k23+k24)

    return u1,u2




def iterate(method, function, ran, dt, y0):
    y = [y0]
    for t in ran:
        y.append(method(function, y[-1], t+dt, dt))
    return y


def iterateEquasion(method, function1, function2, start, end, dts, s, f10, f20, tol):
    p0=PointZad2()
    p0.x=f10
    p0.v=f20
    p0.dt=dts

    pu = [p0]
    n=method.n
    t = start
    dt=dts
    while t < end:
        u11, u12 = method(function1, function2, t+dt , pu[-1].x, pu[-1].V,  dt)
        u21, u22 = method(function1, function2, t +0.5*dt, pu[-1].x, pu[-1].v,  0.5*dt)
        u21, u22 = method(function1, function2, t +dt, u21, u22,  0.5*dt)

        e1=error(u11,u21,n)
        e2=error(u12,u22,n)
        er=max(e1,e2);
        dt *= ((s * tol) / (abs(er))) ** (1 / n)


        if(er<tol):
            t +=  dt
            p=PointZad2()
            p.x=u21
            p.V=u22
            p.dt=dt/2.0
            p.t=t
            pu.append(p)
    return pu


def lab3Zadanie2():
    v0 = 1
    x0 = 0
    S = 0.75
    start = 0.0
    end = 24.0
    tols = (10.0 ** (-1), 10.0 ** (-4), 10.0 ** (-6))
    files=("Zadanie2.txt","Zadanie2.1.txt","Zadanie2.2.txt")
    for file,tol in zip(files,tols):
        ru= iterateEquasion(RK2Eauasion, function1Zad2, function2Zad2, start, end, 0.001, S, x0, v0, tol)
        with open(file, "w") as fp:
            for u1 in ru:
                fp.write("{0.X:0.12f} {0.V:0.12f} {0.e:0.12f} {0.DT:0.12f} {0.t:0.12f} {0.X2:0.12f} {0.V2:0.12f}\n".format(u1))

def lab3Zadanie3():
    v0 = 1
    x0 = 0
    S = 0.75
    start = 0.0
    end = 24.0
    tols = (10.0 ** (-1), 10.0 ** (-4), 10.0 ** (-6))
    files=("Zadanie3.1.txt","Zadanie3.2.txt","Zadanie3.3.txt")
    for file,tol in zip(files,tols):
        ru= iterateEquasion(RK4, function1Zad2, function2Zad2, start, end, 0.01, S, x0, v0, tol)
        with open(file, "w") as fp:
            for u1 in ru:
                fp.write("{0.X:0.12f} {0.V:0.12f} {0.e:0.12f} {0.DT:0.12f} {0.t:0.12f} {0.X2:0.12f} {0.V2:0.12f}\n".format(u1))


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
    RK2Eauasion.n=3
    RK4.n=5
    lab3Zadanie1()
    lab3Zadanie2()
    lab3Zadanie3()
    call(["gnuplot","Macura_03.gpl"])


main()