# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from utils import OthelloCell
from game_pas_nettoye import Game

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
    def __init__(self):
        self.game = Game("j","r")
        self.game.initia2()
        self.setupUi()
        self.retranslateUi()
        self.start()

    def setupUi(self):
        """Affiche tous les éléments de l'interface principale"""
        self.window = QtGui.QMainWindow()
        self.window.setObjectName(_fromUtf8("Window"))
        self.window.resize(480, 560)
        self.window.setAnimated(True)
        self.centralwidget = QtGui.QWidget(self.window)
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
        self.window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOthello = QtGui.QMenu(self.menubar)
        self.menuOthello.setObjectName(_fromUtf8("menuOthello"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.window.setStatusBar(self.statusbar)
        self.action_new_game = QtGui.QAction(self.window)
        self.action_new_game.setObjectName(_fromUtf8("action_new_game"))
        self.action_undo = QtGui.QAction(self.window)
        self.action_undo.setObjectName(_fromUtf8("action_undo"))
        self.action_stats = QtGui.QAction(self.window)
        self.action_stats.setObjectName(_fromUtf8("action_stats"))
        self.menuOthello.addAction(self.action_new_game)
        self.menuOthello.addAction(self.action_undo)
        self.menuOptions.addAction(self.action_stats)
        self.menubar.addAction(self.menuOthello.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())

        self.length = 8
        self.buttons = [[OthelloCell(self.game.grid.read_element(i,j))
            for i in range(self.length)]
            for j in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                self.game_layout.addWidget(self.buttons[i][j],i,j)

        self.window.show()

    def retranslateUi(self):
        """Affiche les textes de l'interface principale"""
        self.window.setWindowTitle("Othello")
        self.player_1.setText("Player 1")
        self.score_1.setText("Score 1")
        self.player_2.setText("Player 2")
        self.score_2.setText("Score 2")
        self.menuOthello.setTitle("Game")
        self.menuOptions.setTitle("Options")
        self.action_new_game.setText("New Game")
        self.action_undo.setText("Undo")
        self.action_stats.setText("Stats")

    def start(self):
        """Gère les événements : boutons cliqués, signaux émis"""
        for i in range(self.length):
            for j in range(self.length):
                self.window.connect(self.buttons[i][j], QtCore.SIGNAL('clicked()'), self.cell_clicked(i,j))
        self.window.connect(self.action_new_game, QtCore.SIGNAL('triggered()'), self.new_game)
        self.window.connect(self.action_stats, QtCore.SIGNAL('triggered()'), self.stats)

    def cell_clicked(self,i,j):
        """Renvoie une fonction permettant de lancer le tour en cas d'activation d'une
        case valide"""
        return lambda:self.cell_test(i,j)

    def cell_test(self,i,j):
        print("Case "+str(i)+","+str(j)+" activee")

    def new_game(self):
        """Affiche le menu permettant de rentrer les paramètres pour lancer un nouveau jeu"""
        # Les objets ne sont pas des attributs de la classe car ils n'ont pas
        # vocation à exister hors de cette fonction
        self.new_game_window = QtGui.QMainWindow()
        central_widget = QtGui.QWidget(self.new_game_window)
        self.new_game_window.setCentralWidget(central_widget)
        layout = QtGui.QGridLayout()
        central_widget.setLayout(layout)
        player_1_label = QtGui.QLabel("Noir :")
        layout.addWidget(player_1_label,0,0)
        player_2_label = QtGui.QLabel("Blanc :")
        layout.addWidget(player_2_label,1,0)
        player_1_name = QtGui.QLineEdit("Joueur 1")
        layout.addWidget(player_1_name,0,1)
        player_2_name = QtGui.QLineEdit("Joueur 2")
        layout.addWidget(player_2_name,1,1)
        AI_box = QtGui.QCheckBox("IA")
        layout.addWidget(AI_box,2,0)
        start_button = QtGui.QPushButton("Commencer")
        layout.addWidget(start_button,3,3)
        self.new_game_window.setWindowTitle("New Game")
        self.new_game_window.show()
        start_button.clicked.connect(self.ok)

        # Mise en place des paramètres avec set_parameters
        #start_button.clicked.connect(lambda:self.set_parameters(
        #	player_1_name.text(),player_2_name.text(),
        #	AI_box.isChecked()))

    def stats(self):
        """Affiche la fenêtre contenant les statistiques du jeu"""
        # Les objets ne sont pas des attributs de la classe car ils n'ont pas
        # vocation à exister hors de cette fonction
        self.stats_window = QtGui.QMainWindow()
        central_widget = QtGui.QWidget(self.stats_window)
        self.stats_window.setCentralWidget(central_widget)
        layout = QtGui.QGridLayout()
        central_widget.setLayout(layout)
        player_1_label = QtGui.QLabel("En construction")
        layout.addWidget(player_1_label,0,0)
        exit_button = QtGui.QPushButton("Continuer")
        layout.addWidget(exit_button,1,1)
        self.stats_window.setWindowTitle("Statistics")
        self.stats_window.show()
        self.stats_window.connect(exit_button, QtCore.SIGNAL('clicked()'), self.ok)

    def ok(self):
        print("Ok")

import sys
app = QtGui.QApplication(sys.argv)
ui = Ui_Window()
sys.exit(app.exec_())

