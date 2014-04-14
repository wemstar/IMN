__author__ = 'wemstar'

from lab6.relaksacji import *


def zadanie2():
    srodkowy("Zadanie2.1.txt", 10.0 ** -5.0, iterate)
    srodkowy("Zadanie2.2.txt", 10.0 ** -8.0,iterate)
    srodkowy("Zadanie2.3.txt", 10.0 ** -13.0,iterate)


def iterate(tab,dr=0.1):
    tab[-2].f=-1
    tab[-1].f=-1
    for i in reversed(range(1, len(tab) - 1)):
        pierwszy = -4.0 * pi * (dr ** 2.0) * tab[i].r * nr(tab[i].r)
        drugi = -tab[i+1].f+2.0*tab[i].f
        tab[i-1].f = pierwszy + drugi

