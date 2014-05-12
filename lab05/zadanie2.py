__author__ = 'wemstar'
from constrant import *

def function2(t,u):
    return u*(u-1)*(u-2)





def zadanie2():
    start = -1.0
    end = 0.9
    u0 = 1.4
    dt = 1.0
    num = RK2(start, end, u0, dt, 0.000001, function2)
    with open("Zad2.txt", "w") as fp:
        for u in num:
            for x,y in zip(u.tabU1,u.tabU2):
                print(u.t,x,y)
    start=0
    end=8
    dt=0.4
    roz=[]
    for u0 in drange(0.0,2.0,0.2):
        num = RK2(start, end, u0, dt, 0.000001, function2)
        roz.append(num)
    for u,i in zip(roz,range(len(roz))):
        fileName="Zad2.{0}.txt".format(i)
        with open(fileName, "w") as fp:
            for x in u:
                fp.write("{0.t:0.20f} {0.u:0.20f}\n".format(x))

