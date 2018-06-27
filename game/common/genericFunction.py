# -*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.common.genericFunction.py
# Fonctions génériques utilisées par certains composants du jeu simplifiants certains processus.
# 20 décembre 2009
	
# Fonction permetant de gérer les entrées avec l'utilisateur lors de la saisie d'un nombre.
# Le nombre saisie doit être compris entre la valeur min et max.
def getInt(invite, min, max):
	boucle = True
	while(boucle):
		n = raw_input(invite)
		
		try:
			n = int(n)
		except:
			print "Entrez un entier"
		else:
			if(min <= n <= max):
				boucle = False
			else:
				print "Entrez une valeur comprise entre %s et %s" % (min, max)
		
	return n
	
# Recupère le nom de l'utilisateur depuis l'entrée standard.
def getPlayerName():
	nom = ""
	while(nom == ""):
		nom = raw_input("Entrez votre nom: ")
			
	return nom

	
# Tri un tableau de cartes suivant l'ordre croissant
def sortCardArray(tab):
	lenght = len(tab)
	for i in range(0, lenght-1):
		max = tab[0]
		indice = 0
		print "\n", max, "-->",
		for j in range(1, lenght-i):
			if tab[j] > max:
				max = tab[j]
				indice = j
				print "Maximum Trouve a l'indice", j, ":", max
		print indice
		tab[indice] = tab[lenght-1]
		tab[lenght-1] = max
