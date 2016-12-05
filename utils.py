from PyQt4 import QtCore, QtGui

class OthelloCell(QtGui.QLabel):
    def __init__(self,color):
        super().__init__()
        self.setFixedSize(60,60)
        self.color = color
        if (self.color == 1):
            self.setPixmap(QtGui.QPixmap('occ_white_cell.jpg'))
        elif (self.color == -1):
            self.setPixmap(QtGui.QPixmap('occ_black_cell.jpg'))
        else:
            self.setPixmap(QtGui.QPixmap('cell.jpg'))
        self.setMouseTracking(True)

    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))

    def enterEvent(self,event):
        if (self.color == 0):
            self.setPixmap(QtGui.QPixmap('occ_cell.jpg'))

    def leaveEvent(self,event):
        if (self.color == 0):
            self.setPixmap(QtGui.QPixmap('cell.jpg'))