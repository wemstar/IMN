import numpy as np
from scipy import weave
from scipy.weave import converters

def zadanie2(matrix):
    potencjal = np.zeros((121, 121))
    dokladny=np.zeros((121, 121))
    (m, n) = matrix.shape

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
    weave.inline(code,['matrix','m','n','dokladny','potencjal'],support_code=support)

    with open("Zadanie2Poch.txt","w") as fp1,open("Zadanie2Dok.txt","w") as fp2:
        (m, n) = matrix.shape
        for i in range(m):
            for j in range(n):
                fp1.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, potencjal[i][j]))
                fp2.write("{0:0.20f} {1:0.20f} {2:0.20f} \n".format(i - 60, j - 60, dokladny[i][j]))
            fp1.write("\n")
            fp2.write("\n")
support="""
double potencjalFun(double i,double j)
{
    double x=pow((i-60) * 0.1,2.0);
    double y=pow((j-60) * 0.1,2.0);
    return exp(-pow(sqrt( x+y)  -2.0,2.0));
}
"""