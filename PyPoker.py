#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: PyPoker
# 'Main'
# 20 décembre 2009

import game

jeu = True

#on cree le joueur principal	
joueur = Players(poker.getPlayerName())

#on cree les bots
nBot = poker.getInt("Combien de bots ?\t", poker.nombreMinBot, poker.nombreMaxBot)
bot = BotClass(nBot)


while(jeu):
	initIngame() #on initialise le tableau des cartes utilisees en jeu et le croupier
	ingameBot = nBot
	outgameBot = []
	onlyBot = False
	 
	#Initialisation des jeux des groupes de joueurs (class PlayerGrp)
	joueur.setGame()
	bot.setGame()
	
	#Affichage des jeux des groupes de joueurs (class PlayerGrp)
	print joueur
	#print bot
	
	round = 0
	while(round<4):
		if not onlyBot: 
			miseJoueur = poker.getInt("Souhaitez-vous miser (0 pour checker, -1 pour quitter)", -1, joueur.getMoney())
		
			if miseJoueur == -1: #revoir le procedure puisqu'il n'y aura que des bots qui joue ==> tirage automatique
				joueur.stopGame()
				print "%s se couche." % (joueur.getNom())
				onlyBot = True
				
			else:
				joueur.mise(miseJoueur)
			
				#reaction des bots
				i = 1			
				for f in bot.getFlop():
					if(i in outgameBot):
						pass
					elif(f < poker.flopMinBot[round] or miseJoueur > 300):
						bot.stopGame(i)
						print "%s se couche." % (bot.getNom()[i-1])
						ingameBot -= 1
						outgameBot.append(i)
					else:
						bot.mise(miseJoueur, i)
					i+=1
					
		if(ingameBot==0):
			credit = joueur.win()
			print "Vous avez gagne (+%d credits)" % credit
			round = 5
		
		else:
			
			#Tirages des cartes
			if(round<3):
				croupierCarte(round)
					
				print jeuCroupier()
				if not onlyBot:
					print "\n%s" % (joueur)
					print "Vous avez %s\n\n" % (poker.combinaison[joueur.getFlop()])
					
			else: #fin de la partie et affichage du gagnant
				i = 0
				flop = 0
				for f in bot.getFlop():
					if(f >= flop):
						winBot = i
						flop = f
					i += 1
					
				flopJoueur = joueur.getFlop()
				if(flop==flopJoueur):
					print "No winner..."
				else:
					if(flop<flopJoueur): #==> gérer les fops suivants les cartes
						winner = joueur.getNom()
						credit = joueur.win()
						flop = joueur.getFlop()
						combi = joueur.getCombinaison()
					else:
						winner = bot.getNom()[winBot]
						credit = bot.win(winBot)
						combi = bot.getCombinaison()[winBot]

					print "\n%s a gagne avec %s %s. (+%d credits)" % (winner, poker.combinaison[flop], combi, credit)
			
			round += 1
			
	print "********* END GAME *************"
	
	if(raw_input("\nPartie terminee. 'stop' pour ne pas rejouer !") == "stop"):
		jeu = False
