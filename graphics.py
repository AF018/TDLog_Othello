# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from csv import reader,writer
from utils import OthelloCell
import tools
from tools_game import Game

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
        """Récupère les statistiques pour pouvoir les modifier et lance un nouveau jeu"""
        # Statistiques dans un fichier csv, lecture de chaque ligne du document pour récupérer
        with open("stats.csv", newline = '\n') as text:
            content = reader(text, delimiter = ',')
            self.stats_tab=[[int(number) for number in line] for line in content]
        print(self.stats_tab)
        self.new_game()

    def setupUi(self):
        """Affiche tous les éléments de l'interface principale"""
		# Création de tous les éléments de la fenêtre
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
        self.game_layout.addWidget(self.player_2, 8, 7, 1, 1)
        self.score_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.score_2.setObjectName(_fromUtf8("score_2"))
        self.game_layout.addWidget(self.score_2, 8, 6, 1, 1)
        self.information_1_label = QtGui.QLabel(self.gridLayoutWidget)
        self.information_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_1_label.setObjectName(_fromUtf8("information_1"))
        self.game_layout.addWidget(self.information_1_label, 8, 3, 1, 1)
        self.information_2_label = QtGui.QLabel(self.gridLayoutWidget)
        self.information_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_2_label.setObjectName(_fromUtf8("information_2"))
        self.game_layout.addWidget(self.information_2_label, 8, 4, 1, 1)
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
        # Création et affichage des boutons du plateau
        self.length = 8
        self.buttons = [[OthelloCell(self.game.grid.read_element(i,j))
            for i in range(self.length)]
            for j in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                self.game_layout.addWidget(self.buttons[i][j],i,j)
        # Affichage de la fenêtre de jeu
        self.window.show()

    def retranslateUi(self):
        """Affiche les textes de l'interface principale"""
        self.window.setStyleSheet("QMainWindow {background: 'darkgrey';}")
        self.window.setWindowTitle("Othello")
        self.player_1.setStyleSheet("QLabel { color : black; }")
        self.player_1.setText(self.game.player1.read_name())
        self.score_1.setStyleSheet("QLabel { color : black; }")
        self.score_1.setText(str(self.game.player1.read_score()))
        self.player_2.setStyleSheet("QLabel { color : white; }")
        self.player_2.setText(self.game.player2.read_name())
        self.score_2.setStyleSheet("QLabel { color : white; }")
        self.score_2.setText(str(self.game.player2.read_score()))
        self.information_1_label.setText("Au tour de :")
        self.information_2_label.setText(self.game.player1.read_name())
        self.menuOthello.setTitle("Game")
        self.menuOptions.setTitle("Options")
        self.action_new_game.setText("New Game")
        self.action_undo.setText("Undo")
        self.action_stats.setText("Stats")

    def start(self):
        """Gère les événements : boutons cliqués, signaux émis"""
        playable_pos = self.game.valid_positions(self.game.current_player)[1]
        for i in range(self.length):
            for j in range(self.length):
                if (i,j) in playable_pos:
                    self.buttons[i][j].playable = 1
                else:
                    self.buttons[i][j].playable = 0
                self.window.connect(self.buttons[i][j], QtCore.SIGNAL('clicked()'), self.cell_clicked(i,j))
        self.window.connect(self.action_new_game, QtCore.SIGNAL('triggered()'), self.new_game)
        self.window.connect(self.action_stats, QtCore.SIGNAL('triggered()'), self.stats)

    def cell_clicked(self,i,j):
        """Renvoie une fonction permettant de lancer le tour en cas d'activation d'une
        case valide"""
        print("premier appel")
        return lambda:self.play_this(i,j)

    def play_this(self,i,j):
        """Lance un tour,actualise l'interface graphique et la classe Game"""
        print("entendu")
        if self.buttons[i][j].playable==1:
            # Calcul des positions des pions qui vont être "en bout de ligne" pour les retournements
            origins=self.game.origins(i,j,self.game.current_player)
            # Commande permettant de jouer le mouvement proposé
            self.game.play_one_shot(i,j,self.game.current_player)
            # Effectue tous les retournements de pion engendrés par le coup
            self.game.turn_pawn(i,j,self.game.current_player,*origins)
			# Changement de joueur
            self.game.current_player=self.game.opponent(self.game.current_player)
			# Calcul de toutes les positions jouables dans playable_pos
            playable_pos = self.game.valid_positions(self.game.current_player)[1]
            if len(playable_pos)==0:
                # Changement de joueur si celui dont c'est le tour n'a pas de position admissible
                self.game.current_player=self.game.opponent(self.game.current_player)
                playable_pos = self.game.valid_positions(self.game.current_player)[1]
            self.information_2_label.setText(self.game.current_player.read_name())
            self.score_1.setText(str(self.game.player1.read_score()))
            self.score_2.setText(str(self.game.player2.read_score()))
            for k in range(self.length):
                for l in range(self.length):
                    self.buttons[k][l].refresh(self.game.grid.read_element(k,l),(k,l) in playable_pos)
            if self.game.end_game():
                self.finish_game()
                #probleme sur certaines cases au relancement d'une partie
				#checker le vainqueur a la fin du jeu
                #reorganiser les fonctions et autres pour plus de lisibilité
                #le probleme est dependant deterministiquement des positions précédentes
        self.game.display()
        return

    def finish_game(self):
        self.information_1_label.setText("Gagnant :")
        self.information_2_label.setText("")
        # Mise a jour des statistiques
        self.stats_tab[0][0]+=1
        self.stats_tab[0][1]+=1
        with open("stats.csv", 'w') as text:
            content = writer(text)
            content.writerows([[str(number) for number in line] for line in self.stats_tab])
        self.stats()

    def cell_test(self,i,j):
        print("Case "+str(i)+","+str(j)+" activee")

    def set_parameters(self,player_1_name,player_2_name):
        self.game = Game(player_1_name,player_2_name)
        self.new_game_window.close()
        self.setupUi()
        self.retranslateUi()
        self.start()

    def new_game(self):
        """Affiche le menu permettant de rentrer les paramètres pour lancer un nouveau jeu"""
        # Les objets ne sont pas des attributs de la classe car ils n'ont pas
        # vocation à exister hors de cette fonction
        self.new_game_window = QtGui.QMainWindow()
        self.new_game_window.setStyleSheet("QMainWindow {background: 'darkgrey';}")
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
        self.new_game_window.setWindowTitle("Nouvelle partie")
        self.new_game_window.show()
        start_button.clicked.connect(lambda:self.set_parameters(player_1_name.text(),player_2_name.text()))

    def stats(self):
        """Affiche la fenêtre contenant les statistiques du jeu"""
        # Les objets ne sont pas des attributs de la classe car ils n'ont pas
        # vocation à exister hors de cette fonction
        self.stats_window = QtGui.QMainWindow()
        self.stats_window.setStyleSheet("QMainWindow {background: 'darkgrey';}")
        central_widget = QtGui.QWidget(self.stats_window)
        self.stats_window.setCentralWidget(central_widget)
        layout = QtGui.QGridLayout()
        central_widget.setLayout(layout)
        games_label = QtGui.QLabel("Nombre de parties :")
        layout.addWidget(games_label,0,0)
        games = QtGui.QLabel(str(self.stats_tab[0][0]))
        layout.addWidget(games,0,1)
        not_AI_games_label = QtGui.QLabel("Nombre de parties sans IA :")
        layout.addWidget(not_AI_games_label,1,0)
        not_AI_games = QtGui.QLabel(str(self.stats_tab[0][1]))
        layout.addWidget(not_AI_games,1,1)
        AI_games_label = QtGui.QLabel("Nombre de parties avec IA :")
        layout.addWidget(AI_games_label,2,0)
        AI_games = QtGui.QLabel(str(self.stats_tab[0][2]))
        layout.addWidget(AI_games,2,1)
        exit_button = QtGui.QPushButton("Continuer")
        layout.addWidget(exit_button,3,2)
        self.stats_window.setWindowTitle("Statistics")
        self.stats_window.show()
        self.stats_window.connect(exit_button, QtCore.SIGNAL('clicked()'), lambda:self.stats_window.close())

    def ok(self):
        print("Ok")

import sys
app = QtGui.QApplication(sys.argv)
ui = Ui_Window()
sys.exit(app.exec_())

