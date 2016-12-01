# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 01:13:39 2016

@author: Paloma
"""

import csv

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
    
    
#--------------------Classe grille d'entiers
class Grid:
    
    def __init__(self):
        self._size=8
        #self.grid=8*[8*[0]] ne marche pas!! en quelque sorte toutes les lignes sont egales
        self.grid=[[0 for j in range(8)]for i in range (8)]
    

    #validité des coordonnées: 
    #def __contains__(self,x,y):
        #return(x>=0 and y>=0 and x<self._size and y<self._size)
    def __contains__(self,p):
        x,y=p
        return(x>=0 and y>=0 and x<self._size and y<self._size)   
        
    #@property
    
    #Méthode qui renvoie l'élément de la ie ligne et je colonne
    def read_element(self, i, j): #ligne i, colonne j
        try:
            verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille          
            return(self.grid[i][j])
        except ErrorIndex:  #traitement si les indices débordent de la grille
            print ("erreur d'indice")
            
        
    #Méthode qui modifie l'élément de la ie ligne et je colonne
    def write_element(self,i,j,elem):
        try:
            verify_bounds(i,j,self._size) # on vérifie que le couple (i,j) est bien dans la grille    
            verify_value(elem) # on vérifie que l'élément a une valeur acceptable (1 ou -1)
            self.grid[i][j]=elem

        except ErrorIndex: #traitement si les indices débordent de la grille
            print("vous ne pouvez pas vous déplacer ici, vous dépassez les bornes")
        except ErrorValue: #traitement si la valeur qu'on veut rentrer ne vaut ni 1 ni -1
            print ("impossible de rentrer cette valeur...")
            
    
    #Méthode qui renvoie Vrai si la cellule est vide ie non occupée
    def empty_cell(self,i,j):
        try:
            verify_bounds(i,j,self._size) #on vérifie que la cellule est bien dansla grille
            return(self.grid[i][j]==0)
        except ErrorIndex: #traitement si les indices débordent de la grille
            print("Cette case n'existe pas...")
        

        
        
#-----------------------------------Classe Joueur
class Player:
    
    #Initialisation
    def __init__(self, name, value):
        self._name=name
        self.score=0 #correspond au nombre de positions occupées
        self.used_positions=[] #a initialiser    .append marche! l.append((i,j))
        self._value=value # valeur affectée au joueur
        
    
        #Implémentation des méthodes        
    #@property 
    
    #Renvoie le nom du joueur  
    def read_name(self):
        return(self._name)
        
    #Renvoie le score du joueur
    def read_score(self):
        #return(self.score)
        return (len(self.used_positions))
        
    #Renvoie la liste des positions occupées par le joueur sous forme d'une liste de doublets, chaque doublet étant le couple 
    # (i,j) des indices des positions
    def read_positions(self):
        return(self.used_positions)
            
    #Modifie le score du joueur, en ajoutant le nombre entré en argument au score initial
    def modify_score(self,add):
        self.score+=add
           
    #Ajoute une position à la liste des positions occupées par le joueur
    def occupy_position(self,i,j):
        try:
            #verify_bounds(i,j,8)       #BOF ATTENTION ON FAIT DEJAINTERVENIR LA GRILLE... PPLUTOT A METTRE DANS LE JEU   
            self.used_positions.append((i,j)) #On ajoute la position à la liste des positions occupées
            self.modify_score(1) #le score augmente de 1
            
        except ErrorIndex: #Tritement de l'exception
            print("Hors de la grille ....")
    
    def no_more_occupy_position(self,i,j):
        try:
            #verify_bounds(i,j,8)       #BOF ATTENTION ON FAIT DEJAINTERVENIR LA GRILLE... PPLUTOT A METTRE DANS LE JEU   
            self.used_positions.remove((i,j)) #On ajoute la position à la liste des positions occupées
            self.modify_score(-1) #le score augmente de 1
            
        except ErrorIndex: #Tritement de l'exception
            print("Hors de la grille ....")
    
        
    #Vérifie si la position en argument est occupée par le joueur
    def test_position(self,x,y):
        return ((x,y) in self.used_positions)  #a tester
        


#Classe Jeu

class Game:
    
    #Initialisation
    def __init__(self, name1, name2):
        self.grid=Grid()
        self._player1=Player(name1, -1)  #Noirs, -1       player_nb=0
        self._player2=Player(name2, 1)   #Blancs, 1             player_nb=1
        
    def number_to_player(self,number):
        if number==0:
            return(self._player1)
        elif number==1:
            return(self._player2)
     
    def opponent(self,player):
        if player==self._player1:
            return(self._player2)
        else:
            return (self._player1)
               
        
        #Initialisation:
    def play_one_shot(self,i,j,player_nb):                    
        
        if (player_nb==0):
            player=self._player1
            player.occupy_position(i,j)
            self.grid.write_element(i,j,-1)
        elif (player_nb==1):
            player=self._player2
            player.occupy_position(i,j)
            self.grid.write_element(i,j,1)
        else:
            print("erreur  ce joueur n'existe pas")
        
    def play_one_shot2(self,i,j,player):
        player.occupy_position(i,j)
        self.grid.write_element(i,j,player._value)
    
    def replacement(self,i,j,current_player):
        current_player.occupy_position(i,j)
        self.grid.write_element(i,j,current_player._value)
        opponent_player=self.opponent(current_player)
        opponent_player.no_more_occupy_position(i,j)
        
   
        
    def initia(self):
        self.play_one_shot(3,3,1)  
        self.play_one_shot(4,4,1)
        self.play_one_shot(3,4,0)
        self.play_one_shot(4,3,0)
    
    def initia2(self):
        self.play_one_shot2(3,3,self._player2)  
        self.play_one_shot2(4,4,self._player2)
        self.play_one_shot2(3,4,self._player1)
        self.play_one_shot2(4,3,self._player1)

    #Méthode qui affiche l'état courant du damier    
    def display(self):
        for i in range(8):
            line=''
            for j in range(8):
                #Afin d'aligner les nombres, et en considérant que ceux-ci ne possederont pas 4 chiffres, on les espace ainsi
                line=line + " "*(4-len(str(self.grid.read_element(i,j)))) + str(self.grid.read_element(i,j))    
            print (line)
    
    #Méthode qui retourne un tableau, avec tableau[0] la liste des positions (i,j) des pions courants qui peuvent servir d'origine et
    # en tableau[1] les positions accessibles (i,j) en correspondance avec l'origine
    def valid_positions(self,player): 
        current_occupied_positions=player.read_positions()
        possible_origins=[]
        accessible_positions=[]
        #Pour chaque pion du joueur courant
        for player_position in current_occupied_positions:
            x,y=player_position
            
            #Liste des voisins adverses pour un pion du joueur courant
            """
            neighbours=[]    
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    tested_position=(x+i,y+j)
                    if (tested_position in self.grid and not self.grid.read_element(x+i,y+j)==joueur._value and not self.grid.empty_cell(x+i,y+j)):
                        neighbours.append((x+i,y+j))
            print (neighbours)
            """
                       
            neighbours=[(x+i,y+j) for i in [-1,0,1] for j in [-1,0,1] if not self.grid.read_element(x+i,y+j)==player._value and not self.grid.empty_cell(x+i,y+j)]

            
            #Pour chaque pion voisin adverse:
            for opponant_pawn in neighbours:
                x_opponant,y_opponant= opponant_pawn #coordonnées du pion
                
                #Vecteur (pion_courant->pion_adverse_voisin)
                dx=x_opponant-x 
                dy=y_opponant-y
                """
                #On continue à avancer tout en restant dans la grille et tant que on est sur des pions du joueur adverse
                while (x+x_opponant,y+y_opponant) in self.grid and self.grid.read_element(x+x_opponant,y+y_opponant)==player._value:
                    x_opponant=x_opponant+dx
                    y_opponant=y_opponant+dy
                    """
                #On continue à avancer tout en restant dans la grille et tant que on est sur des pions du joueur adverse
                opponant_value=(-1)*player._value
                while (dx+x_opponant,dy+y_opponant) in self.grid and self.grid.read_element(dx+x_opponant,dy+y_opponant)==opponant_value:
                    x_opponant=x_opponant+dx
                    y_opponant=y_opponant+dy
                    
                #print ('position atteinte',x_opponant, y_opponant)
                if self.grid.empty_cell(dx+x_opponant,dy+y_opponant): #si la case du "bout" est bien vide
                    possible_origins.append(player_position)
                    accessible_positions.append((dx+x_opponant,dy+y_opponant))
                    #print('ok', dx+x_opponant,dy+y_opponant)
                    
        #print(possible_origins)
        #print(accessible_positions)
        final=[possible_origins,accessible_positions]
        return(final)
           
    def verify_accepted_position(self,i,j,player):
        tab=self.valid_positions(player)
        accessible_positions=tab[1]
        if not (i,j) in accessible_positions:
            raise ErrorAccessible
            
    #Méthode qui, à position donnée pour un joueur donné, retourne les pions adverses suivant les règles de l'othello
    def turn_pawn(self,i,j,player):
        tab=self.valid_positions(player)
        possible_origins=tab[0]
        accessible_positions=tab[1]
        count=0
        for pair in accessible_positions:            
            if pair == (i,j): #on  retrouve
                x_origin,y_origin= possible_origins[count]
                print(x_origin,y_origin)
                dx=i-x_origin
                dy=j-y_origin
                if dx==0: #déplacement sur une ligne
                    maximum=max(j,y_origin)
                    minimum=min(j,y_origin)
                    for k in range(minimum+1,maximum):
                        self.replacement(i,k,player)
                elif dy==0: # déplacement sur une colonne
                    maximum=max(i,x_origin)
                    minimum=min(i,x_origin)                
                    for k in range(minimum+1,maximum):
                        self.replacement(k,j,player)
                #else: #déplacement en diagonale
                self.display()                                    
            count+=1
            print(count)
            
    #Méthode qui retourne un tableau contenant les origines, pour une position but donnée        
    def origins(self,i,j,player):
        tab=self.valid_positions(player)
        possible_origins=tab[0]
        accessible_positions=tab[1]
        res=[]
        count=0
        for pair in accessible_positions:
            if pair==(i,j):
                res.append(possible_origins[count])
            count+=1
        return(res)
 
        
        
    def turn_pawn2(self,i,j,player,*tab):
        
        for pair in tab:
            x_origin,y_origin= pair
            dx=i-x_origin
            dy=j-y_origin
            
            maximum_x=max(i,x_origin)
            minimum_x=min(i,x_origin)  
            maximum_y=max(j,y_origin)
            minimum_y=min(j,y_origin)
            
            #déplacement sur une ligne
            if dx==0:
                for k in range(minimum_y+1,maximum_y):
                    self.replacement(i,k,player)
            
            # déplacement sur une colonne
            elif dy==0: 
                for k in range(minimum_x+1,maximum_x):
                    self.replacement(k,j,player)
            
            # déplacement en diagonale
            else: 
                if dx*dy>0:  #diagonale d'équation -x+a (visualisation dans un repère habituel)                   
                    #Vu la configuration, minimum_x et minium_y correspondent bien à une unique position
                    for k in range(0,abs(dx)-1):   #on effectue abs(dx)-2 itérations, et on est sur une diagonale                    
                        self.replacement(minimum_x+1+k,minimum_y+1+k,player)
                else: #diagonale d'équation +x (visualisation dans un repère habituel)
                    for k in range (0, abs(dx)-1):
                        self.replacement(maximum_x-1-k,minimum_y+1+k,player)
                    
                    
                    
                    
    #Fin de jeu si pour aucun des deux joueurs, iln'y a de position admissible
    def end_game(self):
#        if self.valid_positions(self._player1)==[[],[]] and self.valid_positions(self._player2)==[[],[]]:
#            return (True)
        if self.valid_positions(self._player1)[1]==[] and self.valid_positions(self._player2)[1]==[]:
            return (True)
                
          
                
            
            #Noir
       
def play():
    
    #On demande aux joueurs d'entrer leur nom           
    nom1=input("Nom du premier joueur:") 
    nom2=input("Nom du deuxième joueur:") 
    
    #Creation du jeu
    game=Game(nom1,nom2)
    
    #Initialisation du jeu
    game.initia2()
    number=0
    
#Tests:
    
#ga.actualisation(ga._player1,2,2)
#ga.actualisation(ga._player1,2,3)
#ga.actualisation(ga._player2,2,1)
#ga.actualisation(ga._player2,5,6)
    #print(game.end_game())
    while not game.end_game():
        print('Configuration actuelle:')
        game.display()
        current_player=game.number_to_player(number)
        print('{} doit jouer'.format(current_player.read_name()))
        
        t=True
        if game.valid_positions(current_player)[1] == []:
            print("Il n'y a aucune position admissible pour vous. C'est a votre adversaire de jouer.")
            t=False
        print ('positions admissibles:{}'.format(game.valid_positions(current_player)[1]))    
        while t:
            position_tested_i=int(input('Entrez la position desiree:i:'))
            position_tested_j=int(input('Entrez la position desiree:j:'))
           
            try:
                game.verify_accepted_position(position_tested_i,position_tested_j,current_player)
                origins=game.origins(position_tested_i,position_tested_j,current_player)
                game.play_one_shot2(position_tested_i,position_tested_j,current_player)
                game.turn_pawn2(position_tested_i,position_tested_j,current_player,*origins)
                
                t=False
            except ErrorIndex:
                print("Hors du damier...")
            except ErrorAccessible:
                print('Position non autorisee...')
            #except :
                #print("autre erreur")
                      
        number=1-number  #On change de joueur courant             

    score_player1=game._player1.read_score() 
    score_player2=game._player2.read_score()
    if score_player1>score_player2:
        print(game._player1.read_name(),"wins! Congrats!")
    elif score_player2>score_player1:
        print(game._player2.read_name(),"wins! Congrats!")
    else:
        print("Too bad, no one wins...")
        
        
        
        
        
        
        
        
        
        
        
def test(*tab):
        print ("ok")
        print(len(tab))
        for i in range(len(tab)):
            print (tab[i])
def test2(j,*tab):
    print(j)
    print ("ok")
    print(len(tab))
    for i in range(len(tab)):
        print (tab[i])
            