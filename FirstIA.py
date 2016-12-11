

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


"""
Pseudo code : 
on a besoin de : 
- la grille
- les coups réalisables : la fonction de mise à jour
- 

valid_positions(self,player): #retourne un tableau, avec tableau[0] la liste 
des positions (i,j) des pions courants qui peuvent servir d'origine et
    # en tableau[1] les positions accessibles (i,j) en correspondance avec l'origine
     

NB : int color = 1 ou -1, selon la couleur qu'on décide d'attribuer à l'IA.
NB2 : on crée une instance de Player nommée IA avant de lancer la fonction IA(x,y)
NB3 : IA est une méthode de la classe Game qui retourne le "gain max" associé 
IAs_turn = booléen égal à "c'est au tour de l'IA de jouer"
NB4 : Question de ce qu'est le "gain max" : ça ne peut pas juste être le nombre de cases occupées (inefficace).
Donc : plutôt nombre de cases occupées par l'IA-nombre de cases occupées par le joueur
Moyen pour retrouver la valeur initiale d'une case donnée ? play_one_shot ne permet pas ça, si ?
Peut-être directement un set ? => à rajouter !!!
"""
def IA_play(self,(x,y),IAs_turn) : 
    val_pos = self.valid_positions(IA)
    val_maxi=-1e5
    val_mini=1e5
    for i in range (len(val_pos)) : 
        #On indique qu'on simule le coup en val_pos[i]
        #Si c'est au tour de l'IA : on sélectionne le max
        if (IAs_turn) :    
        play_one_shot2(val_pos[i][1],val_pos[i][2],IA)    #NB : play_one_shot pas efficace dans ce contexte, à changer !
        val_move = IA_play(val_pos[i],1-IAs_turn)
            if (val_maxi<=val_move) : 
                val_maxi=val_move
                (xnext,ynext)=val_pos[i]
        #Sinon : le min
        else : 
        play_one_shot2(val_pos[i][1],val_pos[i][2],player)    #NB : Accès au nom du joueur ? Tableau de joueurs ?
        val_move = IA_play(val_pos[i],1-IAs_turn)
            if (val_mini>=val_move) : 
                val_maxi=val_move
                (xnext,ynext)=val_pos[i]
    #En sortie de boucle, (xnext,ynext) contient le coup conduisant au meilleur résultat
    #Notons que l'IA (ou le joueur) peut se retrouver dans une situation où passer son tour est la meilleure option ; 
    #=> à rajouter !!! Pour l'instant, on suppose qu'on ne passe pas son tour
    play_one_shot2(xnext,yxnext,IA)
    return len(self.valid_positions(IA)-len(self.valid_positions(player))  #Même chose : nom joueur ???
    
