#!/usr/bin/python


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

    posLeaf1 = [0, 1, 0]
    scaleLeaf1G = [1,1,1]
    spineLeaf1 = [0,0.5,0,0,1,0,0,1.5,0]
    crossSectionLeaf1 = [-1,0,-0.707106,0.707106,0,1, 0.707106,0.707106,1,0,0.866025,0.5,0.866025,-0.5,0,-1, -0.866025,-0.5,-0.866025,0.5,0,1,0.866025,0.5]
    scaleLeaf1 =  [1,1,1.4,1.4,0.8,0.8,0.4,0.4,0,0]

    posLeaf2 = [0, 3, 0]
    scaleLeaf2G = [0.8,0.8,0.8]
    spineLeaf2 = [0,0.5,0,0,1,0,0,1.5,0]
    crossSectionLeaf2 = [-1,0,-0.707106,0.707106,0,1, 0.707106,0.707106,1,0,0.866025,0.5,0.866025,-0.5,0,-1, -0.866025,-0.5,-0.866025,0.5,0,1,0.866025,0.5]
    scaleLeaf2 =  [1,1,1.4,1.4,0.8,0.8,0.4,0.4,0,0]

    posLeaf3 = [0, 4, 0]
    scaleLeaf3G = [0.5,0.5,0.5]
    spineLeaf3 = [0,0.5,0,0,1,0,0,1.5,0]
    crossSectionLeaf3 = [-1,0,-0.707106,0.707106,0,1, 0.707106,0.707106,1,0,0.866025,0.5,0.866025,-0.5,0,-1, -0.866025,-0.5,-0.866025,0.5,0,1,0.866025,0.5]
    scaleLeaf3 =  [1,1,1.4,1.4,0.8,0.8,0.4,0.4,0,0]


    def __init__(self, X=0, Y=0, Z=0):
        self.posTree = [X,Y,Z]

    def toString(self):
        stri = "Transform {\n"
        stri += "\ttranslation " + "  ".join(str(x) for x in self.posTree) + "\n"
        stri += "\tscale " + "  ".join(str(x) for x in self.scaleTree) + "\n"
        stri += "\tTransform {\n"
        stri += "\t\tscale " + "  ".join(str(x) for x in self.posTree) + "\n"
        stri += "\t\tChildren [\n"
        stri += "\t\t\tShape {\n"
        stri += "\t\t\t\tappearance Appearance {\n"
        stri += "\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\tdiffuseColor " + "  ".join(str(x) for x in self.colorTrunk) + "\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\tccw TRUE\n"
        stri += "\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineTrunk, 5) + "]\n"
        stri += "\t\t\t\t\tscale [\n"
        stri += listStr2(self.scaleTrunk, 5) + "]\n"
        stri += "\t\t\t\t\tcrossSection [\n"
        stri += listStr2(self.crossSectionTrunk, 5) + "]\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t}\n"
        stri += "\t\t]\n"
        stri += "\t}\n"

        stri += "\tTransform {\n"
        stri += "\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf1) + "\n"
        stri += "\t\tscale " + "  ".join(str(x) for x in self.scaleLeaf1G) + "\n"
        stri += "\t\tChildren [\n"
        stri += "\t\t\tShape {\n"
        stri += "\t\t\t\tappearance	Appearance {\n"
        stri += "\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\tdiffuseColor "+ " ".join(str(x) for x in self.colorLeaf) + "\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineLeaf1, 5) + "]\n"
        stri += "\t\t\t\t\tscale [\n"
        stri += listStr3(self.scaleLeaf1, 5) + "]\n"
        stri += "\t\t\t\t\tcrossSection [\n"
        stri += listStr3(self.crossSectionLeaf1, 5) + "]\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t}\n"
        stri += "\t\t]\n"
        stri += "\t}\n"

        stri += "\tTransform {\n"
        stri += "\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf2) + "\n"
        stri += "\t\tscale " + "  ".join(str(x) for x in self.scaleLeaf2G) + "\n"
        stri += "\t\tChildren [\n"
        stri += "\t\t\tShape {\n"
        stri += "\t\t\t\tappearance	Appearance {\n"
        stri += "\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\tdiffuseColor "+ " ".join(str(x) for x in self.colorLeaf) + "\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineLeaf2, 5) + "]\n"
        stri += "\t\t\t\t\tscale [\n"
        stri += listStr3(self.scaleLeaf2, 5) + "]\n"
        stri += "\t\t\t\t\tcrossSection [\n"
        stri += listStr3(self.crossSectionLeaf2, 5) + "]\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t}\n"
        stri += "\t\t]\n"
        stri += "\t}\n"

        stri += "\tTransform {\n"
        stri += "\t\ttranslation " + "  ".join(str(x) for x in self.posLeaf3) + "\n"
        stri += "\t\tscale " + "  ".join(str(x) for x in self.scaleLeaf3G) + "\n"
        stri += "\t\tChildren [\n"
        stri += "\t\t\tShape {\n"
        stri += "\t\t\t\tappearance	Appearance {\n"
        stri += "\t\t\t\t\tmaterial Material {\n"
        stri += "\t\t\t\t\t\tdiffuseColor "+ " ".join(str(x) for x in self.colorLeaf) + "\n"
        stri += "\t\t\t\t\t}\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t\tgeometry Extrusion {\n"
        stri += "\t\t\t\t\tspine [\n"
        stri += listStr3(self.spineLeaf3, 5) + "]\n"
        stri += "\t\t\t\t\tscale [\n"
        stri += listStr3(self.scaleLeaf3, 5) + "]\n"
        stri += "\t\t\t\t\tcrossSection [\n"
        stri += listStr3(self.crossSectionLeaf3, 5) + "]\n"
        stri += "\t\t\t\t}\n"
        stri += "\t\t\t}\n"
        stri += "\t\t]\n"
        stri += "\t}\n"

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
    print myTree.toString()
