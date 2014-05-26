#include "utils.hpp"
using namespace std;
void zapisz(string file,double zapis[301][91],int n,int m)
{
	ofstream fileS((file +".txt").c_str()); 
	fileS.precision(20);	
	fileS.setf(ios::fixed);
	fileS.setf(ios::showpoint);
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			fileS << (double)i<< " " << (double)j <<" " << zapis[i][j] << endl;
		}
		fileS << endl;
	}
	fileS.close();
}

void generateArray(double strumien[301][91],double wirowsc[301][91],int n,int m,double Q)
{
		for(int j=0;j<=90;j++)
		{
			strumien[0][j]=strum(j,Q);
			wirowsc[0][j]=wir(j,Q);
			strumien[300][j]=strum(j,Q);
			wirowsc[300][j]=wir(j,Q);
		}
		for(int i=0;i<n;i++)
		{
			strumien[i][0]=strum(0,Q);
			wirowsc[i][0]=wir(0,Q);
			strumien[i][90]=strum(90,Q);
			wirowsc[i][90]=wir(90,Q);
		}

		for(int j=50;j<m;j++)
		{
			strumien[101][j]=strum(90,Q);
			strumien[90][j]=strum(90,Q);
			wirowsc[101][j]=wir(90,Q);
			wirowsc[90][j]=wir(90,Q);
		}
		for(int i=90;i<=101;i++)
		{
			strumien[i][50]=strum(90,Q);
			wirowsc[i][50]=wir(90,Q);
		}
}
void wykonajZadanie(string filename,double Q)
{
	double strumien[301][91] ;
	double wirowsc[301][91] ;
	double predkosc[301][91];
	generateArray(strumien,wirowsc,301,91,Q);
	metoda(strumien,wirowsc,N,M,true);
	zapisz(filename,strumien,N,M);
	predkoscU(predkosc,strumien,91);
	zapisz(filename+"U",predkosc,N,M);
	predkoscV(predkosc,strumien,91);
	zapisz(filename+"V",predkosc,N,M);
}


void zadanie2()
{
	wykonajZadanie("Zadanie2.1",-1.0);
	wykonajZadanie("Zadanie2.100",-100.0);
	wykonajZadanie("Zadanie2.200",-200.0);
	wykonajZadanie("Zadanie2.400",-400.0);
	

}