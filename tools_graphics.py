# -*- coding: utf-8 -*-

"""
Created on Wed Dec  7 16:03:34 2016
Outils pour l'interface graphique : cases du plateau et statistiques
"""

from PyQt4 import QtCore, QtGui
from csv import reader,writer

class OthelloCell(QtGui.QLabel):
    """Classe représentant une case du plateau"""

    def __init__(self,color_nb):
        super().__init__()
        self.setFixedSize(60,60)
        self.color_nb = color_nb
        self.playable = 0
        if (self.color_nb == 1):
            self.setPixmap(QtGui.QPixmap('occ_white_cell.jpg'))
        elif (self.color_nb == -1):
            self.setPixmap(QtGui.QPixmap('occ_black_cell.jpg'))
        else:
            self.setPixmap(QtGui.QPixmap('cell.jpg'))
        self.setMouseTracking(True)

    def refresh(self,new_color_nb,is_playable):
        """Actualise l'apparence de la case et l'attribut playable permettant de savoir
        si la case est jouable"""
        self.color_nb=new_color_nb
        if (self.color_nb == 1):
            self.setPixmap(QtGui.QPixmap('occ_white_cell.jpg'))
        elif (self.color_nb == -1):
            self.setPixmap(QtGui.QPixmap('occ_black_cell.jpg'))
        else:
            self.setPixmap(QtGui.QPixmap('cell.jpg'))
        if is_playable:
            self.playable = 1
        else:
            self.playable = 0

    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))

    def enterEvent(self,event):
        if (self.color_nb == 0 and self.playable == 1):
            self.setPixmap(QtGui.QPixmap('occ_cell.jpg'))

    def leaveEvent(self,event):
        if (self.color_nb == 0 and self.playable == 1):
            self.setPixmap(QtGui.QPixmap('cell.jpg'))

def add_name(combo_box,name,names):
    """Permet d'ajouter le nom name à un widget du type QComboBox
    Utilisé pour le lancement du jeu dans la partie graphique, lorsqu'un
    profil est crée"""
    if name not in names:
        combo_box.addItem(name)
            
class Profiles:
    """Classe conservant les profils et statistiques associées"""

    def __init__(self):
        """Crée un tableau contenant tous les profils avec leurs statistiques"""
        # Statistiques dans un fichier csv, lecture de chaque ligne du document pour récupérer
        with open("stats.csv", newline = '\n') as text:
            content = reader(text, delimiter = ',')
            self.stats_tab=[[info for info in line] for line in content]

    def information(self,profile_nb,index):
        """Renvoie les statistiques associées au profil d'index i"""
        return self.stats_tab[profile_nb][index]

    def names(self):
        """Renvoie la liste des noms des profils"""
        return [self.stats_tab[i][0] for i in range(len(self.stats_tab))]

    def new_profile(self,name):
        """Crée un nouveau profil à partir d'un nom, vérifie que le nom n'est pas déjà existant"""
        if name not in self.names():
            self.stats_tab.append([name,"0","0","0","0","0","0"])
            self.save_stats()
            
    def increment_reboots(self,players):
        for player_stats in self.stats_tab:
            for i in [0,1]:
                if player_stats[0]==players[i]:
                    player_stats[6]=str(int(player_stats[6])+1)
        self.save_stats()
            
    def update_stats(self,winner,loser,pvp):
        """Met à jour les statistiques du perdant et du gagnant"""
        # Le type des éléments du tableau est la chaîne de caractère
        # On fait attention à cela pour l actualisation
        for player_stats in self.stats_tab:
            # 1 correspond au nombre de parties jouées,
            # 2 aux parties gagnées sans IA, 3 perdues sans IA
            # 4 aux parties gagnées avec IA, 5 perdues avec IA
            # 4-2*int(pvp) donne 2 si la partie se joue sans IA, 4 sinon
            if player_stats[0] == winner:
                player_stats[1] = str(int(player_stats[1])+1)
                player_stats[4-2*int(pvp)] = str(int(player_stats[4-2*int(pvp)])+1)
            elif player_stats[0] == loser:
                player_stats[1] = str(int(player_stats[1])+1)
                player_stats[5-2*int(pvp)] = str(int(player_stats[5-2*int(pvp)])+1)
        self.save_stats()
        
    def save_stats(self):
        """Sauvegarde les données dans le fichier csv"""
        with open("stats.csv", 'w') as text:
            content = writer(text)
            content.writerows([[info for info in line] for line in self.stats_tab]) 