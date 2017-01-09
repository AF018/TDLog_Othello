# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:30:44 2016

@author: Paloma
"""

import tools
import tools_grid
import tools_player

#Classe Jeu

class Game:
    
    #Initialisation
    def __init__(self, name1, name2):
        self.grid=tools_grid.Grid()
        self.player1=tools_player.Player(name1, -1)  #Noirs, -1       
        self.player2=tools_player.Player(name2, 1)   #Blancs, 1 
        self.current_player=self.player1
        
        #On place les pionts initiaux
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1)         
        

    def number_to_player(self,number):
        if number==-1:
            return(self.player1)
        elif number==1:
            return(self.player2)
     
    def opponent(self,player):
        if player==self.player1:
            return(self.player2)
        else:
            return (self.player1)
               
        
        #Initialisation:
    def play_one_shot_bis(self,i,j,player_nb):                    
        
        if (player_nb==-1):
            player=self.player1
            player.occupy_position(i,j)
            self.grid.write_element(i,j,-1)
        elif (player_nb==1):
            player=self.player2
            player.occupy_position(i,j)
            self.grid.write_element(i,j,1)
        else:
            print("erreur  ce joueur n'existe pas")
        
    def play_one_shot(self,i,j,player):
        player.occupy_position(i,j)
        print("ok")
        self.grid.write_element(i,j,player.read_value())
    
    def replacement(self,i,j,current_player):
        current_player.occupy_position(i,j)
        self.grid.write_element(i,j,current_player.read_value())
        opponent_player=self.opponent(current_player)
        opponent_player.no_more_occupy_position(i,j)
        
   
        
    def initia_bis(self):
        self.play_one_shot_bis(3,3,1)  
        self.play_one_shot_bis(4,4,1)
        self.play_one_shot_bis(3,4,0)
        self.play_one_shot_bis(4,3,0)
    
    def initia(self):
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1)

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
            neighbours=[(x+i,y+j) for i in [-1,0,1] for j in [-1,0,1] if (x+i,y+j) in self.grid and not self.grid.read_element(x+i,y+j)==player.read_value() and not self.grid.empty_cell(x+i,y+j)]

            
            #Pour chaque pion voisin adverse:
            for opponant_pawn in neighbours:
                x_opponant,y_opponant= opponant_pawn #coordonnées du pion
                
                #Vecteur (pion_courant->pion_adverse_voisin)
                dx=x_opponant-x 
                dy=y_opponant-y
                
                #On continue à avancer tout en restant dans la grille et tant que on est sur des pions du joueur adverse
                opponant_value=(-1)*player.read_value()
                while (dx+x_opponant,dy+y_opponant) in self.grid and self.grid.read_element(dx+x_opponant,dy+y_opponant)==opponant_value:
                    x_opponant=x_opponant+dx
                    y_opponant=y_opponant+dy
                    
                if (dx+x_opponant,dy+y_opponant) in self.grid and self.grid.empty_cell(dx+x_opponant,dy+y_opponant): #si la case du "bout" est bien vide
                    possible_origins.append(player_position)
                    accessible_positions.append((dx+x_opponant,dy+y_opponant))
                   
                    
     
        final=[possible_origins,accessible_positions]
        return(final)
           
    def verify_accepted_position(self,i,j,player):
        tab=self.valid_positions(player)
        accessible_positions=tab[1]
        if not (i,j) in accessible_positions:
            raise tools.ErrorAccessible
            
            
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
 
        
        
    def turn_pawn(self,i,j,player,*tab):
        
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
        if self.valid_positions(self.player1)[1]==[] and self.valid_positions(self.player2)[1]==[]:
            return (True)
                
    def winner (self):
        score_player1=self.player1.read_score() 
        score_player2=self.player2.read_score()
        if score_player1>score_player2:
            return(self.player1.read_name())
        elif score_player2>score_player1:
            return(self.player2.read_name())
        else:
            return("No one wins...")
    
    # Réinitialisation du jeu
    def empty_game(self):
        #Initialisation des positions occupées par les joueurs
        for p in [self.player1,self.player2]:
            while p.read_positions()!=[]:
                i,j=p.read_positions()[0]
                p.no_more_occupy_position(i,j)
        #Initilisation de la grille
        self.grid.empty_grid()
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1) 
        
                