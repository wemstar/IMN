#include "utils.hpp"

void zeruj(double tablica[301][91])
{
	for(int i=0;i<301;i++)
		for(int j=0;j<91;j++)
		{
			tablica[i][j]=0.0;
		}
}
void iteruj(double strumien[301][91],double wirowosc[301][91],int n,int m,bool tryb)
{
	for(int i=1;i<n-1;i++)
		for(int j=1;j<m-1;j++)
		{
			if(!(tryb && ( i >= 90 && i<=101 && j>=50)) )
			{
				double pierwszy=(wirowosc[i+1][j]+wirowosc[i-1][j]+wirowosc[i][j+1]+wirowosc[i][j-1])/4.0 ;
				double drugi=(strumien[i][j+1]-strumien[i][j-1])*(wirowosc[i+1][j]-wirowosc[i-1][j]);
				double trzeci=(strumien[i+1][j]-strumien[i-1][j])*(wirowosc[i][j+1]-wirowosc[i][j-1]);
				wirowosc[i][j]=pierwszy-(drugi-trzeci)/16.0;



				strumien[i][j]=(strumien[i+1][j]+strumien[i-1][j]+strumien[i][j+1]+strumien[i][j-1]-wirowosc[i][j]*(0.01*0.01))/4.0;
			}
		}
}


double strum(double j,double Q)
{
	double y=j*0.01;
	return ((y*y*y)/3.0-(y*y)*0.9/2.0)*Q/2.0;
}
double wir(double j,double Q)
{
	double y=j*0.01;
	return (2.0*y-0.9)/2.0*Q;
}
double pred(double j,double Q)
{
	double y=j*0.01;
	return Q*(y*(y-0.9))/2.0;
}

void predkoscU(double predkosc[91],double strumien[301][91],int m)
{
	for(int j=1;j<m-1;j++)
	{
		predkosc[j]=(strumien[100][j+1]-strumien[100][j-1])/(0.02);
	}
}
void predkoscU(double predkosc[301][91],double strumien[301][91],int m)
{
	for(int i=0;i<301;i++)
	for(int j=1;j<m-1;j++)
	{
		if(!( i >= 90 && i<=101 && j>=50) )
		predkosc[i][j]=(strumien[i][j+1]-strumien[i][j-1])/(0.02);
	};
}
void predkoscV(double predkosc[301][91],double strumien[301][91],int m)
{
	for(int i=1;i<300;i++)
	for(int j=0;j<m;j++)
	{
		if(!( i >= 90 && i<=101 && j>=50) )
		predkosc[i][j]=(strumien[i+1][j]-strumien[i-1][j])/(0.02);
	};
}

void generujWir(double strumien[301][91],double wirowosc[301][91],int n,int m)
{
	for(int i=0;i<n;i++)
	{
		wirowosc[i][90]=2.0*(strumien[i][89]-strumien[i][90])/(0.01*0.01);
		wirowosc[i][0]=2.0*(strumien[i][1]-strumien[i][0])/(0.01*0.01);
	}
	for(int j=50;j<m;j++)
	{
		wirowosc[101][j]=2.0*(strumien[102][j]-strumien[101][j])/(0.01*0.01);
		wirowosc[90][j]=2.0*(strumien[89][j]-strumien[90][j])/(0.01*0.01);
	}
	for(int i=90;i<=101;i++)
	{
		wirowosc[i][50]=2.0*(strumien[i][49]-strumien[i][50])/(0.01*0.01);
	}
	wirowosc[90][50]=(strumien[89][50]-strumien[90][50])/(0.01*0.01)+(strumien[90][49]-strumien[90][50])/(0.01*0.01);
	wirowosc[101][50]=(strumien[102][50]-strumien[101][50])/(0.01*0.01)+(strumien[101][49]-strumien[101][50])/(0.01*0.01);
}
void metoda(double strumien[301][91],double wirowosc[301][91],int n,int m,bool tryb)
{
	int i=0;
	for(i=0;i<200;i++)
	{
		
		iteruj(strumien,wirowosc,n,m,tryb);
		if(tryb)generujWir(strumien,wirowosc,n,m);
	
	}
	double error=1.0;
	while (error > 0.0000001)
	{
		
		double ps=strumien[150][45];
		double pw=wirowosc[150][45];
		if(tryb)generujWir(strumien,wirowosc,n,m);
		iteruj(strumien,wirowosc,n,m,tryb);
		++i;
		error=max(fabs(ps- strumien[150][45]),fabs(pw- wirowosc[150][45]));
		
	}
	cout << "Ilosc iteracji : " << i << endl;
}
