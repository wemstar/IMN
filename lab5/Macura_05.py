from cmath import sqrt

import zadanie1
import zadanie2
import zadanie3
from subprocess import call

__author__ = 'wemstar'




def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    zadanie3.zadanie3()
    call(["gnuplot", "Macura_05.gpl"])




main()