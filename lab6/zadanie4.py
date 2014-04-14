__author__ = 'wemstar'

from lab6.relaksacji import *


def zadanie4():
    srodkowy("Zadanie4.1.txt", 10.0 ** -5.0, iterate)
    srodkowy("Zadanie4.2.txt", 10.0 ** -8.0, iterate)
    srodkowy("Zadanie4.3.txt", 10.0 ** -13.0, iterate)


def iterate(tab, dr=0.1):
    tab[-2].f=-1
    tab[-1].f=-1
    for i in reversed(range(1, len(tab) - 1)):
        pierwszy = -4.0 * pi * tab[i + 1].r * nr(tab[i + 1].r)
        drugi = -4.0 * pi * tab[i].r * nr(tab[i].r)
        trzeci = -4.0 * pi * tab[i - 1].r * nr(tab[i - 1].r)
        czwarty = 2.0*tab[i].f - tab[i + 1].f
        tab[i-1].f = (pierwszy +10.0* drugi+trzeci)*(dr**2.0)/12.0 +czwarty