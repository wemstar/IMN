from math import exp

__author__ = 'wemstar'
import numpy as np
from lab5.constrant import *

class Point4:
    def __init__(self,t,dt,u,v):
        self.t=t
        self.dt=dt
        self.u=u
        self.v=v


def function1(u, v):
    return 98.0 * u + 198.0 * v


def function2(u, v):
    return -99.0 * u - 199.0 * v

def function1Roz(t):
    return 2.0*exp(-1.0*t)-exp(-100.0*t)
def function2Roz(t):
    return exp(-100.0*t)-exp(-1.0*t)

def RK4(pu, pv, dt):
    A = np.array([[1.0 - 98.0 * a11 * dt, -198.0 * a11 * dt, -98.0 * a12 * dt,-198.0*a12*dt],
                  [99.0 * a11 * dt, 1.0 + 199.0 * a11 * dt, 99.0 * a12 * dt, 199.0 * a12 * dt],
                  [-98.0 * a21 * dt, -198.0 * a21 * dt, 1.0 - 98.0 * a22*dt, -198.0 * a22 * dt],
                  [99.0 * a21 * dt, 199.0 * a21 * dt, 99.0 * a22 * dt, 1.0 + 199.0 * a22 * dt]])
    B=np.array([pu,pv,pu,pv])
    x = np.linalg.solve(A, B)
    Uu1=x[0]
    Uv1=x[1]
    Uu2=x[2]
    Uv2=x[3]
    u=pu+dt*0.5*(function1(Uu1,Uv1)+function1(Uu2,Uv2))
    v=pv+dt*0.5*(function2(Uu1,Uv1)+function2(Uu2,Uv2))
    return u,v


def richardson(start,end,dts,u0,v0):

    n = 5.0
    dt = dts
    tol=0.00001
    t = start;
    s=0.75
    p0 = Point4(start,dts,u0,v0)
    y=[p0]
    while t < end:
        u1,v1 = RK4(y[-1].u,y[-1].v, dt)
        u2,v2 = RK4(y[-1].u,y[-1].v, 0.5*dt)
        u2,v2 = RK4(u2,v2, 0.5*dt)
        er1=error(u1,u2,n)
        er2=error(v1,v2,n)
        er=max(er1,er2)
        dt *= ((s * tol) / abs(er)) ** (1.0 / n)
        if er < tol:

            p = Point4(t,dt,u2,v2)
            t+=dt
            y.append(p)

    return y

def normal(start,end,dts,u0,v0):
    t = start;

    dt = dts

    p0 = Point4(start,dts,u0,v0)
    y=[p0]
    while t < end:
        u1,v1 = RK4(y[-1].u,y[-1].v, dt)


        t+=dt
        p = Point4(t,dt,u1,v1)
        y.append(p)

    return y

def error(u1, u2, n):
    return abs((u1 - u2))/(2.0**(n-1.0)-1.0)

def zadanie3():
    y=richardson(0.0,100.0,100.0,1,0)
    rozu=[]
    with open("Zad3.txt","w") as fp:
        for x in y:
            fp.write("{0.t:0.20f} {0.dt:0.20f} {0.u:0.20f} {0.v:0.20f} {1:0.20f} {2:0.20f}\n".format(x,function1Roz(x.t),function2Roz(x.t)))
