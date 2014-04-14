__author__ = 'wemstar'



from relaksacji import *


def zadanie3():
    srodkowy("Zadanie3.1.txt", 10.0 ** -13.0, iterate)
    srodkowy("Zadanie3.2.txt", 10.0 ** -13.0, iterate,0.01)
    srodkowy("Zadanie3.3.txt", 10.0 ** -13.0, iterate2)



def iterate(tab,dr=0.1):
    tab[1].f=function1Roz(tab[1].r)
    tab[0].f=0
    for i in range(1, len(tab) - 1):
        pierwszy = -4.0 * pi * (dr ** 2.0) * tab[i].r * nr(tab[i].r)
        drugi = -tab[i-1].f+2.0*tab[i].f
        tab[i+1].f = pierwszy + drugi

def iterate2(tab,dr=0.1):
    tab[1].f=-0.024958398625867
    tab[0].f=0
    for i in range(1, len(tab) - 1):
        pierwszy = -4.0 * pi * (dr ** 2.0) * tab[i].r * nr(tab[i].r)
        drugi = -tab[i-1].f+2.0*tab[i].f
        tab[i+1].f = pierwszy + drugi

