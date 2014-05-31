__author__ = 'wemstar'
import numpy as np
from utils import *


def zadanie2():
    U = np.zeros([301, 91])
    V = np.zeros([301, 91])
    readFromFile(U, V)
    mI = []
    mIX = []
    for x, ro in enumerate(leapfrog(U, V, mI, mIX)):
        saveMatrix("Zadanie2.{0}.txt".format(x), ro)
    with open("Zadanie2.I.txt", "w") as fp1:
        with open("Zadanie2.IX.txt", "w") as fp2:
            for i, (a, b) in enumerate(zip(mI, mIX)):
                fp1.write("{0:0.20f} {1:0.20f} \n".format(i, a))
                fp2.write("{0:0.20f} {1:0.20f} \n".format(i, b))


