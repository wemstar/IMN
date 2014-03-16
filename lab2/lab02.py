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
        u.append(t0 + function(dt, u[-1], dt) * dt)
    return u


def newton(function, ran, dt, t0, n):
    u = [t0]
    umi = [t0]
    for x in ran:
        u.append(t0 + function(0.01, u[-1], 0.01) * 0.01)
    return u


def trapez(function, ran, dt, t0):
    u = [t0]
    for t in ran:
        pu = u[len(u) - 1]
        u.append(pu + dt * (function(t + dt, pu, dt) + function(t, u, dt)) / 2.0)
    return u


def newtonIter(function, ran, dt, t0):
    u = [t0]
    umi = [t0]
    for x in ran:
        u.append(u[-1] - (u[-1] - t0 - dt * function(dt, u[-1], dt)) / (1 - pochodna1(function, dt, u[-1], dt, 0.1)))
    return u

def newtonIter3(function, ran, dt, t0):
    u = [t0]
    umi = [t0]
    for x in ran:
        u.append(u[-1] - (u[-1] - t0 - dt * function(dt, u[-1], dt)) / (1 - pochodna2(function, dt, u[-1], dt, 0.1)))
    return u


def newtonIter2(function, ran, dt, t0, n, du):
    u = [t0]
    for x in ran:
        umi = [t0]
        for b in range(0, n):
            umi.append(
                umi[-1] - (umi[-1] - u[-1] - dt / 2 * (function(x + dt, umi[-1], dt) + function(x, u[-1], dt))) / (
                    1 - dt / 2 * pochodna2(function, x, u[-1], dt, du)))
        u.append(umi[-1])
    return u


def pochodna1(function, t, u, dt, du):
    return (function(t, u + du, dt) - function(t, u, dt)) / du


def pochodna2(function, t, u, dt, du):
    return (function(t, u + du, dt) - function(t, u - du, dt)) / (2 * du)


#równania różniczkowe
def function1(t, u, dt):
    return 32 * t - 4


def function2(t, u, dt):
    return -8 * (u - 16 * t ** 2 - 7)


def function3(t, u, dt):
    return (u + 128 * (t ** 2) * dt + 56 * dt) / (1 + 8 * dt)


def function6(t, u, dt):
    return u * (u - 1) * (u - 2)


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


def lab02Z4(fileName, method, function, functionRoz, dt, u0, n):
    with open(fileName, "w") as file1:
        ran = range(0, n)
        u = method(function, ran, dt, u0)
        dok = [functionRoz(dt, 0) for t in ran]
        for x, y, z in zip(ran, u, dok):
            file1.write("{0} {1} {2} {3}\n".format(x, y, z, z - y))


def lab02Z8(fileName, method, function, functionRoz, start, koniec, krok, u0, iloscIteracji, du):
    with open(fileName, "w") as fp:
        ran = drange(start, koniec, krok)
        u = method(function, ran, krok, u0, iloscIteracji, du)
        dok = [functionRoz(t, 0) for t in ran]
        for x, y, z in zip(ran, u, dok):
            fp.write("{0} {1} {2} {3}\n".format(x, y, z, z - y))


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
    fileNames = ("File1.txt", "File2.txt", "File3.txt")
    for file, method in zip(fileNames, methodList):
        lab02Z1(file, method, function1, function1Roz, 0, 60, 1.5, 7.5)

    # Zadanie 2
    fileNames2 = ("File4.txt", "File5.txt", "File6.txt", "File7.txt")
    steps = (0.01, 0.1, 0.25, 0.27)

    for file, step in zip(fileNames2, steps):
        lab02Z1(file, simpleEuera, function2, function2Roz, 0, 10, step, 9.5)

    # Zadanie 3
    fileNames3 = ("File8.txt", "File9.txt", "File10.txt", "File11.txt", "File12.txt")
    steps3 = (0.01, 0.1, 0.25, 0.27, 1.33)
    for file, step in zip(fileNames3, steps3):
        lab02Z1(file, complicateEuera2, function3, function2Roz, 0, 10, step, 9.5)
    #Zadanie 4
    fileNames4 = ("File13.txt", "File14.txt", "File15.txt")
    steps4 = (0.01, 0.125, 0.13)
    for file, step in zip(fileNames4, steps4):
        lab02Z4(file, iterationEuelera, function2, function2Roz, step, 9.5, 5)

    #Zadanie 5
    lab02Z4("File16.txt", newtonIter, function2, function2Roz, 1.33, 9.5, 15)

    #Zadanie 6
    lab02Z4("File17.txt", newtonIter, function6, function2Roz,1, 1.9, 15)

    #Zadanie 7
    lab02Z4("File18.txt", newtonIter3, function6, function2Roz,1, 1.9, 15)

    #Zadanie 8
    lab02Z8("File19.txt", newtonIter2, function2, function2Roz, 0, 30, 0.2, 9.5, 5, 0.1)


main()
