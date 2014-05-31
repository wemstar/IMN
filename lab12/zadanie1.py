__author__ = 'wemstar'
import numpy as np
from utils import *


def zadanie1():
    u = prepareU(np.zeros([301, 91]))
    v = np.zeros([301, 91])
    mI = []
    mIX = []
    for x, ro in enumerate(leapfrog(u, v, mI, mIX)):
            saveMatrix("Zadanie1.{0}.txt".format(x), ro)
    with open("Zadanie1.I.txt", "w") as fp1:
        with open("Zadanie1.IX.txt", "w") as fp2:
            for i, (a, b) in enumerate(zip(mI, mIX)):
                fp1.write("{0:0.20f} {1:0.20f} \n".format(i, a))
                fp2.write("{0:0.20f} {1:0.20f} \n".format(i, b))


def prepareU(matrix):
    (m, n) = matrix.shape
    for i in range(n):
        y = i * 0.01
        matrix[:, i] = -1.0 / 2.0 * y * (y - 0.9)
    return matrix