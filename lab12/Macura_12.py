import subprocess

__author__ = 'wemstar'
import zadanie1
import zadanie2
import zadanie3







def main():
    # zadanie1.zadanie1()
    zadanie2.zadanie2()
    zadanie3.zadanie3()
    subprocess.call(["gnuplot", "Macura_12.gpl"])


main()