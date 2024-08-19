import tkinter as tk
from typing import Callable


class ResultPage:
    """Class to create game result page UI
    """
    quit_button: tk.Button = None
    play_again_button: tk.Button = None

    @staticmethod
    def render_page(root: tk.Tk, text: str, width: int, height: int, handler: Callable[[str], None]):
        """Render the Page

        Args:
            root (tk.Tk): tkinter window
            player (int): player number
            handler (Callable[[str], None]): _description_
        """
        label = tk.Label(
            root, text=text, font=("Helvetica", 30), background="white")

        label.place(relx=0.5, rely=0.2, anchor='center')

        ResultPage.play_again_button = tk.Button(
            root, text="Play Again", font=("Helvetica", 20),
            command=lambda: handler("play_again"))

        ResultPage.quit_button = tk.Button(
            root, text="Quit", font=("Helvetica", 20),
            command=lambda: handler("quit"))

        ResultPage.play_again_button.place(relx=0.1, rely=0.85)
        ResultPage.quit_button.place(relx=0.7, rely=0.85)
