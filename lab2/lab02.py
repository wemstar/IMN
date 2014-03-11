from math import exp

__author__ = 'wemstar'

#metody numeryczne
def simpleEuera(function, ran, dt, t0):
    u = [t0]
    for t in ran:
        pu = u[-1]
        u.append(pu + dt * function(t, pu, dt))
    return u


def complicateEuera(function, ran, dt, t0):
    u = [t0]
    for t in ran:
        pu = u[-1]
        u.append(pu + dt * function(t + dt, pu, dt))
    return u


def complicateEuera2(function, ran, dt, t0):
    u = [t0]
    for t in ran:
        pu = u[-1]
        u.append(function(t + dt, pu, dt))
    return u


def iterationEuelera(function, ran, dt, t0):
    u = [t0]
    for x in ran:
        u.append(t0 + function(0.01, u[-1], 0.01) * 0.01)
    return u

def newton(function,ran,dt,t0,n):
    u = [t0]
    umi=[t0]
    for x in ran:
        u.append(t0 + function(0.01, u[-1], 0.01) * 0.01)
    return u


def trapez(function, ran, dt, t0):
    u = [t0]
    for t in ran:
        pu = u[len(u) - 1]
        u.append(pu + dt * (function(t + dt, pu, dt) + function(t, u, dt)) / 2.0)
    return u


#równania różniczkowe
def function1(t, u, dt):
    return 32 * t - 4


def function2(t, u, dt):
    return -8 * (u - 16 * t ** 2 - 7)


def function3(t, u, dt):
    return (u + 128 * (t ** 2) * dt + 56 * dt) / (1 + 8 * dt)


#rozwiązanie funkcji
def function1Roz(t, u):
    return 16 * t ** 2 - 4 * t + 7.5


def function2Roz(t, u):
    return 2 * exp(-8 * t) + 16 * t ** 2 - 4 * t + 7.5


def lab02Z1(fileName, method, function, functionRoz, start, end, dt, u0):
    with open(fileName, "w") as file1:
        ran = drange(start, end, dt)
        u = method(function, ran, dt, u0)
        dok = [functionRoz(t, 0) for t in ran]
        for x, y, z in zip(ran, u, dok):
            file1.write("{0} {1} {2} {3}\n".format(x, y, z, z - y))

def lab02Z4(fileName,method,function,functionRoz,dt,u0,n):
    with open(fileName, "w") as file1:
        ran = range(0,n)
        u = method(function, ran, dt, u0)
        dok = [functionRoz(dt, 0) for t in ran]
        for x, y, z in zip(ran, u, dok):
            file1.write("{0} {1} {2} {3}\n".format(x, y, z, z - y))



def drange(start, stop, step):
    a = []
    r = start
    while r <= stop:
        a.append(r)
        r += step
    return a


def main():
    # Zadanie 1
    methodList = (simpleEuera, complicateEuera, trapez)
    fileNames = ("File1", "File2", "File3")
    for file, method in zip(fileNames, methodList):
        lab02Z1(file, method, function1, function1Roz, 0, 60, 1.5, 7.5)

    # Zadanie 2
    fileNames2 = ("File4", "File5", "File6", "File7")
    steps = (0.01, 0.1, 0.25, 0.27)

    for file, step in zip(fileNames2, steps):
        lab02Z1(file, simpleEuera, function2, function2Roz, 0, 10, step, 9.5)

    # Zadanie 3
    fileNames3 = ("File8", "File9", "File10", "File11", "File12")
    steps3 = (0.01, 0.1, 0.25, 0.27, 1.33)
    for file, step in zip(fileNames3, steps3):
        lab02Z1(file, complicateEuera2, function3, function2Roz, 0, 10, step, 9.5)
    #Zadanie 4
    lab02Z4("File13", iterationEuelera, function2, function2Roz, 0.01, 9.5,5)


main()
