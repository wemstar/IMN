__author__ = 'wemstar'
from relaksacji import *

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


def RK2Eauasion(pt, pu1, pu2, dt):
    k11 = function1(pt, pu1, pu2)
    k21 = function2(pt, pu1, pu2)

    k12 = function1(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    k22 = function2(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    u1 = pu1 + dt *0.5 * k11 + dt*0.5 * k12
    u2 = pu2 + dt *0.5 * k21 + dt*0.5 * k22
    return u1, u2



def iterateEquasion(start, end, dts,f10, f20):

    p0 = PointZad2()
    p0.x = f10
    p0.v = f20
    p0.dt = dts

    pu = [p0]

    t = start
    dt = dts
    while t > end:
        u11, u12 = RK2Eauasion(t, pu[-1].x, pu[-1].v, dt)
      

        t += dt
        p = PointZad2()
        p.x = u11
        p.V = u12
        p.dt = dt 
        p.t = t
        pu.append(p)
    return pu

def function1(pt,pu1,pu2):
    return pu2
def function2(pt,pu1,pu2):
    return -4.0 * pi * pt * nr(pt)

def error(u1, u2, n):
    return abs((u2 - u1) / (2.0 ** (n - 1.0) - 1.0))

def zadanie6():
    roz=iterateEquasion(35,0,-0.1,-1.0,0.0)
    with open("Zadanie6.txt", "w") as fp:
        for u1 in roz[1:-1]:
            fp.write("{0.t:0.20f} {0.x:0.20f} {0.v:0.20f} {1:0.20f} {2:0.20f} \n".format(u1,function1Roz(u1.t),function1Roz(u1.t)-u1.x))

