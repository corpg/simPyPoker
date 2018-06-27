#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.players.bot.py
# Définit un Bot et les Bots, l'ensemble des bots du jeu.
# 20 décembre 2009

from default import DefaultPlayer

# TODO: Rendre la classe Bots itérable !
# TODO: Commenter d'avantage le code

class Bots:
    """ Bots est une classe itérable qui gère l'ensemble des bots. Possède les même méthodes / attributs """
	def __init__(self, nb):
		self.bots = [Bot(i) for i in range(1, nb+1)]
		self.nb = nb
				
	def __str__(self):
		texte = [str(b) for b in self.bots]
		return '\n'.join(texte)
				
	def setGame(self):
		for p in self.bots:
			p.setGame()
			
	def getGame(self):
		game = []
		for p in self.bots:
			game.append(p.getGame())
		return game
		
	def stopGame(self, idBot):
		self.bots[idBot-1].stopGame()
	
	def mise(self, money, idBot):
		if(idBot==-1):
			for bot in self.bots:
				bot.mise(money)
		else:
			self.bots[idBot-1].mise(money)
		
	def getMoney(self):
		money = []
		for p in self.bots:
			money.append(p.getMoney())
		return money
		
	def win(self, idBot):
		return self.bots[idBot-1].win()
		
	def getNom(self):
		nom = []
		for p in self.bots:
			nom.append(p.getNom())
		return nom
		
	def getFlop(self):
		flop = []
		for p in self.bots:
			flop.append(p.getFlop())
		return flop
		
	def getCombinaison(self):
		combi = []
		for p in self.bots:
			combi.append(p.getCombinaison())
		return combi
		
		
class Bot(DefaultPlayer):
    """ Classe Bot """
    def __init__(self, numero):
        DefaultPlayer.__init__(self, "Bot n°%d" % numero)
