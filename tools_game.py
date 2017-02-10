# -*- coding: utf-8 -*-	
"""
Created on Wed Dec  7 13:30:44 2016

@author: Paloma
"""
#Ajout : self.AI dans __init__
#Ajout de la fonction AI


import tools
import tools_grid
import tools_player

#Classe Jeu

class Game:
    
    #Initialisation
    def __init__(self, name1, name2,pvp,color):
        self.grid=tools_grid.Grid()
        if (pvp) : 
            self.player1=tools_player.Player(name1, -1)  #Noirs, -1       
            self.player2=tools_player.Player(name2, 1)   #Blancs, 1 
            self.current_player=self.player1
        else : 
            self.player1=tools_player.Player(name1,color)
            self.player2=tools_player.Player("IA",-1*color)
            self.AI = self.player2
            if (color==-1) : 
                self.current_player=self.player1
            else : 
                self.current_player=self.player2
        #On place les pionts initAIux
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
               
        
        #InitAIlisation:
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
        print " scores : {0} {1}".format(score_player1,score_player2)
        if score_player1>score_player2:
            return(self.player1.read_name())
        elif score_player2>score_player1:
            return(self.player2.read_name())
        else:
            return("No one wins...")

    #Ajouts alpha-beta : appels de AI_play : rajouter ab_max,ab_min            
    def AI_play(self,val_pos,AIs_turn,depth,depth0,player,ab_max,ab_min) : #ab_max/min : un seul est signifiant et correspond au max/min des valeurs déjà calculées au même niveau que le noeud courant 
#        print "IA begins {0} {1}".format(val_pos[1][0][0],val_pos[1][0][1])
#        origins=self.origins(val_pos[1][0][0],val_pos[1][0][1],self.player2)
#        self.play_one_shot(val_pos[1][0][0],val_pos[1][0][1],self.player2)
#        self.turn_pawn(val_pos[1][0][0],val_pos[1][0][1],self.player2,*origins)
#        print "A pawn is turned..."
    #    print "Entrée dans AI_play, avec depth={0}".format(depth)
    #    print "val_pos",val_pos
        if (depth==0) :
            return self.AI.read_score()-self.player2.read_score()
#        val_pos = self.valid_positions(self.AI)
        val_maxi=-1e5
        val_mini=1e5
        if (len(val_pos)==0) :
            return -1e5
   #     print "depth≠0 : on contine"
        #On explore chaque coup possible pour l'AI.
        for i in range (len(val_pos[1])) :
        #On indique qu'on simule le coup en val_pos[i]
        #Si c'est au tour de l'AI : on sélectionne le max
            (xpawn,ypawn)=val_pos[1][i]
            if (AIs_turn) :
    #            print "AIsturn : play_one_shot en {0},{1}".format(xpawn,ypawn)
                origins=self.origins(xpawn,ypawn,self.AI)
                self.play_one_shot(xpawn,ypawn,self.AI)
    #            print "coup joué"
                self.turn_pawn(xpawn,ypawn,self.AI,*origins)
    #            print "pion tourné ; appel à depth-1={0}".format(depth-1)
                #NB : play_one_shot : pas beau
    #            print "test : ",player.read_positions()
                l = self.valid_positions(player)
    #            print "l : fait"


                val_move = self.AI_play(l,1-AIs_turn,depth-1,depth0,player,val_maxi,val_mini)


            #On retire le pion
                self.grid.make_empty(xpawn,ypawn)
