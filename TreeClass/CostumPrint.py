import os
from random import randint
from random import uniform


def listStr3(list, tab):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%3 == 0:
            stri += str(x) + ",\n" + "\t" * tab + " "
        else:
            stri += str(x) + " "
    return stri

def listStr4(list, tab):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%4 == 0:
            stri += str(x) + ",\n" + "\t" * tab + " "
        else:
            stri += str(x) + " "
    return stri

def listStr2(list, tab):
    ind = 0
    stri = "\t" * tab + " "
    for x in list:
        ind += 1
        if ind%2 == 0:
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
