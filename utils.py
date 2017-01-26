from PyQt4 import QtCore, QtGui
from csv import reader,writer

class OthelloCell(QtGui.QLabel):
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
        print(self.playable)
        self.emit(QtCore.SIGNAL('clicked()'))

    def enterEvent(self,event):
        if (self.color_nb == 0 and self.playable == 1):
            self.setPixmap(QtGui.QPixmap('occ_cell.jpg'))

    def leaveEvent(self,event):
        if (self.color_nb == 0 and self.playable == 1):
            self.setPixmap(QtGui.QPixmap('cell.jpg'))
            
class Profiles:
    def __init__(self):
        """Crée un tableau contenant tous les profils avec leurs statistiques"""
        # Statistiques dans un fichier csv, lecture de chaque ligne du document pour récupérer
        with open("stats.csv", newline = '\n') as text:
            content = reader(text, delimiter = ',')
            self.stats_tab=[[info for info in line] for line in content]

    def stats_for_player(self,index):
        """Renvoie les statistiques associées au profil d'index i"""
        return [self.stats_tab[index][i] for i in range(1,len(self.stats_tab[index]))]

    def names(self):
        """Renvoie la liste des noms des profils"""
        return [self.stats_tab[i][0] for i in range(len(self.stats_tab))]

    def new_profile(self,name):
        """Crée un nouveau profil à partir d'un nom, vérifie que le nom n'est pas déjà existant"""
        if name not in self.names():
            self.stats_tab.append([name,0,0,0])
            self.save_stats()
            
    def update_stats(self,winner,loser):
        """Met à jour les statistiques du perdant et du gagnant"""
        # Le type des éléments du tableau est la chaîne de caractère
        # On fait attention à cela pour l actualisation
        for player_stats in self.stats_tab:
            if player_stats[0] == winner:
                player_stats[1] = str(int(player_stats[1])+1)
                player_stats[2] = str(int(player_stats[2])+1)
        self.save_stats()
        
    def save_stats(self):
        """Sauvegarde les données dans le fichier csv"""
        with open("stats.csv", 'w') as text:
            content = writer(text)
            content.writerows([[info for info in line] for line in self.stats_tab])
            
            
            
            
            