# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:21:20 2016

@author: Paloma
"""
import tools

#--------------------Classe grille d'entiers

class Grid:
    
    def __init__(self):
        self._size=8
        self.grid=[[0 for j in range(8)]for i in range (8)]
    

    #validité des coordonnées: 
    def __contains__(self,p):
        x,y=p
        return(x>=0 and y>=0 and x<self._size and y<self._size)   
        
    #@property
    
    #Méthode qui renvoie l'élément de la ie ligne et je colonne
    def read_element(self, i, j): #ligne i, colonne j
        try:
            tools.verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille          
            return(self.grid[i][j])
        except tools.ErrorIndex:  #traitement si les indices débordent de la grille
            print ("erreur d'indice")
            
        
    #Méthode qui modifie l'élément de la ie ligne et je colonne
    def write_element(self,i,j,elem):
        try:
            tools.verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille    
            tools.verify_value(elem) # on vérifie que l'élément a une valeur acceptable (1 ou -1)
            self.grid[i][j]=elem

        except tools.ErrorIndex: #traitement si les indices débordent de la grille
            print("vous ne pouvez pas vous déplacer ici, vous dépassez les bornes")
        except tools.ErrorValue: #traitement si la valeur qu'on veut rentrer ne vaut ni 1 ni -1
            print ("impossible de rentrer cette valeur...")
            
    
    #Méthode qui renvoie Vrai si la cellule est vide ie non occupée
    def empty_cell(self,i,j):
        try:
            tools.verify_bounds(i,j,self._size) #on vérifie que la cellule est bien dansla grille
            return(self.grid[i][j]==0)
        except tools.ErrorIndex: #traitement si les indices débordent de la grille
            print("Cette case n'existe pas...")
        
