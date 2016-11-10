# -*-coding:Latin-1 -*

import generator
from TreeClass.RandTree import randTree
from math import pow
from random import randint

#Choix des parametres du programme
largeurMatrice = 5 #La matrice finale sera de taille 2^largeurMatrice+1
ratio = 10 #Il est multiplié à la valeur alératoire à ajouter à chaque point de la matrice
xSpacing = int(ratio*largeurMatrice/12)
zSpacing = int(ratio*largeurMatrice/12)

#Calcul du terrain
taille = int(pow(2,largeurMatrice))+1
gridElevation = generator.carreDiamant(taille,ratio)
gridColor = generator.elevationGridColor(taille,gridElevation)



#Calcul de la position de l'avatar
posX = str(pow(2,largeurMatrice-1)+1)
posY = "500"
posZ = str(pow(2,largeurMatrice-1)+1)

#Calcul des paramètresliés à l'heure dans la journée
heure = randint(0,3)
ambientLightColour = generator.colourTemperature(heure)
intensity = generator.intensity(heure)
angles = generator.lightAngle(heure)
angleX = str(angles[0])
angleY = str(angles[1])

#Création du fichier texte
mon_fichier = open("base.wrl", "w")
mon_fichier.write("#VRML V2.0 utf8")
mon_fichier.write("\n\tGroup {")
mon_fichier.write("\n\t\tchildren [")
mon_fichier.write("\n\t\t\tWorldInfo {")
mon_fichier.write("\n\t\t\t\ttitle \"Generation procedurale d'un terrain\"")
mon_fichier.write("\n\t\t\t\tinfo [ \"Auteur : Florent PERGOUD (perf13)")
mon_fichier.write("\n\t\t\t\t\t- automne 2016 - UQO")
mon_fichier.write("\n\t\t\t\t\tUtilisez la souris pour découvrir l'environnment.\"]")
mon_fichier.write("\n\t\t\t}")
mon_fichier.write("\n\t\t\tNavigationInfo {")
mon_fichier.write("\n\t\t\t\tavatarSize [0.25, 1.6, 0.75]")
mon_fichier.write("\n\t\t\t\theadlight FALSE")
mon_fichier.write("\n\t\t\t\tspeed 7.0")
mon_fichier.write("\n\t\t\t\ttype \"WALK\"")
mon_fichier.write("\n\t\t\t\tvisibilityLimit 800.0")
mon_fichier.write("\n\t\t\t}")
mon_fichier.write("\n\t\t\tViewpoint {")
mon_fichier.write("\n\t\t\t\tposition " + posX + " " + posY + " " + posZ + "# 500 pour être sûr de ne pas passer sous la carte")
mon_fichier.write("\n\t\t\t\torientation 0 0 0 0")
mon_fichier.write("\n\t\t\t}")
mon_fichier.write("\n\t\t\tBackground {")
mon_fichier.write("\n\t\t\t\tskyColor [0.165 0.616 0.843 0 0.882 1]")
mon_fichier.write("\n\t\t\t\tskyAngle [1.57 3.14]")
mon_fichier.write("\n\t\t\t}")
mon_fichier.write("\n\t\t\tDEF RayonsSolaires DirectionalLight {")
mon_fichier.write("\n\t\t\t\tdirection " + angleX + " " + angleY +" 0")
mon_fichier.write("\n\t\t\t\tintensity " + str(intensity))
mon_fichier.write("\n\t\t\t\tambientIntensity 1")
mon_fichier.write("\n\t\t\t\tcolor " + str(ambientLightColour[0]) + " " + str(ambientLightColour[1]) + " " + str(ambientLightColour[2]))
mon_fichier.write("\n\t\t\t}")

mon_fichier.write("\n\t\t\tTransform {")
mon_fichier.write("\n\t\t\t\tscale 1 1 1")
mon_fichier.write("\n\t\t\t\trotation 0 0 1 0")
mon_fichier.write("\n\t\t\t\ttranslation " + str(-taille) + " 0 " + str(-taille))
mon_fichier.write("\n\t\t\t\tchildren [")

