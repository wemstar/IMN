__author__ = 'wemstar'

import numpy as np



def ilorazRoznicowy(matrix):
	matrixV=np.zeros((241,81))
	matrixU=np.zeros((241,81))
	(m,n)=matrix.shape
	for x in range(1,m-1):
		for y in range(1,n-1):
			if ((x >=100 and x<=140) and (y<=18 or y >=62)):
				continue
			matrixU[x,y]=(matrix[x+1,y]-matrix[x-1,y])/2.0
			matrixV[x,y]=(matrix[x,y+1]-matrix[x,y-1])/2.0

	(m,n)=matrix.shape
	with open("Zadanie3u.txt","w") as fp1:
		with open("Zadanie3V.txt","w") as fp2:
			for i in range(m):
				for j in range(n):
					fp1.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i,j,matrixU[i][j]))
					fp2.write("{0:0.20f} {1:0.20f} {2:0.20f}\n".format(i,j,matrixV[i][j]))
				fp1.write("\n")
				fp2.write("\n")
def zadanie3(matrix):
    ilorazRoznicowy(matrix)