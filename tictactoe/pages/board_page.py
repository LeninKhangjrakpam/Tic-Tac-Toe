import tkinter as tk
from typing import Callable, Union, List


class BoardPage:
    """Class to create game board page UI
    """
    cells: List[Union[tk.Button, None]] = [None for _ in range(9)]
    cur_player_label: Union[tk.Label, None] = None
    warning_label: Union[tk.Label, None] = None

    @staticmethod
    def render_page(
            root: tk.Tk,
            curPlayer: int,
            boardState: List[List[Union[int, None]]],
            handler: Callable[[int, int], None]):
        """Render the page

        Args:
            root (tk.Tk): _description_
            curPlayer (int): current player
            boardState (List[List[Union[int, None]]]): state of the board to be rendered
            handler (Callable): _description_
        """
        # Clear previous page
        for i in root.winfo_children():
            i.destroy()

        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(frame, text="Board Page", font=("Helvetica", 30))
        label.pack()

        BoardPage.cur_player_label = tk.Label(
            frame, text=f"Current Player: {curPlayer}", font=("Helvetica", 20))
        BoardPage.cur_player_label.pack()

        BoardPage.warning_label = tk.Label(
            frame, text=f"", font=("Helvetica", 20))
        BoardPage.warning_label.pack()

        m_left = (root.winfo_width() - 70*3) / 2
        for i, row in enumerate(boardState):
            for j, elm in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=f"{'X' if elm == 0 else 'O' if elm == 1 else ' '}",
                    font=("Helvetica", 50),
                    command=lambda r=i, c=j: handler(r, c)
                )
                btn.place(x=j*70 + m_left, y=i*70 + 150, height=70,
                          width=70)
                BoardPage.cells[i * 3 + j] = btn

    @staticmethod
    def update_page(
            root: tk.Tk,
            curPlayer: int,
            boardState: List[List[Union[int, None]]]):
        """Update the board component of Board page

        Args:
            root (tk.Tk): tkinter window
            curPlayer (int): current player
            boardState (List[List[Union[int, None]]]): board state
        """
        # Clear Warning labels
        BoardPage.warning_label.config(
            text="", background="#%02x%02x%02x" % (250, 240, 237))
        BoardPage.cur_player_label.config(text=f"Current Player: {curPlayer}")

        for i, btn in enumerate(BoardPage.cells):
            elm = boardState[i // 3][i % 3]
            sym = 'X' if elm == 0 else 'O' if elm == 1 else ' '
            btn.config(
                text=f"{sym}",
                background="salmon" if sym == 'O' else "lawngreen" if sym == "X" else None)

    @staticmethod
    def disable_cells():
        """Disabled cells"""
        for btn in BoardPage.cells:
            btn["state"] = "disabled"

    @staticmethod
    def display_warning(text: str):
        """Display warning to user 

        Args:
            text (str): warning message
        """
        BoardPage.warning_label.config(
            text=text, background="salmon")
