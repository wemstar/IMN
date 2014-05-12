from cmath import sqrt

import lab05.zadanie1
import lab05.zadanie2
import lab05.zadanie3

from subprocess import call

__author__ = 'wemstar'




def main():
    lab05.zadanie1.zadanie1()
    lab05.zadanie2.zadanie2()
    lab05.zadanie3.zadanie3()

    call(["gnuplot", "Macura_05.gpl"])




main()