import numpy as np
from math import exp, sqrt
def zadanie1():
	error=1
	pa=0
	while error >0.000001:		
		matrix=np.zeros((121,121))
		metoda(matrix,0.5)
		ta=a(matrix)
		error=pa-ta
		pa=ta
		print(error)
	with open("Zadanie1.txt","w") as fp:
		(m,n)=matrix.shape
		for i in range(m):
			for j in range(n):
				fp.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i-60,j-60,matrix[i][j]))

		



def metoda(matrix,omega):
	(m,n)=matrix.shape
	for i in range(1,m-1):
		for j in range(1,n-1):
			matrix[i][j]=(1-omega)*matrix[i][j] + omega*(matrix[i+1][j]+matrix[i-1][j]+matrix[i][j+1]+matrix[i][j-1]+ro(i-60.0,j-60.0))/(4)

def ro(x,y):
	return exp(-(sqrt((x*0.1)**2.0+(y*0.1)**2)-2.0)**2.0)		

def a(matrix):
	sum=0
	(m,n)=matrix.shape
	for i in range(1,m-1):
		for j in range(1,n-1):
			pochodnax=(matrix[i+1][j]-matrix[i-1][j])*0.5
			pochodnay=(matrix[i][j+1]-matrix[i][j-1])*0.5
			trzeci=matrix[i][j]*ro(i-60,j-60)
			sum+=(0.5*(pochodnax**2.0+pochodnay**2.0)-trzeci)
	return sum