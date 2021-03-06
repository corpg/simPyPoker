# -*- coding: utf-8 -*-
# Etienne Glossi - etienne.glossi@gmail.com
# PyPoker: game.common.constant.py
# Fichiers contenant des constantes modifiables par l'utilisateur afin qu'il puisse adapter certains paramètres du jeu.
# 20 décembre 2009

# TODO: Intégrer ces paramètres dans un fichier .ini ou .txt pour faciliter les modifications.

# La mise minimale pour entrer en jeu (blind)
MISE_MINIMALE = 10

# Ce que possède chaque joueur au début du jeu
CAVE = 1000

# Nombre maximum de bot en jeu
NB_MAX_BOTS = 9 

# Nombre minimal de bot en jeu
NB_MIN_BOTS = 1

# Flop minimum des bots pour qu'ils continuent aux rounds 1 à 5 (indice 0 à 4 du tableau)
FLOP_MIN_BOT = [0, 1, 1, 1, 1]
