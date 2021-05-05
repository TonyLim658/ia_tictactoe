# ia_tictactoe
Projet initié suite aux cours de *Modélisation & Vérification*.

# Description
Jeu de morpion avec une IA générée à l'aide de minimax, un algorithme d'arbre de jeu, qui permet en amont de détecter le meilleur coup à jouer pour gagner.

# Explications
L'arbre de jeu a été créé par **memoization**. L'arbre est un dictionnaire qui contient tous les états du jeu, sans redondance, ayant des états enfants. Un noeud qui est une feuille, qui n'a pas d'état enfant, possède un score qui a été trouvé par checkState. 
L'algorithme minimax permet de faire remonter le score jusqu'au noeud racine pour savoir quel chemin emprunter en fonction de l'état du jeu.