#                self.grid.write_element(xpawn,ypawn,0)
                self.turn_pawn(xpawn,ypawn,player,*origins)
                self.AI.no_more_occupy_position(xpawn,ypawn)
    #            print "CETTE CASE DOIT ETRE 0000000000 : : : : : : fin AIsturn pour xpawn,ypawn = {0},{1} avec une valeur dans la case de 0 = {2}".format(xpawn,ypawn,self.grid.read_element(xpawn,ypawn))


                if(val_move>=ab_min) : 
                    (xnext,ynext)=(xpawn,ypawn)
                    break

    #            print "fin appel récursif, on revient à depth = {0}".format(depth)
                if (val_maxi<=val_move) :
                    val_maxi=val_move
                    (xnext,ynext)=(xpawn,ypawn)
        #Sinon : le min
            else :
    #            print "joueur turn : play_one_shot en {0},{1}".format(xpawn,ypawn)
                origins=self.origins(xpawn,ypawn,player)
                self.play_one_shot(xpawn,ypawn,player)    #NB : Accès au nom du joueur ? Tablea
     #           print "coup joué"
                self.turn_pawn(xpawn,ypawn,player,*origins)
                val_move = self.AI_play(self.valid_positions(self.AI),1-AIs_turn,depth-1,depth0,player,val_maxi,val_mini)
                #On retire le pion
                self.grid.make_empty(xpawn,ypawn)
#                self.grid.write_element(xpawn,ypawn,0)
                self.turn_pawn(xpawn,ypawn,self.AI,*origins)
                player.no_more_occupy_position(xpawn,ypawn)
      #          print "CETTE CASE DOIT ETRE 0000000000  / / / / / / / / fin joueur turn pour xpawn,ypawn = {0},{1} AVEC UNE VALEUR DANS LA CASE DE 0 = {2}".format(xpawn,ypawn,self.grid.read_element(xpawn,ypawn))


                if (val_move<=ab_max) : 
                    (xnext,ynext)=(xpawn,ypawn)
                    break
                if (val_mini>=val_move) :
                    val_mini=val_move
                    (xnext,ynext)=(xpawn,ypawn)
    #En sortie de boucle, (xnext,ynext) contient le coup conduisant au meilleur résultat
    #Notons que l'AI (ou le joueur) peut se retrouver dans une situation où passer son tour est la meilleure $
    #=> à rajouter !!! Pour l'instant, on suppose qu'on ne passe pas son tour
    #Notons que pour la rajouter, il suffit dans la boucle for de faire un coup où on n'appelle pas play_one_$

#        score=-1*self.AI.read_score() + self.player2.read_score()  NBNBNBNB : !!!!!!! ATTENTION : je ne comprends toujours pas j'ai écrit cette ligne !!! Normalement le score renvoyé pour un coup vaut la différence entre les positions occupées par l'AI et celles du joueur non ???
        score=AIs_turn*val_maxi + (1-AIs_turn)*val_mini
        if (depth==depth0) :
            origins=self.origins(xnext,ynext,self.AI)
            self.play_one_shot(xnext,ynext,self.AI)
            self.turn_pawn(xnext,ynext,self.AI,*origins)         
#        score+=self.AI.read_score()-self.player2.read_score()         NBNBNBNB : Normalement la valeur renvoyee ne depend que de val_maxi ou val_mini, faire gaffe à ces deux lignes !!! NBNBNBNB : Normalement la valeur renvoyee ne depend que de val_maxi ou val_mini, faire gaffe à ces deux lignes !!!
    #    print "ù`ù$^$ù`ù$^$ù`ù$^$ù`^$`ù^!!!!!!!!!! ATTENTION : 6,7 = {0}".format(self.grid.read_element(6,7))
        return score


#Pour intégrer l'AI au code dans son ensemble :
#lancer du jeu => souhaitez-vous une partie à deux joueurs ou contre l'AI => booléen AI
#si AI : quelle couleur désirez-vous, + quel nom ? (double input)
#et dans init : self.player1 = player(nom, couleurdonnée)
#self.AI = player("AI",-1*couleurdonnée)
#
#sinon : habituel (double requête de nom)
#init game : ce qui est déjà là
#
#=> du coup, AI est bien un attribut de game, c'est en réalité un player
#
#Dans le jeu lui même :
#il suffit par exemple de faire un test à chaque tour : si le joueur courrant est l'AI,
#au lieu de faire des inputs, on lance game.AI(self.valid_positions(game.AI),1,depthinitAIl,game.player1)
#
#
#
#

