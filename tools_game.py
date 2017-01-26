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
    """Classe de je qui prend en argument deux chaînes de carcatère qui sont les noms des joueurs."""

    def __init__(self, name1, name2, pvp_option, color):
        """Initialisation"""
        self.grid=tools_grid.Grid()
        self.pvp = pvp_option
        
        if (self.pvp) : 
            self.player1=tools_player.Player(name1, -1)  #Noirs, -1       
            self.player2=tools_player.Player(name2, 1)   #Blancs, 1 
            self.current_player=self.player1
        else : 
            self.player1=tools_player.Player(name1,color)
            self.player2=tools_player.Player("IA",-1*color)
            self.IA = self.player2
            if (color==-1) : 
                self.current_player=self.player1
            else : 
                self.current_player=self.player2
        
        #On place les pionts initiaux
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1)         
        

    def number_to_player(self,number):
        """Méthode qui prend un nombre -1 ou 1 en argument et qui renvoie le joueur coresspondant. (en sortie: instance de la classe Player"""
        if number==-1:
            return(self.player1)
        elif number==1:
            return(self.player2)
     
    def opponent(self,player):
        """Méthode qui renvoie le joueur opposé à celui pris en argument. """
        if player==self.player1:
            return(self.player2)
        else:
            return (self.player1)
               
    def play_one_shot(self,i,j,player):
        """Méthode qui prend en argument deux entiers i et j et un joueur et qui place le joueur en (i,j): ajoute (i,j) à la liste des positions
        occupées par le joueur et inscrit la valeur associée au joueur dans la grille."""
        player.occupy_position(i,j)
        self.grid.write_element(i,j,player.read_value())
        
         
    def play_one_shot_bis(self,i,j,player_nb):                    
        """Idem que play_one_shot mais prend en argument non pas le joueur mais un nombre, crrespondant à la valeur du joueur."""
        if (player_nb==-1):
            player=self.player1
        elif (player_nb==1):
            player=self.player2
        else:
            print("erreur  ce joueur n'existe pas")
        player.occupy_position(i,j)
        self.grid.write_element(i,j,player_nb)
        
    
    def replacement(self,i,j,current_player):
        """Méthode qui prend en argument deux entiers i et j et un joueur, et qui remplace la case (i,j) de la grille par ce joueur.
        Cad: (i,j) est ajouté à la liste des positions occupées par le joueur, et enlevé de la liste du joueur adverse, et la grille 
        a à présent en (i,j) le numérodu joueur."""
        current_player.occupy_position(i,j)
        self.grid.write_element(i,j,current_player.read_value())
        opponent_player=self.opponent(current_player)
        opponent_player.no_more_occupy_position(i,j)
        
    def initia(self):
        """ Méthode qui ne prend aucun argument, et qui joue les 4 coups initiaux."""
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1)

        
    def initia_bis(self):
        """ Idem que initia mais d'une autre manière"""
        self.play_one_shot_bis(3,3,1)  
        self.play_one_shot_bis(4,4,1)
        self.play_one_shot_bis(3,4,0)
        self.play_one_shot_bis(4,3,0)
    
        
    def display(self):
        """ Méthode qui affiche l'état courant du damier"""
        for i in range(8):
            line=''
            for j in range(8):
                #Afin d'aligner les nombres, et en considérant que ceux-ci ne possederont pas 4 chiffres, on les espace ainsi
                line=line + " "*(4-len(str(self.grid.read_element(i,j)))) + str(self.grid.read_element(i,j))    
            print (line)
    
    
    def valid_positions(self,player): 
        """Méthode qui retourne un tableau, avec en tableau[0] la liste des positions (i,j) des pions courants du joueur qui peuvent servir d'origine et
    en tableau[1] les positions accessibles (i,j) en correspondance avec l'origine."""
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
        """ Méthode qui prend en argument deux entiers i et j et un joueur, et qui renvoie Vrai si (i,j) est une position accessible au joueur."""
        tab=self.valid_positions(player)
        accessible_positions=tab[1]
        if not (i,j) in accessible_positions:
            raise tools.ErrorAccessible
                        
    def origins(self,i,j,player):
        """ Méthode qui prend en argument deux entiers i et j et un joueur, et qui retourne un tableau contenant les origines, pour la position but (i,j) donnée """
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
        """ Méthode qui prend en argument deux entiers i, j, un joueur et un tableau, et qui retourne tous les pions (joueur adverse -> joueur courant) entre (i,j) et les positions contenues dasn tab, les extrémités cad (i,j) et les couples de tab étant exclues."""
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
                    
                    
                    
                    
 
    def end_game(self):
        """  Méthode qui ne prend pas d'argument et qui renvoie Vrai si la fin du jeu est atteinte cad si pour aucun des deux joueurs, il n'y a de position admissible """
        if self.valid_positions(self.player1)[1]==[] and self.valid_positions(self.player2)[1]==[]:
            return (True)
                
    def winner (self):
        """ Méthode qui ne prend rien en argument et renvoie une chaîne de caractère: le nom du vainqueur."""
        score_player1=self.player1.read_score() 
        score_player2=self.player2.read_score()
        if score_player1>score_player2:
            return(self.player1.read_name())
        elif score_player2>score_player1:
            return(self.player2.read_name())
        else:
            return("No one wins...")
    
    def empty_game(self):
        """Méthode qui réinitialise le jeu."""
        #Initialisation des positions occupées par les joueurs
        for p in [self.player1,self.player2]:
            while p.read_positions()!=[]:
                i,j=p.read_positions()[0]
                p.no_more_occupy_position(i,j)
        #Le joueur courant est à nouveau le joueur 1
        self.current_player=self.player1      
        #Initilisation de la grille
        self.grid.empty_grid()
        self.play_one_shot(3,3,self.player2)  
        self.play_one_shot(4,4,self.player2)
        self.play_one_shot(3,4,self.player1)
        self.play_one_shot(4,3,self.player1) 
        
