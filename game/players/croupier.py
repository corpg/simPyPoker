#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.players.croupier
# Définition d'une classe Croupier qui distribue les cartes. Pas utile mais simplifie la compréhension.
# 20 décembre 2009

class Croupier(object):
    """ Simple objet permettant de simplifier la compréhension du jeu. Le croupier se charge de distribuer les cartes du tableau (cartes positionnées face visible sur la table).
    
        Attribut:
            - board: list contenant l'ensemble des cartes du tableau (disponible pour les joueurs).
        
        Méthodes:
            - carte(): ajoute une nouvelle carte au tableau
            - brule(): une carte est tirée et est replacée dans le tas (la carte n'est plus disponible dans le jeu)
    """
    def __init__(self):
        self.board = [] # Le tableau constitue l'ensemble des cartes plaçées face visible sur la table
        
    def carte(self):
        """ Le croupier tire une nouvelle carte et l'ajoute au tableau.
        Ne retourne aucune valeur. """
        self.board.append(Card())
        
    def brule(self):
        """ Le croupier brule une carte, c'est-à-dire qu'il en tire une en la repositionnant dans le tas, la rendant indisonible pour les joueurs.
        Ne retourne aucune valeur."""
        Card()
