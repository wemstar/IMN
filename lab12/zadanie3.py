__author__ = 'wemstar'

import numpy as np
from utils import *
def zadanie3():
    U = np.zeros([301, 91])
    V = np.zeros([301, 91])
    readFromFile(U, V)
    for x, ro in enumerate(LaxFriedrichs(U, V)):
        saveMatrix("Zadanie3.{0}.txt".format(x), ro, True)

