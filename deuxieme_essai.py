# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:13:39 2016

@author: Paloma
"""

# -*- coding: utf-8 -*-

#-------------Création des classes (grille, joueur, jeu)--------------------#

"""
Grille d'entiers 8*8 contenant (-1,0,1) (enfin trois valeurs dans tous les cas)
        Constructeur,accesseurs,setters__contains__,cellule_vide, liste de voisins vides
Joueur (nom, score, liste de toutes les positions occupées pour les IA)
        Constructeur,accesseurs,(modification score)
Jeu
        Constructeur,jouer un tour,vérifier que le coup est valide ou donner tous les coups
        licites (checker le voisinage et prolonger les droites jusqu'a toucher un pion de la
        couleur voulue), indiquer que le jeu est fini, accesseurs pour l'interface graphique
        (à voir après)
"""
#Fonctions utiles


#Classe grille d'entiers

class Grid:
    
    def __init__(self):
        self.grid_size=8
        self.grid=8*[8*[0]]

    #validité des coordonnées: 
    def __contains__(self,x,y):
        return(x>=0 and y>=0 and x<self.grid_size and y<self.grid_size)
        
    #renvoie l'élément de la ie ligne et je colonne
    def read_element(self, i, j): #ligne i, colonne j
        return(self.grid[i][j])
        
    #modifie l'élément de la ie ligne et je colonne
    def write_element(self,i,j,elem):
        assert (abs(elem)<=1)
        self.grid[i][j]=elem
    
    #renvoie Vrai si la cellule est vide ie non occupée
    def empty_cell(self,i,j):
        return(self.grid[i][j]==0)
        

        
        
#Classe Joueur
class Player:
    
    #Initialisation
    def __init__(self, nom):
        self._name=nom
        self._score=0
        self._positions_occupees=[] #a initialiser    .append marche! l.append((i,j))
        
    #Implémentation des méthodes        
    
    #Renvoie le nom du joueur    
    def read_name(self):
        return(self._name)
        
    #Renvoie le score du joueur
    def read_score(self):
        return(self._score)
            
    #Modifie le score du joueur
    def modify_score(self,n):
        self._score=n
    
    #Ajoute une position à laliste des positions occupées par le joueur
    def occupe_position(self,x,y):
        self._positions_occupees.append((x,y))
        
    #Vérifie si la position en argument est occupée par le joueur
    def test_position(self,x,y):
        return ((x,y) in self._positions_occupes)  #a tester
        


#Classe Jeu

class Game:
    
    #Initialisation
    def __init__(self, name1, name2):
        self._grid=Grid()
        self._player1=Player(name1)
        self._player2=Player(name2)
        
   
       
            

