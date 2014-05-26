__author__ = 'wemstar'
import zadanie1
import zadanie2
import zadanie3
import zadanie4
import zadanie5
import zadanie6


from subprocess import call

__author__ = 'wemstar'




def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    zadanie3.zadanie3()
    zadanie4.zadanie4()
    zadanie5.zadanie5()
    zadanie6.zadanie6()

    call(["gnuplot", "Macura_06.gpl"])




main()