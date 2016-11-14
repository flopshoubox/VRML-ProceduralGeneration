# -*-coding:Latin-1 -*
#programme créant une surface de taille "taille" (taille doit être égal à 2^n+1) à l'aide de l'algorithme carré-diamant.
#programme implémentant une relation heure de la journée, couleur du ciel et orientation de la lumière
import os

from math import pow
from TreeClass.RandTree import randTree
from random import randint

def carreDiamant(taille,facteur):
	
	if facteur > 1:
		facteur =1
		pass
	profondeurMax = -30
	hauteurMax = 100
	liste = [[0] * taille for _ in range (taille)]
	liste[0][0]=int(facteur * randint(profondeurMax,hauteurMax))
	liste[0][taille-1]=int(facteur * randint(profondeurMax,hauteurMax))
	liste[taille-1][0]=int(facteur * randint(profondeurMax,hauteurMax))
	liste[taille-1][taille-1]=int(facteur * randint(profondeurMax,hauteurMax))
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
	rgbFinalColour = [0.5,0.5,0.5, 0.7,0.7,0.7, 0.8,0.8,0.8, 1,1,1]
	sortie = [0,0,0]
	for x in xrange(0,3):
		sortie[x] =rgbFinalColour[heure * 3 + x]
		pass
	return sortie

def intensity(heure):
	finalIntensity = [0.6, 0.7, 0.8, 0.9]
	intensity = finalIntensity[heure]
	return intensity

def lightAngle(heure):
	angleX = [0.9, 0.8, 0.2, 0]
	angleY = [-0.1, -0.2, -0.8, -1]
	angles = [0,0]
	angles [0] = angleX[heure] 
	angles [1] = angleY[heure]
	return angles

def elevationGridColor(taille,grid):
	sortie = [["0 0 0"] * (taille-1) for _ in range (taille-1)]
	for x in xrange(taille-1):
			for y in xrange(taille-1):
				moyenne = ( ( grid[x][y] + grid[x+1][y] + grid[x][y+1] + grid[x+1][y+1] ) / 4)
				if moyenne < 0:
					sortie [x][y] = "0 0.1 0.5"
					pass
				elif moyenne < 3:
					sortie [x][y] = "0.15 0.3 0"
					pass
				elif moyenne < 50:
					sortie [x][y] = "0 0.6 0"
					pass
				else :
					sortie [x][y] = "1 1 1"
					pass
				pass
			pass
	return sortie
def treePlacer(taille,grid,space):
	sortie = ""
	for x in xrange(taille-1):
			for z in xrange(taille-1):
				minY = min(grid[x][z],grid[x][z+1],grid[x+1][z],grid[x+1][z+1])-0.5
				posX = z*space+space/2
				posZ = x*space+space/2
				proba = randint(0,20)
				if proba < 1 and grid[x][z] > 3:
					if grid[x][z] <= 20:
						sortie += randTree(posX,minY,posZ,3,0) + "\n"
						pass
					elif grid[x][z] <= 35:
						sortie += randTree(posX,minY,posZ,3,1) + "\n"
						pass
					elif grid[x][z] <= 50:
						sortie += randTree(posX,minY,posZ,3,2) + "\n"
						pass
					elif grid[x][z] > 50:
						sortie += randTree(posX,minY,posZ,3,3) + "\n"
						pass
					pass
	return sortie



