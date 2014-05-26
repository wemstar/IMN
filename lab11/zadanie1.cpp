#include "utils.hpp"
using namespace std;



void zapisz(string file,double strumen[301][91],double wirowosc[301][91],double predkosc[91],int n,int m)
{
	ofstream fileStrum((file + "Strum" + ".txt").c_str()); 
	fileStrum.precision(20);	
	fileStrum.setf(ios::fixed);
	fileStrum.setf(ios::showpoint);

	for(int j=0;j<m;j++)
	{
		fileStrum << j << " " << strumen[100][j] <<" " << strumen[100][j] << " "<< strum(j) << endl;
	}
	fileStrum.close();
	ofstream fileU((file + "U" + ".txt").c_str()); 
	fileU.precision(20);	
	fileU.setf(ios::fixed);
	fileU.setf(ios::showpoint);
	for(int j=0;j<m;j++)
	{
		fileU << j << " " << predkosc[j] <<" " <<pred(j) << endl;
	}
}

void generateArray(double strumien[301][91],double wirowsc[301][91],int n,int m)
{
		for(int j=0;j<m;j++)
		{
			strumien[0][j]=strum(j);
			wirowsc[0][j]=wir(j);
			strumien[300][j]=strum(j);
			wirowsc[300][j]=wir(j);
		};
		for(int i=0;i<n;i++)
		{
			strumien[i][0]=strum(0);
			wirowsc[i][0]=wir(0);
			strumien[i][90]=strum(90);
			wirowsc[i][90]=wir(90);
		}
}


void zadanie1()
{

	double strumien[301][91] ;
	double wirowsc[901][91] ;
	double predkosc[91];
	generateArray(strumien,wirowsc,301,91);
	//metoda(strumien,wirowsc,N,M,false);
	predkoscU(predkosc,strumien,M);
	zapisz("zadanie1",strumien,wirowsc,predkosc,N,M);
}