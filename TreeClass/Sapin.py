#!/usr/bin/python
import os
from random import randint
from random import uniform


class Sapin:
    """docstring for Sapin"""

    posTree = []
    scaleTree = [1, 1 ,1]
    colorLeaf = [0,0.392157,0]
    colorTrunk = [0.545098,0.270588,0.0745098]
    scaleTrunkG = [0.75,1,0.75]
    scaleTrunk = [0.5,0.5,0.5,0.5,0.5,0.5]
    spineTrunk = [0,0.5,0,0,1,0,0,1.5,0] #2
    crossSectionTrunk = [1,0,0.707106,-0.707106,0,-1,-0.707106,-0.707106,-1,0,-0.707106,0.707106,0,1,0.707106,0.707106,1,0] #2

    posLeaf = [0, 1, 0]
    scaleLeafG = [1,1,1]
    spineLeaf = [0,0.5,0,0,0.65,0,0,1.5,0,0,2,0,0,2.5,0]
    crossSectionLeaf = [0.866025,0.5,0.866025,-0.5,0,-1, -0.866025,-0.5,-0.866025,0.5,0,1,0.866025,0.5]
    scaleLeaf =  [1,1,1.4,1.4,0.8,0.8,0.4,0.4,0,0]



    def __init__(self, X=0, Y=0, Z=0):
        self.posTree = [X,Y,Z]

    def toString(self):
        stri = "#VRML V2.0 utf8\n\n"

        stri += "Transform {\n"
        stri += "\ttranslation " + "  ".join(str(x) for x in self.posTree) + "\n"
        stri += "\tscale " + "  ".join(str(x) for x in self.scaleTree) + "\n"
        stri += "\tchildren [\n"


        for i in range(0,3):
            self.posLeaf = [0, 1 + i, 0]
            self.scaleLeafG = [1 - i *0.2,1 - i *0.2,1 - i *0.2]

            stri += "\t\tTransform {\n"
            stri += "\t\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf) + "\n"
            stri += "\t\t\tscale " + "  ".join(str(x) for x in self.scaleLeafG) + "\n"
            stri += "\t\t\tchildren [\n"
            stri += "\t\t\t\tShape {\n"
            stri += "\t\t\t\t\tappearance	Appearance {\n"
            stri += "\t\t\t\t\t\tmaterial Material {\n"
            stri += "\t\t\t\t\t\t\tdiffuseColor "+ " ".join(str(x) for x in self.colorLeaf) + "\n"
            stri += "\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t}\n"
            stri += "\t\t\t\t\tgeometry Extrusion {\n"
            stri += "\t\t\t\t\t\tccw TRUE\n"
            stri += "\t\t\t\t\t\tspine [\n"
            stri += listStr3(self.spineLeaf, 6) + "]\n"
            stri += "\t\t\t\t\tscale [\n"
            stri += listStr2(self.scaleLeaf, 6) + "]\n"
            stri += "\t\t\t\t\t\tcrossSection [\n"
            stri += listStr2(self.crossSectionLeaf, 6) + "]\n"
            stri += "\t\t\t\t\t}\n"
            stri += "\t\t\t\t}\n"
            stri += "\t\t\t]\n"
            stri += "\t\t}\n"

        stri += "\t\tTransform {\n"
        stri += "\t\tscale " + "  ".join(str(x) for x in self.scaleTrunkG) + "\n"
        stri += "\t\t\tchildren [\n"
        stri += "\t\t\t\tShape {\n"
        stri += "\t\t\t\t\tappearance Appearance {\n"
        stri += "\t\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\t\tdiffuseColor " + "  ".join(str(x) for x in self.colorTrunk) + "\n"
        stri += "\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\t\tccw TRUE\n"
        stri += "\t\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineTrunk, 6) + "]\n"
        stri += "\t\t\t\t\t\tscale [\n"
        stri += listStr2(self.scaleTrunk, 6) + "]\n"
        stri += "\t\t\t\t\t\tcrossSection [\n"
        stri += listStr2(self.crossSectionTrunk, 6) + "]\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t]\n"
        stri += "\t\t}\n"
        stri += "\t]\n"
        stri += "}"

        return stri

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

if __name__ == '__main__':
    myTree = Sapin()
    # print myTree.toString()
    mon_fic = open('Sapin.wrl','w')
    mon_fic.write(myTree.toString())
    mon_fic.close()
