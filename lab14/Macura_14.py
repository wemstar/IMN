import subprocess

__author__ = 'wemstar'
import zadanie1
import zadanie2
import zadanie3
import zadanie4
import zadanie5


def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    zadanie3.zadanie3()
    zadanie4.zadanie4()
    zadanie5.zadanie5()
    subprocess.call(["gnuplot", "Macura_14.gpl"])
main()