#NBNBNB : val_pos = valid_positions[1]                
    def IA_play(self,val_pos,IAs_turn,depth,depth0,player,AI_pos) : 
#        print "IA begins {0} {1}".format(val_pos[1][0][0],val_pos[1][0][1])
#        origins=self.origins(val_pos[1][0][0],val_pos[1][0][1],self.player2)
#        self.play_one_shot(val_pos[1][0][0],val_pos[1][0][1],self.player2)
#        self.turn_pawn(val_pos[1][0][0],val_pos[1][0][1],self.player2,*origins)
#        print "A pawn is turned..."
    #    print "Entrée dans IA_play, avec depth={0}".format(depth)
    #    print "val_pos",val_pos
        if (depth==0) :
            return 0
#        val_pos = self.valid_positions(self.IA)
        val_maxi=-1e5
        val_mini=1e5
        if (len(val_pos)==0) :
            return 0
   #     print "depth≠0 : on contine"
        #On explore chaque coup possible pour l'IA.
        for i in range (len(val_pos)) :
        #On indique qu'on simule le coup en val_pos[i]
        #Si c'est au tour de l'IA : on sélectionne le max
            (xpawn,ypawn)=val_pos[i]
            if (IAs_turn) :
    #            print "IAsturn : play_one_shot en {0},{1}".format(xpawn,ypawn)
                origins=self.origins(xpawn,ypawn,self.IA)
                self.play_one_shot(xpawn,ypawn,self.IA)
    #            print "coup joué"
                self.turn_pawn(xpawn,ypawn,self.IA,*origins)
    #            print "pion tourné ; appel à depth-1={0}".format(depth-1)
                #NB : play_one_shot : pas beau
    #            print "test : ",player.read_positions()
                l = self.valid_positions(player)[1]
    #            print "l : fait"
                val_move = self.IA_play(l,1-IAs_turn,depth-1,depth0,player,AI_pos)
    #            print "fin appel récursif, on revient à depth = {0}".format(depth)
                if (val_maxi<=val_move) :
                    val_maxi=val_move
                    (xnext,ynext)=(xpawn,ypawn)
            #On retire le pion
                self.grid.make_empty(xpawn,ypawn)
