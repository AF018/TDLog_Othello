#coding: utf8

#Premiere version de l'IA : un minimax couple a un alpha-beta
#Principe rappele ici : l'algorithme minimax explore tous les coups possibles a partir
#d'une situation donnee en presumant que lorsque le joueur humain joue, il selectionne
#forcement le meilleur coup pour lui (=le pire pour l'IA) ; on s'arrete a une certaine profondeur
#d'exploration fixee a l'avance
#
#Alpha-beta : ameliore le minimax en diminuant le nombre de coups a explorer.
#Ex : Max
#   /  |  \
# Min Min Min
#       /  |  \
#   coup1 coup2 coup3
#
#Supposons qu'on soit en train de calculer le Min en bas à droite sur ce schema : on calcule le min
#de tous les coups possibles en partant de ce point.
#Si l'un de ces coups renvoie un resultat plus petit que l'un des deux Min deja calculés (milieu et gauche),
#il est inutile de calculer les autres coups : en effet, le Min de droite sera inferieur ou egal a ce resultat,
#donc dans tous les cas plus petit que au moins un des deux autres Min, donc en aucun cas le resultat renvoye par
#le Max. On peut donc "elaguer" les branches correspondantes. Bien sur, le meme raisonnement marche si on est en train
#de calculer un Min de Max.

#NB : d'une maniere generale, les optimisations de minimax ont le meme but : eviter d'explorer certains chemins

import tools_game

"""
Pseudo code : 
on a besoin de : 
- la grille
- les coups réalisables : la fonction de mise à jour
- 

valid_positions(self,player): #retourne un tableau, avec tableau[0] la liste 
des positions (i,j) des pions courants qui peuvent servir d'origine et
    # en tableau[1] les positions accessibles (i,j) en correspondance avec l'origine (là où on place
      le pion)
play_one_shot(i,j,player) : pose un pion en (i,j)

NB : int color = 1 ou -1, selon la couleur qu'on décide d'attribuer à l'IA.
NB2 : on crée une instance de Player nommée IA avant de lancer la fonction IA(x,y)
NB3 : IA est une méthode de la classe Game qui retourne le "gain max" associé 
IAs_turn = booléen égal à "c'est au tour de l'IA de jouer"
NB4 : Question de ce qu'est le "gain max" : ça ne peut pas juste être le nombre de cases occupées (inefficace).
Donc : plutôt nombre de cases occupées par l'IA-nombre de cases occupées par le joueur
Moyen pour retrouver la valeur initiale d'une case donnée ? play_one_shot ne permet pas ça, si ?
Peut-être directement un set ? => à rajouter !!!

Pour l'instant, elle prend aussi player (le joueur humain) en argument, en attendant une solution plus élégante au problème de la simulation d'un coup.
On note depth la profondeur : lorsqu'elle est à 0, on s'arrête. Initialisée au plus grand entier possible, sans que ça lag.
"""
def IA_play(self,(x,y),IAs_turn,depth,player) :
    if (depth==0) : 
        return 0 
    val_pos = self.valid_positions(IA)
    val_maxi=-1e5
    val_mini=1e5
    if (len(val_pos)==0) : 
        return 0
    #On explore chaque coup possible pour l'IA.
    for i in range (len(val_pos)) : 
        #On indique qu'on simule le coup en val_pos[i]
        #Si c'est au tour de l'IA : on sélectionne le max
        if (IAs_turn) :    
            play_one_shot(val_pos[1][i][0],val_pos[1][i][1],IA)    
            #NB : play_one_shot : pas beau
            val_move = IA_play(val_pos[i],1-IAs_turn,depth-1,player)
            if (val_maxi<=val_move) : 
                val_maxi=val_move
                (xnext,ynext)=val_pos[1][i]
            #On retire le pion
            self.grid.write_element(val_pos[1][i][0],val_pos[1][i][1],0)
        #Sinon : le min
        else : 
            play_one_shot2(val_pos[1][i][0],val_pos[1][i][1],player)    #NB : Accès au nom du joueur ? Tableau de joueurs ?
            val_move = IA_play(val_pos[i],1-IAs_turn,depth-1,player)
            if (val_mini>=val_move) : 
                val_maxi=val_move
                (xnext,ynext)=val_pos[1][i]
            #On retire le pion
            self.grid.write_element(val_pos[1][i][0],val_pos[1][i][1],0)
    #En sortie de boucle, (xnext,ynext) contient le coup conduisant au meilleur résultat
    #Notons que l'IA (ou le joueur) peut se retrouver dans une situation où passer son tour est la meilleure option ; 
    #=> à rajouter !!! Pour l'instant, on suppose qu'on ne passe pas son tour
    #Notons que pour la rajouter, il suffit dans la boucle for de faire un coup où on n'appelle pas play_one_shot mais où on appelle quand même IA_play

    score=-1*self.IA.read_score() + self.player.read_score()
    play_one_shot(xnext,yxnext,IA)
    score+=self.IA.read_score()-self.player.read_score()
    return score  
    
    #Même chose : nom joueur pour le score ???
    
