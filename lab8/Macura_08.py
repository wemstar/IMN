from subprocess import call

__author__ = 'dom'


import zadanie1
import zadanie2
import zadanie3







def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    zadanie3.zadanie3()
    call(["gnuplot", "Macura_08.gpl"])

main()
