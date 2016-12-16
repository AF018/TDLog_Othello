# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:26:43 2016

@author: Paloma
"""

import tools
      
#-----------------------------------Classe Joueur
class Player:
    
    #Initialisation
    def __init__(self, name, value):
        self._name=name
        self.score=0 #correspond au nombre de positions occupées
        self.used_positions=[] #a initialiser    .append marche! l.append((i,j))
        self._value=value # valeur affectée au joueur
        
       
    #@property 
    
    #Renvoie le nom du joueur  
    def read_name(self):
        return(self._name)
        
    #Renvoie le score du joueur
    def read_score(self):
        return (len(self.used_positions))
        
    #Renvoie la liste des positions occupées par le joueur sous forme d'une liste de doublets, chaque doublet étant le couple 
    # (i,j) des indices des positions
    def read_positions(self):
        return(self.used_positions)
    
    #Renvoie la valeur affectée au joueur    
    def read_value(self):
        return (self._value)
        
        
           
    #Ajoute une position à la liste des positions occupées par le joueur
    def occupy_position(self,i,j):
        try:
            self.used_positions.append((i,j)) #On ajoute la position à la liste des positions occupées         
            
        except tools.ErrorIndex: #Tritement de l'exception
            print("Hors de la grille ....")
    
    def no_more_occupy_position(self,i,j):
        try:
            #verify_bounds(i,j,8)       #BOF ATTENTION ON FAIT DEJAINTERVENIR LA GRILLE... PPLUTOT A METTRE DANS LE JEU   
            self.used_positions.remove((i,j)) #On ajoute la position à la liste des positions occupées
           
            
        except tools.ErrorIndex: #Tritement de l'exception
            print("Hors de la grille ....")
    
        
    #Vérifie si la position en argument est occupée par le joueur
    def test_position(self,x,y):
        return ((x,y) in self.used_positions)  #a tester
        
