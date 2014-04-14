
from lab6.relaksacji import *

__author__ = 'wemstar'


def zadanie1():
    srodkowy("Zadanie1.1.txt", 10.0 ** -5.0, iterate)
    srodkowy("Zadanie1.2.txt", 10.0 ** -8.0,iterate)
    srodkowy("Zadanie1.3.txt", 10.0 ** -13.0,iterate)


def iterate(tab, dr=0.1):
    for i in range(1, len(tab) - 1):
        pierwszy = 2.0 * pi * (dr ** 2.0) * tab[i].r * nr(tab[i].r)
        drugi = 0.5 * (tab[i - 1].f + tab[i + 1].f)
        tab[i].f = pierwszy + drugi
