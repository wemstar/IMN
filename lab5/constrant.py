from math import sqrt
import numpy as np
__author__ = 'wemstar'
a11 = 1.0 / 4.0
a12 = 1.0 / 4.0 - sqrt(3.0) / 6.0
a21 = 1.0 / 4.0 + sqrt(3.0) / 6.0
a22 = 1.0 / 4.0

b1 = 1.0 / 2.0
b2 = 1.0 / 2.0

c1 = 1.0 / 2.0 - sqrt(3.0) / 6.0
c2 = 1.0 / 2.0 + sqrt(3.0) / 6.0

def drange(start, stop, step):
    a = []
    r = start
    while r <= stop:
        a.append(r)
        r += step
    return a

def pochodna(function, t, u):
    du=0.001
    return (function(t, u + du) - function(t, u - du)) / (2 * du)

def F1(U1, U2, pu, pt, dt, function):
    return U1 - pu - dt * (a11 * function(pt + c1 * dt, U1) + a12 * function(pt + c2 * dt, U2))


def F2(U1, U2, pu, pt, dt, function):
    return U2 - pu - dt * (a21 * function(pt + c1 * dt, U1) + a22 * function(pt + c2 * dt, U2))


def RK2(start, end, u0, dt, du, function):
    t = start
    u = [Point(t,u0,u0,u0,[u0],[u0])]
    while t < end:
        u1 = u[-1].u
        u2 = u[-1].u
        tabU1=[u1]
        tabU2=[u2]
        error = 1000000000000
        while error > du:
            A11 = 1.0 - dt * a11 * pochodna(function,u[-1].t + dt * c1, u1)
            A12 = 0.0 - dt * a12 * pochodna(function,u[-1].t + dt * c2, u2)
            A21 = 0.0 - dt * a21 * pochodna(function,u[-1].t + dt * c1, u1)
            A22 = 1.0 - dt * a22 * pochodna(function,u[-1].t + dt * c2, u2)
            A = np.array([[A11, A12], [A21, A22]])
            B = np.array([-F1(u1, u2, u[-1].u, u[-1].t, dt, function), -F2(u1, u2, u[-1].u, u[-1].t, dt, function)])
            x = np.linalg.solve(A, B)
            error = max(abs(x[0]), abs(x[1]))
            u1 += x[0]
            u2 += x[1]
            tabU1.append(u1)
            tabU2.append(u2)
        newU=u[-1].u + dt * (b1 * function(t + c1 * dt, u1) + b2 * function(t + c2 * dt, u2))
        t += dt
        u.append(Point(t,newU,u1,u2,tabU1,tabU2))

    return u


class Point:
    def __init__(self,t,u,u1,u2,tabU1,tabU2):
        self.t=t
        self.u=u
        self.u1=u1
        self.u2=u2
        self.tabU1=tabU1
        self.tabU2=tabU2
