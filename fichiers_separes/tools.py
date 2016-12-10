# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:19:56 2016

@author: Paloma
"""

#---------------------------Fonctions utiles
class ErrorIndex (Exception): #Exception pour les indices à l'extérieur de la grille
    pass

class ErrorValue(Exception): #Exception pour des valeurs non acceptables par la grille
    pass

class ErrorAccessible(Exception): #Exception si on essaye de jouer dans une case non autorisee
    pass



#Fonction qui lève une exception si le couple est en-dehors de la grille 
def verify_bounds(i,j,size):
    if not (i>=0 and j>=0 and i<size and j<size):
        raise ErrorIndex
        
        
#Fonction qui lève une exception si on rentre une valeur non acceptable (ne correpondant à aucun joueur) dans la grille 
def verify_value(elem):
    if not (abs(elem)==1):
        raise ErrorValue