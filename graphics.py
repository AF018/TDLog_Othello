"""Partie graphique du jeu d'Othello"""

# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from tools_graphics import OthelloCell, add_name, Profiles
from tools_game import Game

class OthelloWindow():
    def __init__(self):
        """Récupère les statistiques pour pouvoir les modifier et lance une partie"""
        # Statistiques dans un fichier csv, lecture de chaque ligne du document pour récupérer
        self.profiles = Profiles()
        self.new_game()

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
        layout.addWidget(player_1_label, 0, 0)
        player_2_label = QtGui.QLabel("Blanc :")
        layout.addWidget(player_2_label, 1, 0)
        player_1_name = QtGui.QComboBox()
        player_1_name.addItems(self.profiles.names())
        layout.addWidget(player_1_name, 0, 1)
        player_2_name = QtGui.QComboBox()
        player_2_name.addItems(self.profiles.names())
        layout.addWidget(player_2_name, 1, 1)
        AI_box = QtGui.QCheckBox("IA")
        layout.addWidget(AI_box, 2, 0)
        creator_label = QtGui.QLabel("Nouveau profil :")
        layout.addWidget(creator_label, 3, 0)
        creator_text = QtGui.QLineEdit()
        layout.addWidget(creator_text, 3, 1)
        creator_button = QtGui.QPushButton("Créer profil")
        layout.addWidget(creator_button, 3, 2)
        start_button = QtGui.QPushButton("Commencer")
        layout.addWidget(start_button, 4, 3)
        self.new_game_window.setWindowTitle("Nouvelle partie")
        self.new_game_window.show()
        AI_box.stateChanged.connect(lambda: player_2_name.setEnabled(not AI_box.isChecked()))
        # Ajout du nouveau profil à la liste des noms s'il n'existe pas déjà
        creator_button.clicked.connect(lambda: add_name(player_1_name, creator_text.text(),
                                                        self.profiles.names()))
        creator_button.clicked.connect(lambda: add_name(player_2_name, creator_text.text(),
                                                        self.profiles.names()))
        creator_button.clicked.connect(lambda: self.profiles.new_profile(creator_text.text()))
        # Lancement du jeu avec les paramètres rentrés
        start_button.clicked.connect(lambda: self.set_parameters(player_1_name.currentText(),
                                                                 player_2_name.currentText(),
                                                                 not AI_box.checkState()))

    def set_parameters(self, player_1_text, player_2_text, pvp_option):
        """Crée le jeu puis l'affiche"""
        if player_1_text == player_2_text and pvp_option:
            return
        self.game = Game(player_1_text, player_2_text, pvp_option, -1)
        self.new_game_window.close()
        self.setup_window()
        self.setup_connections()

    def setup_window(self):
        """Affiche tous les éléments de l'interface principale"""
		# Création de tous les éléments de la fenêtre
        self.window = QtGui.QMainWindow()
        self.window.setObjectName("Window")
        self.window.resize(480, 560)
        self.window.setAnimated(True)
        self.centralwidget = QtGui.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.window.setCentralWidget(self.centralwidget)
        self.game_layout = QtGui.QGridLayout()
        self.centralwidget.setLayout(self.game_layout)
        self.window.setMaximumWidth(480)
        self.window.setMaximumHeight(560)
        self.game_layout.setHorizontalSpacing(0)
        self.game_layout.setVerticalSpacing(0)
        self.game_layout.setObjectName("game_layout")
        self.player_1 = QtGui.QLabel()
        self.player_1.setAlignment(QtCore.Qt.AlignCenter)
        self.player_1.setObjectName("player_1")
        self.game_layout.addWidget(self.player_1, 8, 0, 1, 1)
        self.score_1 = QtGui.QLabel()
        self.score_1.setAlignment(QtCore.Qt.AlignCenter)
        self.score_1.setObjectName("score_1")
        self.game_layout.addWidget(self.score_1, 8, 1, 1, 1)
        self.player_2 = QtGui.QLabel()
        self.player_2.setAlignment(QtCore.Qt.AlignCenter)
        self.player_2.setObjectName("player_2")
        self.game_layout.addWidget(self.player_2, 8, 7, 1, 1)
        self.score_2 = QtGui.QLabel()
        self.score_2.setAlignment(QtCore.Qt.AlignCenter)
        self.score_2.setObjectName("score_2")
        self.game_layout.addWidget(self.score_2, 8, 6, 1, 1)
        self.information_1_label = QtGui.QLabel()
        self.information_1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_1_label.setObjectName("information_1")
        self.game_layout.addWidget(self.information_1_label, 8, 3, 1, 1)
        self.information_2_label = QtGui.QLabel()
        self.information_2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_2_label.setObjectName("information_2")
        self.game_layout.addWidget(self.information_2_label, 8, 4, 1, 1)
        self.player_2.raise_()
        self.menubar = QtGui.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        self.menuOthello = QtGui.QMenu(self.menubar)
        self.menuOthello.setObjectName("menuOthello")
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)
        self.action_new_game = QtGui.QAction(self.window)
        self.action_new_game.setObjectName("action_new_game")
        self.action_stats = QtGui.QAction(self.window)
        self.action_stats.setObjectName("action_stats")
        self.menuOthello.addAction(self.action_new_game)
        self.menuOptions.addAction(self.action_stats)
        self.menubar.addAction(self.menuOthello.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        # Création et affichage des boutons du plateau
        self.length = 8
        self.buttons = [[OthelloCell(self.game.grid.read_element(i, j))
                         for i in range(self.length)] for j in range(self.length)]
        for i in range(self.length):
            for j in range(self.length):
                self.game_layout.addWidget(self.buttons[i][j], i, j)
        # Affichage des textes et couleurs de fond
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
        self.information_1_label.setStyleSheet("QLabel { color : blue; }")
        self.information_1_label.setText("Au tour de :")
        self.information_2_label.setStyleSheet("QLabel { color : blue; }")
        self.information_2_label.setText(self.game.player1.read_name())
        self.menuOthello.setTitle("Jeu")
        self.menuOptions.setTitle("Options")
        self.action_new_game.setText("Recommencer")
        self.action_stats.setText("Statistiques")
        # Initialisation des positions jouables
        self.playable_pos = self.game.valid_positions(self.game.current_player)[1]
        for i in range(self.length):
            for j in range(self.length):
                if (i, j) in self.playable_pos:
                    self.buttons[i][j].playable = 1
                else:
                    self.buttons[i][j].playable = 0
        # Affichage de la fenêtre de jeu
        self.window.show()

    def setup_connections(self):
        """Gère les événements : boutons cliqués, signaux émis"""
        for i in range(self.length):
            for j in range(self.length):
                self.window.connect(self.buttons[i][j], QtCore.SIGNAL('clicked()'),
                                    self.cell_clicked(i, j))
        self.window.connect(self.action_new_game, QtCore.SIGNAL('triggered()'),
                            lambda: self.profiles.increment_reboots((self.game.player1.read_name(),
                                                                     self.game.player2.read_name())))
        self.window.connect(self.action_new_game, QtCore.SIGNAL('triggered()'), self.restart)
        self.window.connect(self.action_stats, QtCore.SIGNAL('triggered()'), self.display_stats)

    def cell_clicked(self, i, j):
        """Renvoie une fonction permettant de lancer le tour en cas d'activation d'une
        case valide"""
        return lambda: self.play_this(i, j)

    def play_this(self, i, j):
        """Lance un tour,actualise l'interface graphique et la classe Game, joue un coup
        avec l'intelligence artificielle si le joueur a sélectionné cette option au départ"""
        if self.buttons[i][j].playable == 1:
            self.apply_move(i, j)
			# Calcul de toutes les positions jouables dans self.playable_pos
            self.playable_pos = self.game.valid_positions(self.game.current_player)[1]
            if len(self.playable_pos) == 0:
                # Changement de joueur si celui dont c'est le tour n'a pas de position admissible
                # On actualise le joueur dont c'est le tour ainsi que ses coups admissibles
                self.game.current_player = self.game.opponent(self.game.current_player)
                self.playable_pos = self.game.valid_positions(self.game.current_player)[1]
            elif not self.game.pvp:
                # L'IA joue, et rejoue si l'adversaire est bloqué
                # time_to_play indique si c'est le premier coup fait après celui de l'autre joueur
                time_to_play = True
                while((time_to_play or
                       len(self.game.valid_positions(self.game.opponent(self.game.current_player))[1]) == 0)
                      and not self.game.end_game()):
                    # Calcul du mouvement de l'IA
                    AI_pos = [0, 0]
                    self.game.AI_play(self.playable_pos, 1, 4, 4, self.game.opponent(self.game.current_player), AI_pos, -1e5, 1e5)
                    # On applique le mouvement en gardant l'IA comme joueur actuel
                    self.apply_move(AI_pos[0], AI_pos[1])
                    self.game.current_player = self.game.opponent(self.game.current_player)
                    # On passe time_to_play a False : l'IA ne rejoue que si l'autre joueur n'a pas de coup admissible
                    time_to_play = False
                # Une fois le(s) coup(s) de l'IA joué(s), on met comme joueur courant le joueur humain et on
                # calcule ses coups admissibles
                self.game.current_player = self.game.opponent(self.game.current_player)
                self.playable_pos = self.game.valid_positions(self.game.current_player)[1]
            # On actualise l'affichage du plateau
            self.refresh_display()
            if self.game.end_game():
                self.finish_game()

    def apply_move(self, i, j):
        """Applique le coup (i,j), et change le joueur actuel"""
        # Calcul des positions des pions qui vont être "en bout de ligne" pour les retournements
        origins = self.game.origins(i, j, self.game.current_player)
        # Commande permettant de jouer le mouvement proposé
        self.game.play_one_shot(i, j, self.game.current_player)
        # Effectue tous les retournements de pion engendrés par le coup
        self.game.turn_pawn(i, j, self.game.current_player, *origins)
		# Changement de joueur
        self.game.current_player = self.game.opponent(self.game.current_player)

    def refresh_display(self):
        """Met à jour l'affichage de la grille"""
        self.information_2_label.setText(self.game.current_player.read_name())
        self.score_1.setText(str(self.game.player1.read_score()))
        self.score_2.setText(str(self.game.player2.read_score()))
        for k in range(self.length):
            for l in range(self.length):
                self.buttons[k][l].refresh(self.game.grid.read_element(k, l), (k, l) in self.playable_pos)

    def finish_game(self):
        """Affiche le gagnant, met à jour les statistiques et les enregistre, puis les affiche"""
        (winner,loser) = self.game.winner()
        self.information_1_label.setText("Gagnant :")
        self.information_2_label.setText(winner)
        # Mise a jour des statistiques
        self.profiles.update_stats(winner, loser, self.game.pvp)
        self.display_stats()

    def restart(self):
        """Relance une nouvelle partie en formatant les données de l'ancienne"""
        self.game.empty_game()
        self.playable_pos = self.game.valid_positions(self.game.current_player)[1]
        self.refresh_display()

    def display_stats(self):
        """Affiche la fenêtre contenant les statistiques du jeu"""
        # Les objets ne sont pas des attributs de la classe car ils n'ont pas
        # vocation à exister hors de cette fonction
        self.stats_window = QtGui.QMainWindow()
        self.stats_window.setStyleSheet("QMainWindow {background: 'darkgrey';}")
        central_widget = QtGui.QWidget(self.stats_window)
        self.stats_window.setCentralWidget(central_widget)
        layout = QtGui.QGridLayout()
        central_widget.setLayout(layout)
        player_label = QtGui.QLabel("Joueur :")
        layout.addWidget(player_label, 0, 0)
        player_name = QtGui.QComboBox()
        player_name.addItems(self.profiles.names())
        layout.addWidget(player_name, 0, 1)
        games_label = QtGui.QLabel("Nombre de parties jouées")
        layout.addWidget(games_label, 1, 0)
        games_nb = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 1))
        layout.addWidget(games_nb, 1, 1)
        reboot_label = QtGui.QLabel("Nombre de parties recommencées :")
        layout.addWidget(reboot_label, 1, 2)
        reboot_nb = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 6))
        layout.addWidget(reboot_nb, 1, 3)
        pvpw_label = QtGui.QLabel("Nombre de parties gagnées, sans IA :")
        layout.addWidget(pvpw_label, 2, 0)
        pvpw_games = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 2))
        layout.addWidget(pvpw_games, 2, 1)
        pvpl_label = QtGui.QLabel("Nombre de parties perdues, sans IA :")
        layout.addWidget(pvpl_label, 2, 2)
        pvpl_games = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 3))
        layout.addWidget(pvpl_games, 2, 3)
        aiw_label = QtGui.QLabel("Nombre de parties gagnées, avec IA :")
        layout.addWidget(aiw_label, 3, 0)
        aiw_games = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 4))
        layout.addWidget(aiw_games, 3, 1)
        ail_label = QtGui.QLabel("Nombre de parties perdues, avec IA :")
        layout.addWidget(ail_label, 3, 2)
        ail_games = QtGui.QLabel(self.profiles.information(player_name.currentIndex(), 5))
        layout.addWidget(ail_games, 3, 3)
        exit_button = QtGui.QPushButton("Continuer")
        layout.addWidget(exit_button, 4, 4)
        self.stats_window.setWindowTitle("Statistiques")
        self.stats_window.show()
        self.stats_window.connect(exit_button, QtCore.SIGNAL('clicked()'), self.stats_window.close)
        player_name.currentIndexChanged.connect(lambda: games_nb.setText(self.profiles.information(player_name.currentIndex(), 1)))
        player_name.currentIndexChanged.connect(lambda: pvpw_games.setText(self.profiles.information(player_name.currentIndex(), 2)))
        player_name.currentIndexChanged.connect(lambda: pvpl_games.setText(self.profiles.information(player_name.currentIndex(), 3)))
        player_name.currentIndexChanged.connect(lambda: aiw_games.setText(self.profiles.information(player_name.currentIndex(), 4)))
        player_name.currentIndexChanged.connect(lambda: ail_games.setText(self.profiles.information(player_name.currentIndex(), 5)))
        player_name.currentIndexChanged.connect(lambda: reboot_nb.setText(self.profiles.information(player_name.currentIndex(), 6)))

import sys
app = QtGui.QApplication(sys.argv)
oth_win = OthelloWindow()
sys.exit(app.exec_())

