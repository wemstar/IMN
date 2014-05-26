import numpy as np


def zadanie2(matrix,dokladny):
    potencjal = np.zeros((121, 121))
    (m, n) = matrix.shape

    
    (m, n) = matrix.shape
 
    potencjal[1:-1,1:-1]=-((matrix[2:,1:-1]-2.0*matrix[1:-1,1:-1]+matrix[:-2,1:-1])+(matrix[1:-1,2:]-2.0*matrix[1:-1,1:-1]+matrix[1:-1,:-2]))
    with open("Zadanie2Poch.txt","w") as fp1:
        (m, n) = matrix.shape
        for i in range(m):
            for j in range(n):
                fp1.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, potencjal[i][j]))

            fp1.write("\n")

    with open("Zadanie2Dok.txt","w") as fp2:
        (m, n) = matrix.shape
        for i in range(m):
            for j in range(n):

                fp2.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, dokladny[i][j]))

            fp2.write("\n")
