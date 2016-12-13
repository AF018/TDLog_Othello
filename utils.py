from PyQt4 import QtCore, QtGui

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