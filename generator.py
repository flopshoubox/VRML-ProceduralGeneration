# -*-coding:Latin-1 -*
#programme créant une surface de taille "taille" (taille doit être égal à 2^n+1) à l'aide de l'algorithme carré-diamant.
#programme implémentant une relation heure de la journée, couleur du ciel et orientation de la lumière
import os

from math import pow

from random import randint

def carreDiamant(taille,facteur):
	
	if facteur > 1:
		facteur =1
		pass
	liste = [[0] * taille for _ in range (taille)]
	liste[0][0]=int(facteur * randint(-taille,taille))
	liste[0][taille-1]=int(facteur * randint(-taille,taille))
	liste[taille-1][0]=int(facteur * randint(-taille,taille))
	liste[taille-1][taille-1]=int(facteur * randint(-taille,taille))
	i = taille - 1
	while i > 1:
		j = i / 2
		x = j
		for x in xrange(j,taille,i):
			for y in xrange(j,taille,i):
				moyenne = ( liste[x - j][y - j] + liste[x - j][ y + j] + liste[x + j][y + j] + liste[x + j][ y - j] ) / 4
				liste[x][y] = moyenne + int(facteur * randint(-j,j))
				pass
			pass
		for x in xrange(0,taille,j):
			if x % i == 0:
				decalage = j
			else:
				decalage = 0
			for y in xrange(decalage,taille,i):
				somme = 0
				n = 0
				if x >= j:
					somme += liste[x-j][y]
					n += 1
				if x + j < taille:
					somme += liste[x +j][y]
					n += 1
				if y >= j:
					somme += liste[x][y-j]
					n += 1
				if y + j < taille:
					somme += liste[x][y+j]
					n += 1
					liste[x][y] = somme / n + int(facteur * randint(-j,j))
				y += i
				pass				
			pass
		i = j
		pass
	return liste

def colourTemperature(heure):
	#4 positions : levé/couché, 1 heure avant/après, moyen été, midi été.
	rgbFinalColour = [1,0.53,0.05, 1,0.75,0.55, 1,0.83,0.70, 1,0.92,0.86]
	sortie = [0,0,0]
	for x in xrange(0,3):
		sortie[x] =rgbFinalColour[heure * 3 + x]
		pass
	return sortie

def intensity(heure):
	finalIntensity = [0.4, 0.5, 0.8, 1]
	for x in xrange(0,3):
		intensity = finalIntensity[heure]
		pass
	return intensity

def lightAngle(heure):
	angleX = [0.9, 0.8, 0.2, 0]
	angleY = [-0.1, -0.2, -0.8, -1]
	angles = [0,0]
	angles [0] = angleX[heure] 
	angles [1] = angleY[heure]
	return angles