#                self.grid.write_element(xpawn,ypawn,0)
                self.turn_pawn(xpawn,ypawn,player,*origins)
                self.IA.no_more_occupy_position(xpawn,ypawn)
    #            print "CETTE CASE DOIT ETRE 0000000000 : : : : : : fin IAsturn pour xpawn,ypawn = {0},{1} avec une valeur dans la case de 0 = {2}".format(xpawn,ypawn,self.grid.read_element(xpawn,ypawn))
        #Sinon : le min
            else :
    #            print "joueur turn : play_one_shot en {0},{1}".format(xpawn,ypawn)
                origins=self.origins(xpawn,ypawn,player)
                self.play_one_shot(xpawn,ypawn,player)    #NB : Accès au nom du joueur ? Tablea
     #           print "coup joué"
                self.turn_pawn(xpawn,ypawn,player,*origins)
                val_move = self.IA_play(self.valid_positions(self.IA)[1],1-IAs_turn,depth-1,depth0,player,AI_pos)
                if (val_mini>=val_move) :
                    val_mini=val_move
                    (xnext,ynext)=(xpawn,ypawn)
                #On retire le pion
                self.grid.make_empty(xpawn,ypawn)
#                self.grid.write_element(xpawn,ypawn,0)
                self.turn_pawn(xpawn,ypawn,self.IA,*origins)
                player.no_more_occupy_position(xpawn,ypawn)
      #          print "CETTE CASE DOIT ETRE 0000000000  / / / / / / / / fin joueur turn pour xpawn,ypawn = {0},{1} AVEC UNE VALEUR DANS LA CASE DE 0 = {2}".format(xpawn,ypawn,self.grid.read_element(xpawn,ypawn))
    #En sortie de boucle, (xnext,ynext) contient le coup conduisant au meilleur résultat
    #Notons que l'IA (ou le joueur) peut se retrouver dans une situation où passer son tour est la meilleure $
    #=> à rajouter !!! Pour l'instant, on suppose qu'on ne passe pas son tour
    #Notons que pour la rajouter, il suffit dans la boucle for de faire un coup où on n'appelle pas play_one_$

        score=-1*self.IA.read_score() + self.player2.read_score()
        if (depth==depth0) :
            AI_pos[0],AI_pos[1]=xnext,ynext
#            origins=self.origins(xnext,ynext,self.IA)
#            self.play_one_shot(xnext,ynext,self.IA)
#            self.turn_pawn(xnext,ynext,self.IA,*origins)
        score+=self.IA.read_score()-self.player2.read_score()
    #    print "ù`ù$^$ù`ù$^$ù`ù$^$ù`^$`ù^!!!!!!!!!! ATTENTION : 6,7 = {0}".format(self.grid.read_element(6,7))
        return score


#Pour intégrer l'IA au code dans son ensemble :
#lancer du jeu => souhaitez-vous une partie à deux joueurs ou contre l'IA => booléen IA
#si IA : quelle couleur désirez-vous, + quel nom ? (double input)
#et dans init : self.player1 = player(nom, couleurdonnée)
#self.IA = player("IA",-1*couleurdonnée)
#
#sinon : habituel (double requête de nom)
#init game : ce qui est déjà là
#
#=> du coup, IA est bien un attribut de game, c'est en réalité un player
#
#Dans le jeu lui même :
#il suffit par exemple de faire un test à chaque tour : si le joueur courrant est l'IA,
#au lieu de faire des inputs, on lance game.IA(self.valid_positions(game.IA),1,depthinitial,game.player1)
#
#
#
#