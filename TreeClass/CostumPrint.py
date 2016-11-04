
from random import randint
from random import uniform
from random import triangular


def listStr(list, tab, mod):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%mod == 0:
            stri += str(x) + ",\n" + "\t" * tab + " "
        else:
            stri += str(x) + " "
    return stri

def matrixRand(matrix,a=-0.25,b=0.25):
    for i in range(0,len(matrix)):
        matrix[i] += uniform(a,b)
    return matrix

def matrixRandTrunk(matrix,a=-0.05,b=0.05):
    for i in range(0,len(matrix)/3):
        r = uniform(a,b)
        matrix[i*3] += r
        matrix[i*3+2] += r
    return matrix

def RandColor(list):
    list[0] += triangular(-0.1,0.1,0)
    list[1] +=  uniform(-0.20,0.30)
    list[2] += triangular(-0.1,0.1,0)
    return list
