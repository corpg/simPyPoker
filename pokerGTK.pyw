# -*- coding: cp1252 -*-

#Import des modules graphique
import pygtk
pygtk.require('2.0')
import gtk

from sys import exit

#import du jeu python
import pokerFunc as poker
from pokerClass import * #les joueurs et les bots possèdent les mème méthodes pour simplifier la programmation du jeu

class interfaceGraphique:
	def __init__(self, nomFenetre):
		self.fenetre = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.fenetre.set_title(nomFenetre)
		self.fenetre.connect("delete-event", self.destroy, "quit") #si on cherche a detruire la fenetre, on ouvre une boite de dialogue
		self.fenetre.set_border_width(15)
		self.fenetre.set_position(gtk.WIN_POS_CENTER) #pour centrer la fenetre

		#creation d'une boite principale
		boite = gtk.VBox(False, 1)
		self.fenetre.add(boite)
		
		#sous boite pour afficher du texte
		self.frame = gtk.HBox(False, 3) #tout les elements ont la meme taille
		boite.pack_start(self.frame, padding = 10) #par defaut le texte prend toute la place disponible

		#sous boite pour le croupier
		self.croupier = gtk.HBox(True, 3)
		boite.pack_start(self.croupier, padding = 5)
				
		#sous boite pour les boutons
		self.BButton = gtk.HBox(True, 3)
		boite.pack_end(self.BButton, False, False) #on ne veut pas que les boutons s'ettire en largeur
		
		#Pour eviter d'utiliser plusieurs fenetre de dialogue de confirmation
		self.alreadyDialog = False
		
		
	def confirmationFenetre(self, typeConf):
		#Pour utiliser des messages de dialogues différents
		type = {
			"quit"	: "Etes-vous sur de vouloir quitter ?",
			"cancel"	: "Etes-vous sur de vouloir annuler ?",
		}
		
		#on cree une boite de dialogue
		self.confirmation = gtk.Dialog("Confirmation", self.fenetre, gtk.DIALOG_NO_SEPARATOR)
		self.confirmation.set_border_width(5)
		self.confirmation.set_position(gtk.WIN_POS_CENTER_ON_PARENT) #pour que la fenetre de confirmation s'ouvre au centre de la fenetre principale
		self.confirmation.connect("focus_out_event", self.getFocus) #pour eviter la perte du focus
		
		
		#on insere du texte
		texte = gtk.Label(type[typeConf])
		self.confirmation.vbox.pack_start(texte)
		texte.show()
		
		#on cree le premier bouton
		bouton = gtk.Button(stock = gtk.STOCK_YES)
		bouton.connect("clicked", self.destroy, True)
		self.confirmation.action_area.pack_start(bouton) #on ajoute le bouton a la boite
		bouton.show()
		
		#on cree le premier bouton
		bouton = gtk.Button(stock = gtk.STOCK_NO)
		bouton.connect("clicked", self.destroy, False)
		self.confirmation.action_area.pack_start(bouton) #on ajoute le bouton a la boite
		bouton.show()
		

		self.confirmation.show()
		self.alreadyDialog = True
		
	
	def getFocus(self, widget, evenement):
		widget.present()
	
	
	def destroy(self, widget, typeDest=None, evenement=None):		
		if(typeDest==True) or (evenement=="quit"): #si confirmation = oui
			gtk.main_quit()
			exit()
			
		elif(typeDest==False): #si confirmation = non
			self.confirmation.destroy()
			self.alreadyDialog = False

		elif(not self.alreadyDialog): #si aucune confirmation
			self.confirmationFenetre(typeDest)
			
		else: #si une fenetre de confirmation est deja ouverte
			pass
		
		
	def launch(self, widget):
		self.fenetre.destroy()
		gtk.main_quit()
			
	def boucle(self):
		#On affiche tout
		self.fenetre.show_all()
		gtk.main()	
		
	
	# ----------------------------------------------------------- Pour parametrer le jeu --------------------------------------------------------#
	def setup(self, nBot, nomJoueur):
		self.fenetre.set_default_size(300, 100) #taille de la fenetre
		
		#bouton pour annuler
		button = gtk.Button(stock = gtk.STOCK_CANCEL)
		button.connect("clicked", self.destroy, "quit")
		self.BButton.pack_start(button)
		
		#bouton pour lancer le jeu
		button = gtk.Button("Jouer")
		button.connect("clicked", self.launch)
		self.BButton.pack_start(button)
		
		#creation d'une boite horizontale
		boite = gtk.VBox(True, 0)
		self.frame.pack_start(boite, True, True, 0)
		
		#creation d'une boite horizontale
		boiteA = gtk.HBox(False, 2)
		boite.pack_start(boiteA, True, True, 5)
		
		#creation d'une boite horizontale
		boiteB = gtk.HBox(False, 2)
		boite.pack_start(boiteB, True, True, 5)
		
		#Etiquette du champs du nom
		etiquette = gtk.Label("Entre votre nom: ")
		boiteA.pack_start(etiquette, False, False, 0)
		
		#Champs de saisie du nom
		nom = gtk.Entry(0)
		nom.set_text(nomJoueur)
		nom.select_region(0, 120)
		nom.set_editable(True)
		nom.connect("changed", self.setPlayerName)
		boiteA.pack_start(nom, True, True, 0)
		
		#Etiquette du gradateur
		etiquette = gtk.Label("Nombre de bots: ")
		boiteB.pack_start(etiquette, False, False, 0)
		
		#Gradateur pour modifier le nombre de bots
		ajust = gtk.Adjustment(nBot, poker.nombreMinBot, poker.nombreMaxBot, 1.0, 1.0, 0.0)
		ajust.connect("value_changed", self.addBot)
		gradateur = gtk.HScale(ajust)
		gradateur.set_digits(0)
		gradateur.set_draw_value(True)
		boiteB.pack_start(gradateur, True, True, 0)
		
	def addBot(self, widget):
		global nBot
		nBot = widget.value
		
	def setPlayerName(self, widget):
		global nom
		nom = widget.get_text()
		
	# ----------------------------------------------------------- Pour la fenetre du jeu --------------------------------------------------------#	
	def game(self, nomJoueur, nBot):
		self.fenetre.set_default_size(400, 140) #taille de la fenetre
		
		#Initialisation du jeu
		initIngame()
		self.round = 0
		
		#initialisation des bots et affichage
		self.bots = BotClass(nBot)
		self.bots.setGame()
		autresJoueurs = "\n"
		i=0
		for bot in self.bots.getNom():
			if(i%2==0):
				autresJoueurs += " - %s" % (bot)
			else:
				autresJoueurs += "\t|  - %s\n" % (bot)
			i+=1
		if((i-1)%2==0):
			autresJoueurs += "\n"
		affiche(self.frame, "Autres Joueurs", autresJoueurs, gtk.JUSTIFY_LEFT)
	
		#Initialisation joueur et affichage
		self.joueur = Players(nomJoueur)
		self.joueur.setGame()
		etiquetteJoueur1 = affiche(self.frame, self.joueur.getNom(), "%s" % (self.joueur))

		#Affiche le jeu du croupier
		etiquetteCroupier = affiche(self.croupier, "Croupier", "")

		#bouton Setup
		button = gtk.Button("Setup")
		button.connect("clicked", self.launch)
		self.BButton.pack_start(button)		
		
		#bouton pour redistribuer les cartes
		button = gtk.Button("Distribuer")
		button.connect("clicked", self.reloadGame, etiquetteJoueur1)
		self.BButton.pack_start(button)

		#bouton pour distribuer les cartes du croupier
		button = gtk.Button("Commencer")
		button.connect("clicked", self.startGame, etiquetteCroupier)
		self.BButton.pack_start(button)
		
		#bouton Quitter
		button = gtk.Button(stock = gtk.STOCK_QUIT)
		button.connect("clicked", self.destroy, "quit")
		self.BButton.pack_start(button)
		
		
	def reloadGame(self, widget, etiquette):
		initIngame() #initialisation des cartes jouees
		self.round = 0
		
		self.joueur.setGame() #redistribution des cartes au joueur
		etiquette.set_text("%s" % (self.joueur)) #affichage	
		self.bots.setGame() #redistribution des cartes aux bots

	def startGame(self, widget, etiquette):
		if(self.round<3):
			croupierCarte(self.round)
			etiquette.set_text(jeuCroupier())
			self.round += 1
	
	
		
# ------------------------------------------- Fonction pour afficher facilement des etiquettes ------------------------------
def affiche(parent, nom, texte, type = gtk.JUSTIFY_FILL):
	cadre = gtk.Frame(nom) #on cree un cadre pour afficher le texte
	etiquette = gtk.Label(texte) #on cree le label du cadre
	etiquette.set_justify(type) #on justifie le texte !
	
	cadre.add(etiquette) #on ajoute le label au cadre		
	parent.pack_end(cadre, padding = 1) #on ajoute notre cadre a la boite frame
	
	return etiquette

	

if __name__ == "__main__":
	jeu = True
	nom = ""
	nBot = 2
	
	while(jeu):
		setup = interfaceGraphique("PokerGTK Setup")
		setup.setup(nBot, nom)
		setup.boucle()
		del setup
		
		fenetreJeu = interfaceGraphique("PokerGTK 0.0.2a")	
		fenetreJeu.game(nom, nBot)
		fenetreJeu.boucle()
		del fenetreJeu