mon_fichier.write("\n\t\t\t\t\tCollision {")
mon_fichier.write("\n\t\t\t\t\t\tchildren [")
mon_fichier.write("\n\t\t\t\t\t\t\tShape {")
mon_fichier.write("\n\t\t\t\t\t\t\t\tappearance Appearance {")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\tmaterial Material {")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t\tdiffuseColor 0.22 0.41 0.6")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t\t#emissiveColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t\t#specularColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t\tshininess 1")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t\ttransparency 0.3")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t\t\t\tgeometry ElevationGrid {")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\tccw TRUE")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t#normal NULL")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t#creaseAngle 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\tsolid FALSE")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\txDimension 2")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\txSpacing "+str(taille*xSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\t\t\tzDimension 2")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\tzSpacing "+str(taille*zSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\t\t\theight [")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t1,1,")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t1,1,")
mon_fichier.write("\n\t\t\t\t\t\t\t\t\t]")
mon_fichier.write("\n\t\t\t\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t\t\t\t}\n")
mon_fichier.write("\n\t\t\t\t\t\t]\n")
mon_fichier.write("\n\t\t\t\t\t\tcollide FALSE")
mon_fichier.write("\n\t\t\t\t\t}")

mon_fichier.write("\n\t\t\t\t\tShape {")
mon_fichier.write("\n\t\t\t\t\t\tappearance Appearance {")
mon_fichier.write("\n\t\t\t\t\t\t\tmaterial Material {")
mon_fichier.write("\n\t\t\t\t\t\t\t\tdiffuseColor 0.9 0.9 0.9")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#emissiveColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#specularColor 0 0 0")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#shininess 1")
mon_fichier.write("\n\t\t\t\t\t\t\t\t#transparency 0")
mon_fichier.write("\n\t\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t\tgeometry ElevationGrid {")
mon_fichier.write("\n\t\t\t\t\t\t\tccw TRUE")
mon_fichier.write("\n\t\t\t\t\t\t\t#normal NULL")
mon_fichier.write("\n\t\t\t\t\t\t\t#creaseAngle 0")
mon_fichier.write("\n\t\t\t\t\t\t\tsolid FALSE")
mon_fichier.write("\n\t\t\t\t\t\t\txDimension " + str(taille))
mon_fichier.write("\n\t\t\t\t\t\t\txSpacing " + str(xSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\tzDimension " + str(taille))
mon_fichier.write("\n\t\t\t\t\t\t\tzSpacing " + str(zSpacing))
mon_fichier.write("\n\t\t\t\t\t\t\theight [")
for x in gridElevation:
	tabTemporaire = x
	outputString = ', '.join(map(str,tabTemporaire))
	mon_fichier.write("\n\t\t\t\t\t\t\t" + outputString + ",")
	pass
mon_fichier.write("\n\t\t\t\t\t\t\t]")
mon_fichier.write("\n\t\t\t\t\t\t\tcolorPerVertex FALSE")
mon_fichier.write("\n\t\t\t\t\t\t\tcolor Color {")
mon_fichier.write("\n\t\t\t\t\t\t\t\tcolor [")
for x in gridColor:
	tabTemporaire = x
	outputString = ', '.join(map(str,tabTemporaire))
	mon_fichier.write("\n\t\t\t\t\t\t\t\t" + outputString + ",")
	pass
mon_fichier.write("\n\t\t\t\t\t\t\t\t]")
mon_fichier.write("\n\t\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t\t}")
mon_fichier.write("\n\t\t\t\t\t}\n")
#Adding trees
mon_fichier.write(generator.treePlacer(taille,gridElevation))

mon_fichier.write("\n\t\t\t\t]")
mon_fichier.write("\n\t\t\t}")
mon_fichier.write("\n\t\t]")
mon_fichier.write("\n\t}")
mon_fichier.close()
