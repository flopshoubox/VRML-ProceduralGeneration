#!/usr/bin/python

from Class1 import Class1
from Class2 import Class2
from Cypres import Cypres
from Sapin import Sapin
from CostumPrint import *
from random import randint

def randTree(X=0,Y=0,Z=0,S=1,Type=-1):
    if Type == -1:
        Type = randint(0,3)

    if Type == 0:
        my_tree = Class1(X,Y,Z,S)
    elif Type == 1:
        my_tree = Class2(X,Y,Z,S)
    elif Type == 2:
        my_tree = Cypres(X,Y,Z,S)
    elif Type == 3:
        my_tree = Sapin(X,Y,Z,S)

    return my_tree.toString()

if __name__ == '__main__':
    typ = randint(0,3)

    if typ == 0:
        my_tree = Class1()
    elif typ == 1:
        my_tree = Class2()
    elif typ == 2:
        my_tree = Cypres()
    elif typ == 3:
        my_tree = Sapin()

    mon_fic.write(my_tree.toString())
