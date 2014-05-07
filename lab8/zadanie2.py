import numpy as np


def zadanie2(matrix,dokladny):
    potencjal = np.zeros((121, 121))
    (m, n) = matrix.shape

<<<<<<< HEAD
    
    (m, n) = matrix.shape
 
    potencjal[1:-1,1:-1]=-((matrix[2:,1:-1]-2.0*matrix[1:-1,1:-1]+matrix[:-2,1:-1])+(matrix[1:-1,2:]-2.0*matrix[1:-1,1:-1]+matrix[1:-1,:-2]))
=======
    code = """
    for(int i=1;i<m-1;i++)
    for(int j=1;j<n-1;j++)
    {
        double pochodnax=(matrix(i+1,j)-2.0*matrix(i,j)+matrix(i-1,j));
        double pochodnay=(matrix(i,j+1)-2.0*matrix(i,j)+matrix(i,j-1));
        potencjal(i,j)=(pochodnax*pochodnax +pochodnay*pochodnay);
        dokladny(i,j)=potencjalFun(i,j);
    }
        """
    weave.inline(code,['matrix','m','n','dokladny','potencjal'],type_converters=converters.blitz,support_code=support)

>>>>>>> ea90c131e7ba4be9c2b270a5181761a39ea6393a
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
