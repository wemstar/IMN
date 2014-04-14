__author__ = 'wemstar'
import lab6.zadanie1
import lab6.zadanie2
import lab6.zadanie3
import lab6.zadanie4


from subprocess import call

__author__ = 'wemstar'




def main():
    lab6.zadanie1.zadanie1()
    # lab6.zadanie2.zadanie2()
    # lab6.zadanie3.zadanie3()
    # lab6.zadanie4.zadanie4()

    call(["gnuplot", "Macura_06.gpl"])




main()