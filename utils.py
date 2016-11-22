from PyQt4 import QtCore, QtGui

class OthelloCell(QtGui.QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedSize(60,60)
        self.setPixmap(QtGui.QPixmap('cell.jpg'))
        self.setMouseTracking(True)

    def mouseReleaseEvent(self, event):
        self.emit(QtCore.SIGNAL('clicked()'))

    def enterEvent(self,event):
        self.setPixmap(QtGui.QPixmap('occ_cell.jpg'))

    def leaveEvent(self,event):
        self.setPixmap(QtGui.QPixmap('cell.jpg'))