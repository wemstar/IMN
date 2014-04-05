from cmath import sqrt

import zadanie1
import zadanie2
from subprocess import call

__author__ = 'wemstar'




def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    call(["gnuplot", "Macura_05.gpl"])




main()