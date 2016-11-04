#!/usr/bin/python

from Class1 import Class1
from Class2 import Class2
from Cypres import Cypres
from Sapin import Sapin
from CostumPrint import *
from random import randint

def main():
    typ = randint(0,3)

    if typ == 0:
        my_tree = Class1()
    elif typ == 1:
        my_tree = Class2()
    elif typ == 2:
        my_tree = Cypres()
    elif typ == 3:
        my_tree = Sapin()

    mon_fic = open('Base.wrl','w')
    mon_fic.write("#VRML V2.0 utf8\n\n")
    mon_fic.write("WorldInfo {\n")
    mon_fic.write("info [Auteur: Alexis CARE]\n")
    mon_fic.write("title \"arbre creer pseudo-aleatoirement\"\n")
    mon_fic.write("}\n")
    mon_fic.write(my_tree.toString())
    mon_fic.close()

if __name__ == '__main__':
    main()
