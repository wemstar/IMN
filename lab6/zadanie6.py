__author__ = 'wemstar'
from relaksacji import *
def RK2Eauasion(function1, function2, pt, pu1, pu2, dt):
    k11 = function1(pt, pu1, pu2)
    k21 = function2(pt, pu1, pu2)

    k12 = function1(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    k22 = function2(pt + dt, pu1 + dt * k11, pu2 + dt * k21)
    u1 = pu1 + dt *0.5 * k11 + dt*0.5 * k12
    u2 = pu2 + dt *0.5 * k21 + dt*0.5 * k22
    return u1, u2



def iterateEquasion(method, function1, function2, start, end, dts, s, f10, f20, tol):

    pu = [p0]
    n = method.n
    t = start
    dt = dts
    while t < end:
        u11, u12 = method(function1, function2, t + dt, pu[-1].x, pu[-1].v, dt)
        u21, u22 = method(function1, function2, t + 0.5 * dt, pu[-1].x, pu[-1].v, 0.5 * dt)
        u21, u22 = method(function1, function2, t + dt, u21, u22, 0.5 * dt)

        e1 = error(u11, u21, n)
        e2 = error(u12, u22, n)
        er = max(e1, e2);


        if er < tol:

            pu.append(p)
        dt *= ((s * tol) / (abs(er))) ** (1.0 / n)
    return pu

def error(u1, u2, n):
    return abs((u2 - u1) / (2.0 ** (n - 1.0) - 1.0))