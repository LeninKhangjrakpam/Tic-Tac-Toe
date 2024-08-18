import tkinter as tk


class ResultPage:
    """Class to create game result page UI
    """
    quit_button: tk.Button = None
    play_again_button: tk.Button = None

    @staticmethod
    def render_page(root: tk.Tk, player: int, handler: Callable[[str], None]):
        """Render the Page

        Args:
            root (tk.Tk): tkinter window
            player (int): player number
            handler (Callable[[str], None]): _description_
        """
        label = tk.Label(
            root, text=f"Winner : {player}", font=("Helvetica", 30))
        label.place(x=100, y=100)

        ResultPage.play_again_button = tk.Button(
            root, text="Play Again", font=("Helvetica", 20),
            command=lambda: handler("play_again"))

        ResultPage.quit_button = tk.Button(
            root, text="Quit", font=("Helvetica", 20),
            command=lambda: handler("quit"))

        ResultPage.play_again_button.place(x=100, y=200)
        ResultPage.quit_button.place(x=100, y=300)
