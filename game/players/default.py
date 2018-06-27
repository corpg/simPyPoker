#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.players.player.py
# Classe Default décrivant les comportements par défaut d'un joueur de poker. Est héritée par Bot et Player. 
# 20 décembre 2009

from game.common.constants import CAVE
from game.card import Card
from game.card.definitions import disp

class DefaultPlayer(object):
    """ 
    Décrit les comportement par défaut d'un joueur (bot ou humain).
    
    Principaux évènements:
        - start_game(): à chaque début de partie,
        - stop_game(): à la fin de la partie ou lorsque le joueur se couche,
        - check(): lorsque le joueur ne souhaite pas relancer,
        - relance(mise): lorsque le joueur relance avec la mise en paramètre (doit-être inférieur à l'argent qu'il possède),
        - tapis(): lorsque le joueur mise tout ce qu'il possède,
        - win(montant): lorsque le joueur à gagné la partie, il recupère le montant du pot
    """
    def __init__(self, nom, money=CAVE):
        self.nom = nom
        self.play = False
        self.flop = 0
        self.cartes_flop = list()
        self.est_tapis = False
        self._money = money
        self._mise = 0
        self._main = list()
        
    def __repr__(self):
        return "<%s nom=%s money=%s main=%s>" % (self.__class__.__name__, self.nom, self._money, self._main)
        
    def __str__(self):
        e0 = if(self._main[0].value_num=="12") "une" else "un"
        e1 = if(self._main[1].value_num=="12") "une" else "un"
        return "%s possède %s %s et %s %s (%d credits restants)." % (self.nom, e0, self._main[0], e1, self._main[1], self._money)
            
    def start_game(self, blind):
        self._main = [Card(), Card()]
        self._money -= blind
        self._mise = blind
        self.play = True
        self.flop = 0
        self.cartes_flop = list()
        self.est_tapis = False
        
    def stop_game(self): 
        self._main = list() #lorsque le joueur se couche on détruit ses cartes
        
    def relance(self, mise):
        if mise >= self._money:
            self.tapis()
        else:
            self._money -= mise
            self._mise += mise
            
    def tapis(self):
        self._mise += self._money
        self._money = 0
        
    def check(self):
        pass
        
    def win(self, montant):
        self._money += montant

    @property
    def mise(self):
        """ Retourne la valeur l'attribut 'mise' en lecture seule. Ne pas surcharger ! """
        return self._mise
        
    @property
    def money(self):
        """ Retourne la valeur l'attribut 'money' en lecture seule. Ne pas surcharger ! """
        return self._money
    
    def get_flop(self, board=None):
        """ Retourne le flop, ou la combinaison, possédé par le joueur. Voir game.common.constants pour voir à quoi correspondent les différentes combinaisons par rapport au nombre retourné. """
        if not self._main or not self.play:
            return self.flop
            
        cartes = tuple(self._main + [c for c in board]) if board else self._main
            
        #initialisation des variables et tableaux utiles
        self.flop = 0 #carte haute
        self.cflop = [] #pour les paires, double paires, ect...
        suite = [] #pour les suite
        couleur = [] #pour les couleur
        suitePossible = [] #pour la suite qui est une suite
        
        for cartea in cartes:
            for carteb in cartes:
                if(cartea!=carteb) and (self.flop not in (6, 7, 8, 9)):
                    if(carteb[0:2]==cartea[0:2]): #on verifie la valeur
                        if(cartea not in self.cflop) and (carteb not in self.cflop):
                            if(self.flop==1):
                                self.flop = 2 #double paire
                            elif(self.flop==3):
                                self.flop = 6 #full
                            else:
                                self.flop = 1 #paire
                            self.cflop.append(cartea)
                            self.cflop.append(carteb)
                            
                        elif(carteb not in self.cflop):
                            if(self.flop==3):
                                self.flop = 7 #carree
                            elif(self.flop==2):
                                self.flop = 6 #full
                            else:
                                self.flop = 3#belan
                            self.cflop.append(carteb)
                            
                    if(carteb[2:4]==cartea[2:4]): #on verifie la couleur
                        if(cartea not in couleur) and (carteb not in couleur):
                            couleur.append(cartea)
                            couleur.append(carteb)
                            
                        elif(carteb not in couleur):
                            couleur.append(carteb)
                            
                            if(len(couleur)>=5):
                                fcouleur = {'co': 0, 'ca' : 0, 'tr' : 0, 'pi' : 0}
                                for carte in couleur:
                                    fcouleur[carte[2:4]]+=1
                                        
                                if 5 in fcouleur.values():
                                    if(self.flop == 4):
                                        self.flop = 8 #quinte flush
                                    else:
                                        self.flop = 5 #couleur

                                        for key in fcouleur:
                                            if(fcouleur[key]==5):
                                                max = 0
                                                for c in couleur:
                                                    if(c[2:4]==key) and (int(c[0:2])>max):
                                                        max = int(c[0:2])
                                                        maxc = c
                                                break
                                        self.cflop.append(maxc)
                                    
                                    

                    #on crée des entier une fois pour toutes...
                    intCartea = int(cartea[0:2])
                    intCarteb = int(carteb[0:2])
                    if(intCarteb==intCartea+1) or ((suite != []) and ((intCarteb==suite[0]-1) or (intCarteb==suite[-1]+1))):
                    
                        #Pour etre sur de ce qu'on ajoute dans le tableau suite
                        if(intCarteb not in suite) and (intCartea not in suite):
                            suite.append(intCartea)
                            suite.append(intCarteb)
                        elif(intCartea not in suite):
                            suite.append(intCartea)
                        elif(intCarteb not in suite):
                            suite.append(intCarteb)
                            
                        if(len(suite)>=5): #si au moins 5éléments dans le tableau, on cherche à savoir s'il peuvent former une suite
                            i = 0 #parcours du tableau avec des indices                            
                            suite.sort(reverse=True) #pour ranger par ordre croissant
                            while(i<len(suite) and len(suitePossible)!=5):
                                if((i!=(len(suite)-1)) and (suite[i]-1==suite[i+1])) or ((i==(len(suite)-1)) and (suite[i-1]==suite[i]+1)): #on est bien partit pour faire une suite ^^
                                    suitePossible.append(suite[i])
                                elif(i!=(len(suite)-1)) and (suite[i]!=suite[i+1]):
                                    suitePossible = [] #on réinitialise si impossible d'enchainer
                                
                                i+=1
                                
                                if((i!=len(suite)) and (suite[i]==suite[i-1])): #pour supprimer les doublons
                                    suite.remove(suite[i])
                                    
                            if(len(suitePossible)==5):
                                if(self.flop==5):
                                    if(suitePossible[0]==14):
                                        self.flop = 9 #quinte flush royale
                                    else:
                                        self.flop = 8 #quinte flush
                                else:
                                    self.flop = 4 #suite
                                    
                                if(suitePossible[0] not in self.cflop):
                                    self.cflop.append(suitePossible[0])
                                    
        if(self.flop==0):
            if(int(cartes[0][0:2])>int(cartes[1][0:2])):
                self.cflop.append(cartes[0])
            else:
                self.cflop.append(cartes[1])
                                    
        return self.flop
        
    def get_combinaison(self):
        if(self.flop==1): #paire
            p = int(self.cflop[0][0:2])
            if(11<= p <= 13):
                s = "s"
            else:
                s = ""
            return "de %s%s" % (disp[p], s)
            
        elif(self.flop==2): #double paire
            p1 = int(self.cflop[0][0:2])
            p2 = int(self.cflop[2][0:2])
            
            if(p1<p2):
                p1, p2 = p2, p1
                
            if(11<= p1 <= 13):
                s1 = "s"
            else:
                s1 = ""    
            if(11<= p2 <= 13):
                s2 = "s"
            else:
                s2 = ""
            return "de %s%s par les %s%s" % (disp[p1], s1, disp[p2], s2)
        
        elif(self.flop==3): #brelan
            br = int(self.cflop[0][0:2])
            if(11<= br <= 13):
                s = "s"
            else:
                s = ""
            return "de %s%s" % (disp[br], s)
            
        elif(self.flop==4): #suite
            p = int(self.cflop[-1][0:2])
            s = disp[p]
            if(11<=p<=13):
                return "aux %ss" % (s)
            else:
                return "au %s" % (s)
            
        elif(self.flop==5): #couleur
            return ""
        
        elif(self.flop==6): #full
            f1 = int(self.cflop[0][0:2])
            f2 = int(self.cflop[-1][0:2])
            
            if(f1<f2):
                f1, f2 = f2, f1
                
            
            if(11<= f1 <= 13):
                s1 = "s"
            else:
                s1 = ""    
            if(11<= f2 <= 13):
                s2 = "s"
            else:
                s2 = ""
                
            return "aux %s%s par les %s%s" % (disp[f1], s1, disp[f2], s2)
            
        elif(self.flop==7): #carre
            return ""
            
        elif(self.flop==8): #quinte flush
            return ""
            
        elif(self.flop==9): #quinte flush royale
            return ""
            
        else:
            return "par le %s" % (disp[int(self.cflop[0][0:2])])
