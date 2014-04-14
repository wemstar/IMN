__author__ = 'wemstar'



from relaksacji import *


def zadanie5():
    srodkowy("Zadanie5.1.txt", 10.0 ** -13.0, iterate)
    srodkowy("Zadanie5.2.txt", 10.0 ** -13.0, iterate,0.01)
    srodkowy("Zadanie5.3.txt", 10.0 ** -13.0, iterate2)

def iterate(tab, dr=0.1):
    tab[1].f=function1Roz(tab[1].r)
    tab[0].f=0
    for i in range(1, len(tab) - 1):
        pierwszy = -4.0 * pi * tab[i + 1].r * nr(tab[i + 1].r)
        drugi =- 4.0 * pi * tab[i].r * nr(tab[i].r)
        trzeci = -4.0 * pi * tab[i - 1].r * nr(tab[i - 1].r)
        czwarty = 2.0*tab[i].f - tab[i - 1].f
        tab[i+1].f = (pierwszy +10.0* drugi+trzeci)*(dr**2)/12.0 +czwarty

def iterate2(tab, dr=0.1):
    tab[1].f=-0.024958398625867
    tab[0].f=0
    for i in range(1, len(tab) - 1):
        pierwszy = -4.0 * pi * tab[i + 1].r * nr(tab[i + 1].r)
        drugi = -4.0 * pi * tab[i].r * nr(tab[i].r)
        trzeci = -4.0 * pi * tab[i - 1].r * nr(tab[i - 1].r)
        czwarty = 2.0*tab[i].f -tab[i - 1].f
        tab[i+1].f = (pierwszy +10.0* drugi+trzeci)*(dr**2)/12.0 +czwarty