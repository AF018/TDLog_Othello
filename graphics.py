# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from utils import OthelloCell

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(480, 560)
        Window.setAnimated(True)
        self.centralwidget = QtGui.QWidget(Window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 541))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.game_layout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.game_layout.setSpacing(0)
        self.game_layout.setObjectName(_fromUtf8("game_layout"))
        self.player_1 = QtGui.QLabel(self.gridLayoutWidget)
        self.player_1.setAlignment(QtCore.Qt.AlignCenter)
        self.player_1.setObjectName(_fromUtf8("player_1"))
        self.game_layout.addWidget(self.player_1, 8, 0, 1, 1)
        self.score_1 = QtGui.QLabel(self.gridLayoutWidget)
        self.score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.score_1.setObjectName(_fromUtf8("score_1"))
        self.game_layout.addWidget(self.score_1, 8, 1, 1, 1)
        self.player_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.player_2.setAlignment(QtCore.Qt.AlignCenter)
        self.player_2.setObjectName(_fromUtf8("player_2"))
        self.game_layout.addWidget(self.player_2, 8, 3, 1, 1)
        self.score_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.score_2.setObjectName(_fromUtf8("score_2"))
        self.game_layout.addWidget(self.score_2, 8, 2, 1, 1)
        self.gridLayoutWidget.raise_()
        self.player_2.raise_()
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOthello = QtGui.QMenu(self.menubar)
        self.menuOthello.setObjectName(_fromUtf8("menuOthello"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        Window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Window.setStatusBar(self.statusbar)
        self.action_new_game = QtGui.QAction(Window)
        self.action_new_game.setObjectName(_fromUtf8("action_new_game"))
        self.action_undo = QtGui.QAction(Window)
        self.action_undo.setObjectName(_fromUtf8("action_undo"))
        self.action_stats = QtGui.QAction(Window)
        self.action_stats.setObjectName(_fromUtf8("action_stats"))
        self.menuOthello.addAction(self.action_new_game)
        self.menuOthello.addAction(self.action_undo)
        self.menuOptions.addAction(self.action_stats)
        self.menubar.addAction(self.menuOthello.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "MainWindow", None))
        self.player_1.setText(_translate("Window", "Player 1", None))
        self.score_1.setText(_translate("Window", "Score 1", None))
        self.player_2.setText(_translate("Window", "Player 2", None))
        self.score_2.setText(_translate("Window", "Score 2", None))
        self.menuOthello.setTitle(_translate("Window", "Game", None))
        self.menuOptions.setTitle(_translate("Window", "Options", None))
        self.action_new_game.setText(_translate("Window", "New Game", None))
        self.action_undo.setText(_translate("Window", "Undo", None))
        self.action_stats.setText(_translate("Window", "Stats", None))
		
        self.__length = 8
        self.__buttons = [[OthelloCell()
            for i in range(self.__length)]
            for j in range(self.__length)]
        for i in range(self.__length):
            for j in range(self.__length):
                self.game_layout.addWidget(self.__buttons[i][j],i,j)
        Window.connect(self.__buttons[0][0], QtCore.SIGNAL('clicked()'), self.ok)

    def ok(self):
        print("Ok")


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Window = QtGui.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())

