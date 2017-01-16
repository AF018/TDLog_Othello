# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:26:43 2016

@author: Paloma
"""

import tools
      
#-----------------------------------Classe Joueur
class Player:
    """Classe du joueur, qui prend en argument une chaine de caractère (le nom) et une valeur qui sera affectée au joueur."""
    
    #Initialisation
    def __init__(self, name, value):
        """Initialisation de la classe Player"""
        self._name=name
        self.score=0 #correspond au nombre de positions occupées
        self.used_positions=[] 
        self._value=value # valeur affectée au joueur
        
       
    #@property 
     
    def read_name(self):
        """Méthode qui ne prend pas d'argument et qui renvoie le nom du joueur """
        return(self._name)
        
    def read_score(self):
        """Méthode qui ne prend pas d'argument et qui renvoie le score du joueur """
        return (len(self.used_positions))
        
    def read_positions(self):
        """Méthode qui ne prend pas d'argument et qui renvoie la liste des positions occupées par le joueur sous forme d'une liste de doublets, chaque doublet étant le couple (i,j) des indices des positions"""
        return(self.used_positions)
    
    def read_value(self):
        """Méthode qui ne prend pas d'argument et qui renvoie la valeur affectée au joueur """
        return (self._value)
        
    def occupy_position(self,i,j):
        """Méthode qui prend en argument deux entiers i et j et qui ajoute la position (i,j) à la liste des positions occupées par le joueur"""
        try:
            self.used_positions.append((i,j)) #On ajoute la position à la liste des positions occupées           
        except tools.ErrorIndex: #Tritement de l'exception
            print("Hors de la grille ....")
    
    def no_more_occupy_position(self,i,j):
        """ Méthode qui prend en argument un couple d'enters (i,j) et qui les enlève de la liste des positions occupées par le joueur."""
        try:
            #verify_bounds(i,j,8)       #BOF ATTENTION ON FAIT DEJAINTERVENIR LA GRILLE... PPLUTOT A METTRE DANS LE JEU   
            self.used_positions.remove((i,j)) #On ajoute la position à la liste des positions occupées
        except tools.ErrorIndex: #Traitement de l'exception
            print("Hors de la grille ....")
           
    def test_position(self,x,y):
        """Méthode qui prend un couple en argument, et qui vérifie (renvoie Vrai) si la position en argument est occupée par le joueur"""
        return ((x,y) in self.used_positions)  
        
