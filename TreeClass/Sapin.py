#!/usr/bin/python
from CostumPrint import *

class Sapin:
    """docstring for Sapin"""

    posTree = []
    scaleTree = []
    colorLeaf = [0,0.392157,0]
    colorTrunk = [0.545098,0.270588,0.0745098]
    scaleTrunkG = [0.75,1,0.75]
    scaleTrunk = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    spineTrunk = [0,0,0,0,0.5,0,0,1,0,0,1.5,0]
    crossSectionTrunk = [1,0,0.707106,-0.707106,0,-1,-0.707106,-0.707106,-1,0,-0.707106,0.707106,0,1,0.707106,0.707106,1,0] #2

    posLeaf = [0, 1, 0]
    scaleLeafG = [1,1,1]
    spineLeaf = [0,0.5,0,0,0.65,0,0,1.5,0,0,2,0,0,2.5,0]
    crossSectionLeaf = [0.866025,0.5,0.866025,-0.5,0,-1, -0.866025,-0.5,-0.866025,0.5,0,1,0.866025,0.5]
    scaleLeaf =  [1,1,1.4,1.4,0.8,0.8,0.4,0.4,0,0]



    def __init__(self,X=0,Y=0,Z=0,S=1):
        self.posTree = [X,Y,Z]
        self.scaleTree = [S, S, S]

    def toString(self):
        #stri = "#VRML V2.0 utf8\n\n"
        tempColor = RandColor(self.colorLeaf[:])

        stri = "\t\t\t\t\tTransform {\n"
        stri += "\t\t\t\t\t\ttranslation " + "  ".join(str(x) for x in self.posTree) + "\n"
        stri += "\t\t\t\t\t\tscale " + "  ".join(str(x) for x in self.scaleTree) + "\n"
        stri += "\t\t\t\t\t\tchildren [\n"


        for i in range(0,3):
            self.posLeaf = [0, 1 + i, 0]
            self.scaleLeafG = [1 - i *0.2,1 - i *0.2,1 - i *0.2]

            stri += "\t\t\t\t\t\t\tTransform {\n"
            stri += "\t\t\t\t\t\t\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf) + "\n"
            stri += "\t\t\t\t\t\t\t\tscale " + "  ".join(str(x) for x in self.scaleLeafG) + "\n"
            stri += "\t\t\t\t\t\t\t\tchildren [\n"
            stri += "\t\t\t\t\t\t\t\t\tShape {\n"
            stri += "\t\t\t\t\t\t\t\t\t\tappearance	Appearance {\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\tmaterial Material {\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\t\tdiffuseColor "+ " ".join(str(x) for x in tempColor) + "\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t\t\t\tgeometry Extrusion {\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\tccw TRUE\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\tspine [\n"
            stri += listStr(self.spineLeaf, 11, 3) + "]\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\tscale [\n"
            stri += listStr(self.scaleLeaf, 11, 2) + "]\n"
            stri += "\t\t\t\t\t\t\t\t\t\t\tcrossSection [\n"
            stri += listStr(self.crossSectionLeaf, 11, 2) + "]\n"
            stri += "\t\t\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t\t\t}\n"
            stri += "\t\t\t\t\t\t\t\t]\n"
            stri += "\t\t\t\t\t\t\t}\n"

        stri += "\t\t\t\t\t\t\tTransform {\n"
        stri += "\t\t\t\t\t\t\tscale " + "  ".join(str(x) for x in self.scaleTrunkG) + "\n"
        stri += "\t\t\t\t\t\t\t\tchildren [\n"
        stri += "\t\t\t\t\t\t\t\t\tShape {\n"
        stri += "\t\t\t\t\t\t\t\t\t\tappearance Appearance {\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\t\tdiffuseColor " + "  ".join(str(x) for x in self.colorTrunk) + "\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\t\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\tccw TRUE\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\tspine [\n"
        stri += listStr(self.spineTrunk, 11, 3) + "]\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\tscale [\n"
        stri += listStr(self.scaleTrunk, 11, 2) + "]\n"
        stri += "\t\t\t\t\t\t\t\t\t\t\tcrossSection [\n"
        stri += listStr(self.crossSectionTrunk, 11, 2) + "]\n"
        stri += "\t\t\t\t\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\t\t\t]\n"
        stri += "\t\t\t\t\t\t\t}\n"
        stri += "\t\t\t\t\t\t]\n"
        stri += "\t\t\t\t\t\t\t}"

        return stri

if __name__ == '__main__':
    myTree = Sapin()
    # print myTree.toString()
    mon_fic = open('Sapin.wrl','w')
    mon_fic.write(myTree.toString())
    mon_fic.close()
