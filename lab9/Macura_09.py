from subprocess import call

__author__ = 'dom'


import zadanie1
import zadanie2







def main():
    matrix=zadanie1.zadanie1()
    zadanie2.zadanie2()

    call(["gnuplot", "Macura_09.gpl"])

main()