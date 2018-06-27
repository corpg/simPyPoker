#*- coding: cp1252 -*-

#Code et POO: Etienne
#Idée et concept: Florian
#All Right Reserved 2008
#Version:  0.1 beta

import random
from player.croupier import Croupier
from common.constant import miseMinimale, cave
from card import cartes, dicoCartes

#------------------ Fonction pour initialiser le jeu -------------------#
class InitGame:
	def __init__(self):
		self.ingame = [] #pour stocker les cartes deja distribuees
		self.pot = 0
	def ajoutIngame(self, carte):
		self.ingame.append(carte)
	def ajoutPot(self, money):
		self.pot += money
	def getPot(self):
		return self.pot
	def getIngame(self):
		return self.ingame	
	
def initIngame():
	global ig, cr
	
	try:
		del ig
		del cr
	except:
		pass
		
	ig = InitGame()
	cr = Croupier()
	
def jeuCroupier():
	jeu = cr.getCarte()
	
	texte = "Cartes tirees:\n"
	for c in jeu:
		texte += "\t%s" % (c.getNom())
		
	return texte
	
def croupierCarte(round):
	if(round==0):
		cr.bruleCarte()
		cr.setCarte()
		cr.setCarte()
		cr.setCarte()
	else:
		cr.bruleCarte()
		cr.setCarte()
		
