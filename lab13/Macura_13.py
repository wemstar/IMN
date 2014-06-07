__author__ = 'wemstar'


import zadanie1
import zadanie2
import subprocess


def main():
    zadanie1.zadanie1()
    zadanie2.zadanie2()
    subprocess.call(["gnuplot", "Macura_13.gpl"])
main()