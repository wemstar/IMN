from cmath import sqrt

import lab5.zadanie1
import lab5.zadanie2
import lab5.zadanie3

from subprocess import call

__author__ = 'wemstar'




def main():
    lab5.zadanie1.zadanie1()
    lab5.zadanie2.zadanie2()
    lab5.zadanie3.zadanie3()

    call(["gnuplot", "Macura_05.gpl"])




main()