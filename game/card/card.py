#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.card.card
# Classe Card qui correspond à une carte unique dans le jeu.
# 20 décembre 2009

from random import randint as rand
from definitions import cartes

class Card(object):
    """
    Carte unique du jeu.
    
    La valeur d'une carte) est stockée sous la forme 'xxcc' où xx correspond à la valeur numérique (2, 3, 4, ..., 11 pour un valet, 12 pour une dame, 13 pour un roi et 14 pour l'as) et cc à la valeur littérale ('tr' pour trèfle, 'co' pour coeur, 'ca' pour carreau et 'pi' pour pique).
    
    Pour accéder à la valeur de la carte:
        - value_num: valeur numérique de la carte ('xx')
        - value_lit: valeur littérale de la carte ('cc')
    """
    _ingame = list() # stocke l'ensemble des cartes distribuées.
    
    def __init__(self):
        doublons = True;
        while(doublons):
            self._value = cartes.keys()[rand(0,51)]                
            if self._value not in self._ingame:
                self._ingame.append(self._value)
                doublons = False
                
    def __cmp__(self, other):
        return cmp(int(self.value_num), int(other.value_num))
        
    def __str__(self):
        return cartes[self._value]
        
    def __repr__(self):
        return "<Card value='%s'>" % self._value
        
    @classmethod
    def reset(cls):
        """ Vide la liste des cartes en jeu afin de pouvoir démarrer une nouvelle partie. """
        cls._ingame = list()
        
    @property
    def value_num(self):
        """ Retourne la valeur numérique de la carte. """
        return int(self._value[0:2])
        
    @property
    def value_lit(self):
        """ Retourne la valeur littérale de la carte. """
           return self._value[2:]
