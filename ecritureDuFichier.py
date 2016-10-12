# -*-coding:Latin-1 -*

import generator
from math import pow
#Choix des parametres du programme
largeurMatrice = 4 #La matrice finale sera de taille 2^largeurMatrice+1
ratio = 10 #Il est multiplié à la valeur alératoire à ajouter à chaque point de la matrice
xSpacing = int(ratio*largeurMatrice/13)
zSpacing = int(ratio*largeurMatrice/13)

#Calcul de la matrice
taille=int(pow(2,largeurMatrice))+1
tableau=generator.carreDiamant(taille,ratio)
tab2 = [ y for x in tableau for y in x]
outputString = ', '.join(map(str,tab2))

#Création du fichier texte
mon_fichier = open("sortie.wrl", "w")
mon_fichier.write("#VRML V2.0 utf8")
mon_fichier.write("\n\tGroup {")
mon_fichier.write("\n\t\tchildren [")
mon_fichier.write("\n\t\t\tWorldInfo {")
mon_fichier.write("\n\t\t\t\ttitle \"Paysage\"")
mon_fichier.write("\n\t\t\t\tinfo [ \"perf13 - automne 2016 - UQO \"]")
mon_fichier.write("\n\t\t\t}\n")
mon_fichier.write("\n\t\t\tNavigationInfo {")
mon_fichier.write("\n\t\t\t\tavatarSize [0.25, 1.6, 0.75]")
mon_fichier.write("\n\t\t\t\theadlight TRUE")
mon_fichier.write("\n\t\t\t\tspeed 5.0")
mon_fichier.write("\n\t\t\t\ttype \"WALK\"")
mon_fichier.write("\n\t\t\t\tvisibilityLimit 50.0")
mon_fichier.write("\n\t\t\t}\n")
mon_fichier.write("\n\t\t\t#Viewpoint {")
mon_fichier.write("\n\t\t\t\t#position 0" + str(tableau[(taille-1)/2+1][(taille-1)/2+1]) + "70")
mon_fichier.write("\n\t\t\t\t#orientation 0 0 0 0")
mon_fichier.write("\n\t\t\t#}\n")
mon_fichier.write("\n\t\t\t#Background {")
mon_fichier.write("\n\t\t\t\t#skyColor [0.165 0.616 0.843 0 0.882 1]")
mon_fichier.write("\n\t\t\t\t#skyAngle [1.57 3.14]")
mon_fichier.write("\n\t\t\t#}\n")
mon_fichier.write("\n\t\t\tTransform {")
mon_fichier.write("\n\t\t\t\tscale 1 1 1")
mon_fichier.write("\n\t\t\t\trotation 0 0 1 0")
mon_fichier.write("\n\t\t\t\ttranslation " + str(-taille) + " 0 " + str(-taille))
mon_fichier.write("\n\t\t\t\tchildren [")
mon_fichier.write("\n\t\t\t\t\tShape {")
mon_fichier.write("\n\t\t\t\t\t\tappearance Appearance {")
mon_fichier.write("\n\t\t\t\t\t\t\tmaterial Material {")
mon_fichier.write("\n\t\t\t\t\t\t\t\tdiffuseColor 0.7 0.7 0.7")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#emissiveColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#specularColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#shininess 1")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#transparency 0")
mon_fichier.write("\n\t\t\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t\t\tgeometry ElevationGrid {")
mon_fichier.write("\n\t\t\t\t\t\t\tccw TRUE")
mon_fichier.write("\n\t\t\t\t\t\t\tsolid FALSE")
mon_fichier.write("\n\t\t\t\t\t\t\tcreaseAngle 0")
mon_fichier.write("\n\t\t\t\t\t\t\txDimension " + str(taille))
mon_fichier.write("\n\t\t\t\t\t\t\txSpacing " + str(xSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\tzDimension " + str(taille))
mon_fichier.write("\n\t\t\t\t\t\t\tzSpacing " + str(zSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\theight [")
for x in tableau:
	tabTemporaire = x
	outputString2 = ', '.join(map(str,tabTemporaire))
	mon_fichier.write("\n\t\t\t\t\t\t\t\t" + outputString2 + ",")
	pass
mon_fichier.write("\n\t\t\t\t\t\t\t]")
mon_fichier.write("\n\t\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t]\n")
mon_fichier.write("\n\t\t\t}\n")
mon_fichier.write("\n\t\t]\n")
mon_fichier.write("\n\t}\n")
mon_fichier.close()