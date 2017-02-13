# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:19:56 2016
Fonctions élémentaires et classes d'exception
"""


#---------------------------Classes d'exception
class ErrorIndex (Exception): 
    """ Exception pour les indices à l'extérieur de la grille """
    pass

class ErrorValue(Exception): 
    """Exception pour des valeurs non acceptables par la grille"""
    pass

class ErrorAccessible(Exception): 
    """Exception si on essaye de jouer dans une case non autorisee"""
    pass

#---------------------------Fonctions utiles
def verify_bounds(i,j,size):
    """Arguments: indice i, indice j, entier <taille>
        Fonction qui lève une exception si on n'a pas 0<i<taille et 0<j<taille"""
    if not (i>=0 and j>=0 and i<size and j<size):
        raise ErrorIndex
              
def verify_value(elem):
    """Fonction qui lève une exception si on rentre une valeur non acceptable (ne correpondant à aucun joueur) dans la grille, cad si l'argument d'entrée n'est ni 1 ni -1"""
    if not (abs(elem)==1):
        raise ErrorValue