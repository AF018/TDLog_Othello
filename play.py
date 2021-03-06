# -*- coding: utf-8 -*-

"""
Created on Wed Dec  7 13:36:13 2016
A exécuter pour jouer (partie console du jeu d'Othello)
"""

import tools
import tools_game

#On demande aux joueurs d'entrer leur nom           
pvp=int(input("Voulez-vous jouez en 1v1 (1) ou contre l'IA (0) ?"))
nom1=input("Nom du premier joueur:") 
color=1
if (pvp) : 
    nom2=input("Nom du deuxième joueur:") 
else : 
    color=int(input("Voulez-vous les noirs (-1) ou les blancs (1) ?"))
    nom2="IA"
    AI_pos=[0,0]
    #Creation du jeu
game=tools_game.Game(nom1,nom2,pvp,color)

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
        if (pvp or game.current_player.read_name()!="IA") : 
            position_tested_i=int(input('Entrez la position desiree:i:'))
            position_tested_j=int(input('Entrez la position desiree:j:'))
        else : 
            game.AI_play(game.valid_positions(game.player2)[1],1,7,7,game.player1,AI_pos,-1e5,1e5)
            origins=game.origins(AI_pos[0],AI_pos[1],game.AI)
            game.play_one_shot(AI_pos[0],AI_pos[1],game.AI)
            game.turn_pawn(AI_pos[0],AI_pos[1],game.AI,*origins)

        try:
            if (pvp or game.current_player.read_name()!="IA") : 
                print("Joueur joue")
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

print("Game Over !")
#Quand le jeu s'arrête, on détermine le gagnant:
game.winner()[0] #renvoie une chaîne de caractère