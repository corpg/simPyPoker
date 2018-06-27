#*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.card.definitions
# Dictionnaires contenant l'ensemble des cartes utilisées ainsi que les combinaisons possibles.
# Utilisés principalement pour permettre l'affichage des cartes.
# 20 décembre 2009

cartes = {

    #coeur
    '14co': 'As de coeur',
    '02co': '2 de coeur',
    '03co': '3 de coeur',
    '04co': '4 de coeur',
    '05co': '5 de coeur',
    '06co': '6 de coeur',
    '07co': '7 de coeur',
    '08co': '8 de coeur',
    '09co': '9 de coeur',
    '10co': '10 de coeur',
    '11co': 'Valet de coeur',
    '12co': 'Dame de coeur',
    '13co': 'Roi de coeur',

    #carreau
    '14ca': 'As de carreau',
    '02ca': '2 de carreau',
    '03ca': '3 de carreau',
    '04ca': '4 de carreau',
    '05ca': '5 de carreau',
    '06ca': '6 de carreau',
    '07ca': '7 de carreau',
    '08ca': '8 de carreau',
    '09ca': '9 de carreau',
    '10ca': '10 de carreau',
    '11ca': 'Valet de carreau',
    '12ca': 'Dame de carreau',
    '13ca': 'Roi de carreau',

    #trèfle
    '14tr': 'As de trefle',
    '02tr': '2 de trefle',
    '03tr': '3 de trefle',
    '04tr': '4 de trefle',
    '05tr': '5 de trefle',
    '06tr': '6 de trefle',
    '07tr': '7 de trefle',
    '08tr': '8 de trefle',
    '09tr': '9 de trefle',
    '10tr': '10 de trefle',
    '11tr': 'Valet de trefle',
    '12tr': 'Dame de trefle',
    '13tr': 'Roi de trefle',
    
    #pique
    '14pi': 'As de pique',
    '02pi': '2 de pique',
    '03pi': '3 de pique',
    '04pi': '4 de pique',
    '05pi': '5 de pique',
    '06pi': '6 de pique',
    '07pi': '7 de pique',
    '08pi': '8 de pique',
    '09pi': '9 de pique',
    '10pi': '10 de pique',
    '11pi': 'Valet de pique',
    '12pi': 'Dame de pique',
    '13pi': 'Roi de pique'
}

combinaisons = {
    0: 'une Carte Haute',
    1: 'une Paire',
    2: 'une Double Paire',
    3: 'un Brelan',
    4: 'une Suite',
    5: 'une Couleur à %s %s',
    6: 'un Full',
    7: 'un Carre de %s',
    8: 'une Quinte Flush %s',
    9: 'une Quinte Flush Royale !'
}

disp = {
    2   : 'deux',
    3   : 'trois',
    4   : 'quatre',
    5   : 'cinq',
    6   : 'six',
    7   : 'sept',
    8   : 'huit',
    9   : 'neuf',
    10  : 'dix',
    11  : 'valet',
    12  : 'dame',
    13  : 'roi',
    14  : 'as',
    'tr': 'trefle',
    'pi': 'pique',
    'ca': 'carreau',
    'co': 'coeur'
}
