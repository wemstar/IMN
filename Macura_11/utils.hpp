#define N 301
#define M 91
#include <iostream>
#include <string>
#include <fstream>
#include <algorithm> 
#include <math.h> 
using namespace std;
void metoda(double strumien[301][91],double wirowosc[301][91],int n,int m,bool tryb);
double strum(double j,double Q=-1.0);
double wir(double j,double Q=-1.0);
double pred(double j,double Q=-1.0);
void predkoscU(double predkosc[91],double strumien[301][91],int m);
void predkoscU(double predkosc[301][91],double strumien[301][91],int m);
void predkoscV(double predkosc[301][91],double strumien[301][91],int m);
void zeruj(double tablica[301][91]);
