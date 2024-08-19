import sys
import tkinter as tk

from game.game import TicTacToe
from move.move import ComputerMove

from pages.start_page import StartPage
from pages.board_page import BoardPage
from pages.result_page import ResultPage
from pages.end_page import EndPage


class GameApp:
    """Class that implement the main game
    """

    def __init__(self, master: tk.Tk, win_width, win_height):
        self.app = master
        self.win_width = win_width
        self.win_height = win_height

        self.game = None
        self.human_player_num = None
        self.ai_player = None

        print("Starting")
        self.start_page()

    def start_page(self):
        """Render the game start Page
        """
        # self.game_over = False
        StartPage.render_page(
            self.app, self.win_width,
            self.win_height,  self.start_page_handler)

    def start_page_handler(self, player: int):
        """Start page handler, responsible for getting user form player and transitioning to boardPage

        Args:
            player (int): player selected by the user
        """
        print("app selected player: ", player)
        print("Iniitialising game, computerMove")

        self.game = TicTacToe()
        self.human_player_num = player
        self.ai_player = ComputerMove(self.game)

        self.board_page()

    def board_page(self):
        """Render the board page
        """

        BoardPage.render_page(
            self.app, self.game.curPlayer, self.game.curState, self.board_page_handler)
        print("Finish first board render", self.game.curPlayer)

        # if ai need to make the first move
        if self.game.curPlayer != self.human_player_num:
            BoardPage.update_page(
                self.app, self.game.curPlayer, self.game.curState)

            action = self.ai_player.get_alpha_beta()
            self.game.move(action)

            BoardPage.update_page(
                self.app, self.game.curPlayer, self.game.curState)

    def board_page_handler(self, row: int, col: int):
        """Handler for board cell click
        Responsible for updating board state and transitioning to result page
        """
        print(row, col)
        print(self.game.curPlayer, self.game.curState)

        # if game is over
        if self.game.terminal():
            self.result_page()
            return

        # Human turn
        action = {"row": row, "col": col, "player": self.game.curPlayer}
        if not self.game.check_action(action):
            # If move is not valid
            BoardPage.display_warning("Invalid Move")
            # self.app.after(
            #     50, lambda: BoardPage.display_warning("Invalid Move"))
            print("invalid move")
            return

        self.game.move(action)
        print(self.game.curPlayer, self.game.curState)
        # Render after human move
        BoardPage.update_page(
            self.app, self.game.curPlayer, self.game.curState)
        # self.app.after(
        #     50, lambda: BoardPage.update_page(
        #         self.app, self.game.curPlayer, self.game.curState))

        # if game is over
        if self.game.terminal():
            self.result_page()
            return

        # AI Turn
        action = self.ai_player.get_alpha_beta()
        print("Before ai: ", self.game.curPlayer, self.game.curState, action)
        self.game.move(action)
        print("After ai: ", self.game.curPlayer, self.game.curState)
        # Render after ai move
        BoardPage.update_page(
            self.app, self.game.curPlayer, self.game.curState)
        # self.app.after(50, lambda: BoardPage.update_page(
        #     self.app, self.game.curPlayer, self.game.curState))
        print("After ai render")

        # if game is over
        if self.game.terminal():
            self.result_page()
            return

    # def board_page_handler(self, row: int, col: int):
    #     """Handler for board cell click
    #     Responsible for updating board state and transitioning to result page
    #     """
    #     print(row, col)
    #     print(self.game.curPlayer, self.game.curState)
    #     # if game is over
    #     if self.game.terminal():
    #         self.result_page()
    #         return

    #     # Human turn
    #     action = {"row": row, "col": col, "player": self.game.curPlayer}
    #     if not self.game.check_action(action):
    #         # If move is not valid
    #         BoardPage.display_warning("Invalid Move")
    #         print("invalid move")
    #         return

    #     self.game.move(action)
    #     print(self.game.curPlayer, self.game.curState)
    #     # Render after human move
    #     BoardPage.update_page(
    #         self.app, self.game.curPlayer, self.game.curState)

    #     # if game is over
    #     if self.game.terminal():
    #         self.result_page()
    #         return

    #     # AI Turn
    #     action = self.ai_player.get_alpha_beta()
    #     self.game.move(action)
    #     # Render after ai move
    #     BoardPage.update_page(
    #         self.app, self.game.curPlayer, self.game.curState)

    def result_page(self):
        """Render the result page
        """
        BoardPage.disable_cells()

        win_res, win_player, win_strip = self.game.winner()
        if win_res == 1:
            ResultPage.render_page(
                self.app, f"Winner: Player{win_player}", self.win_width, self.win_height, self.result_page_handler)
        elif win_res == 0:
            ResultPage.render_page(
                self.app, "Draw", self.win_width, self.win_height, self.result_page_handler)
        else:
            print("error: ", win_res, win_player, win_strip)

    def result_page_handler(self, evntName: str):
        """Handler responsible for result page 

        Args:
            evntName (str): quit or playagain
        """
        if evntName == "quit":
            self.end_page()
        else:
            self.game.reset()
            self.start_page()

    def end_page(self):
        """Render the end page
        """
        EndPage.render_page(self.app)
        self.app.after(800, lambda: sys.exit())
