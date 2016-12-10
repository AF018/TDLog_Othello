# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 13:36:13 2016

@author: Paloma
"""
import tools
import tools_game

#On demande aux joueurs d'entrer leur nom           
nom1=input("Nom du premier joueur:") 
nom2=input("Nom du deuxième joueur:") 
    
    #Creation du jeu
game=tools_game.Game(nom1,nom2)
    
    #initialisation du jeu
    
    #Si on veut séparer la création de la grille et le placement des 4 pions initiaux
    #game.initia()

   
while not game.end_game():
    print('Configuration actuelle:')
    game.display()
    
    print('{} doit jouer'.format(game.current_player.read_name()))
        
    t=True
    if game.valid_positions(game.current_player)[1] == []:
        print("Il n'y a aucune position admissible pour vous. C'est a votre adversaire de jouer.")
        t=False
    print ('positions admissibles:{}'.format(game.valid_positions(game.current_player)[1]))    
    while t:
        position_tested_i=int(input('Entrez la position desiree:i:'))
        position_tested_j=int(input('Entrez la position desiree:j:'))
           
        try:
            game.verify_accepted_position(position_tested_i,position_tested_j,game.current_player)
            origins=game.origins(position_tested_i,position_tested_j,game.current_player)
            game.play_one_shot(position_tested_i,position_tested_j,game.current_player)
            game.turn_pawn(position_tested_i,position_tested_j,game.current_player,*origins)
                
            t=False
        except tools.ErrorIndex:
            print("Hors du damier...")
        except tools.ErrorAccessible:
            print('Position non autorisee...')
        except :
            print("autre erreur")
                      
            
    #On change de joueur courant
    game.current_player=game.opponent(game.current_player)

score_player1=game.player1.read_score() 
score_player2=game.player2.read_score()
if score_player1>score_player2:
    print(game.player1.read_name(),"wins! Congrats!")
elif score_player2>score_player1:
    print(game.player2.read_name(),"wins! Congrats!")
else:
    print("Too bad, no one wins...")
        