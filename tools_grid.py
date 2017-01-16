# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:21:20 2016

@author: Paloma
"""
import tools

#--------------------Classe grille d'entiers

class Grid:
    """Classe définissant une grille d'entiers valant 0 pour les cases inoccupées, ou -1 ou 1 selon le joueur qui occupe la place.
    Sans aurgument."""
    
    def __init__(self):
        """ Initialisation de la grille: création d'un tableau de taille 8 (lignes), chaque élément contenant 8 valeurs, initialement nulles."""
        self._size=8
        self.grid=[[0 for j in range(8)]for i in range (8)]
    
    def __contains__(self,p):
        """Méthode qui prend en argument un couple et qui renvoie Vrai si les coordonnées sont valides ie bien dans la grille: 0=<x<taille et 0=<y<taille."""
        x,y=p
        return(x>=0 and y>=0 and x<self._size and y<self._size)   
        
    #@property
    
    def read_element(self, i, j): 
        """Méthode qui prend en argument deux entiers i et j, et qui renvoie l'élément de la ie ligne et je colonne de la grille."""
        try:
            tools.verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille          
            return(self.grid[i][j])
        except tools.ErrorIndex:  #traitement si les indices débordent de la grille
            print ("erreur d'indice")
            
        
    def write_element(self,i,j,elem):
        """Méthode qui prend en argument trois entiersi,jet elem, et qui modifie l'élément de la ie ligne et je colonne en y plaçant elem."""
        try:
            tools.verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille    
            tools.verify_value(elem) # on vérifie que l'élément a une valeur acceptable (1 ou -1)
            self.grid[i][j]=elem

        except tools.ErrorIndex: #traitement si les indices débordent de la grille
            print("vous ne pouvez pas vous déplacer ici, vous dépassez les bornes")
        except tools.ErrorValue: #traitement si la valeur qu'on veut rentrer ne vaut ni 1 ni -1
            print ("impossible de rentrer cette valeur...")
            
    def empty_grid(self): 
        """Méthode qui met tous les éléments de la grille à zero (sans en recréer une nouvelle)."""
        for i in range(self._size):
            for j in range(self._size):
                self.grid[i][j]=0
                
    def empty_cell(self,i,j):
        """Méthode qui prend en argument deux entiers i et j et qui renvoie Vrai si la cellule est vide ie non occupée"""
        try:
            tools.verify_bounds(i,j,self._size) #on vérifie que la cellule est bien dansla grille
            return(self.grid[i][j]==0)
        except tools.ErrorIndex: #traitement si les indices débordent de la grille
            print("Cette case n'existe pas...")
        
