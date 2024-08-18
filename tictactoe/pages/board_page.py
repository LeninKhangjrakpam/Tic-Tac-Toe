import tkinter as tk
from typing import Callable, Union, List


class BoardPage:
    """Class to create game board page UI
    """
    cells: list[tk.Button] = []

    @staticmethod
    def render_page(
            root: tk.Tk,
            boardState: List[List[Union[int, None]]],
            handler: Callable[[int, int], None]):
        """Render the page

        Args:
            root (tk.Tk): _description_
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

        m_left = (root.winfo_width() - 70*3) / 2
        for i, row in enumerate(boardState):
            for j, elm in enumerate(row):
                btn = tk.Button(
                    frame,
                    text=f"{'X' if elm == 0 else 'O' if elm == 1 else ' '}",
                    font=("Helvetica", 50),
                    command=lambda r=i, c=j: handler(r, c)
                )
                btn.place(x=i*70 + m_left, y=j*70 + 100, height=70,
                          width=70)
                BoardPage.cells.append(btn)

    @staticmethod
    def update_page(root: tk.Tk, boardState: List[List[Union[int, None]]]):
        """Update the board component of Board page

        Args:
            root (tk.Tk): tkinter window
            boardState (List[List[Union[int, None]]]): board state
        """
        for i, btn in enumerate(BoardPage.cells):
            elm = boardState[i // 3][1 % 3]
            sym = 'X' if elm == 0 else 'O' if elm == 1 else ' '
            btn.config(
                text=f"{sym}",
                background="salmon" if sym == 'O' else "lawngreen" if sym == "X" else None)
