import numpy as np
<<<<<<< HEAD
from math import exp, sqrt

=======
from scipy import weave
from scipy.weave import converters
>>>>>>> ea90c131e7ba4be9c2b270a5181761a39ea6393a



def zadanie1():
    file="Zadanie1_{0}.txt"
    tabRo=generateRo()
    for omega in [1.95]:
        matrix,pa=polason(omega,tabRo)
        with open(file.format(omega), "w") as fp:
            (m, n) = matrix.shape
            for i in range(m):
                for j in range(n):
                    fp.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, matrix[i][j]))
                fp.write("\n")
        with open(file.format(str(omega)+"_iter"),"w") as fp:
            for i,x in enumerate(pa):
                fp.write("{0:0.20f} {1:0.20f}\n".format(i,x))
    return matrix,tabRo


def polason(omega,roTab):
    error = 1
    pa =[1]
    matrix = np.zeros((121, 121))
    

    while error > 0.000000001:

        pa.append(a(matrix,roTab))
        matrix=metoda(matrix,omega,roTab)

        error = abs(pa[-1] - pa[-2])
    return matrix,pa

def metoda(matrix, omega,roTab):
    (m, n) = matrix.shape
<<<<<<< HEAD

    #matrix[1:-1,1:-1]=((1-omega)*matrix[1:-1,1:-1]+omega*0.25*(matrix[:-2,1:-1]+matrix[2:,1:-1]+matrix[1:-1,:-2]+matrix[1:-1,2:]+roTab[1:-1,1:-1]))
    for i in range(1,m-1):
        for j in range(1,n-1):
            matrix[i][j]=(1-omega)*matrix[i][j]+omega*0.25*(matrix[i-1][j]+matrix[i+1][j]+matrix[i][j+1]+matrix[i][j-1]+roTab[i][j])

=======
    code2="""
for(int i=1;i<m-1;i++)
    for(int j=1;j<n-1;j++)
    {
        double x=pow((i-60) * 0.1,2.0);
        double y=pow((j-60) * 0.1,2.0);
        double ro=exp(-pow(sqrt( x+y)-2.0  ,2.0));
        matrix(i,j)=(1 - omega) * matrix(i,j)+ omega * (
                matrix(i + 1,j) + matrix(i - 1,j) + matrix(i,j + 1) + matrix(i,j - 1) + ro) * 0.25;
    }
"""
    weave.inline(code2,['matrix','m','n','omega'],type_converters=converters.blitz)
>>>>>>> ea90c131e7ba4be9c2b270a5181761a39ea6393a
    return matrix
def generateRo():

    tabRo= np.zeros((121, 121))
    (m, n) = tabRo.shape
    for i in range(1,m-1):
        for j in range(1,n-1):
            tabRo[i][j]=ro(i-60,j-60)
    return tabRo


<<<<<<< HEAD


def ro(x, y):
    return exp(-((sqrt((x * 0.1) ** 2.0 + (y * 0.1) ** 2) - 2.0) ** 2.0))


def a(matrix,roTab):
    # (m, n) = matrix.shape
    # suma=0
    # for i in range(1,m-1):
    #     for j in range(1,n-1):
    #         pochodnax=(matrix[i+1][j]-matrix[i-1][j])*0.5;
    #         pochodnay=(matrix[i][j+1]-matrix[i][j-1])*0.5;
    #         trzeci=matrix[i][j]*roTab[i][j]
    #         suma+=0.5*(pochodnax*pochodnax +pochodnay*pochodnay)-trzeci
    return np.sum((((matrix[2:,1:-1]-matrix[:-2,1:-1])*0.5)**2.0+((matrix[1:-1,2:]-matrix[1:-1,:-2])*0.5)**2.0)*0.5-matrix[1:-1,1:-1]*roTab[1:-1,1:-1])
    
=======
def a(matrix):
    (m, n) = matrix.shape
    code="""
double pochodnax,pochodnay,trzeci,err=0.0,suma=0,ro;
for(int i=1;i<m-1;++i)
{
    for(int j=1;j<n-1;++j)
    {
        pochodnax=(matrix(i+1,j)-matrix(i-1,j))*0.5;
        pochodnay=(matrix(i,j+1)-matrix(i,j-1))*0.5;
        double x=pow((i-60) * 0.1,2.0);
        double y=pow((j-60) * 0.1,2.0);
        ro=exp(-pow(sqrt( x+y)  -2.0,2.0));
        trzeci=matrix(i,j)*ro;
        suma+=(0.5*(pochodnax*pochodnax +pochodnay*pochodnay)-trzeci);
    }
}
return_val = suma;
"""
    err=weave.inline(code,['matrix','m','n'],type_converters=converters.blitz)
    return err
>>>>>>> ea90c131e7ba4be9c2b270a5181761a39ea6393a





