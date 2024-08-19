import tkinter as tk
import os


class SplashPage:
    """Class to create game board page UI
    """

    @staticmethod
    def render_page(root: tk.Tk, win_width: int, win_height: int, splash_icon: tk.PhotoImage):
        """Render page
        """
        # CLear window component
        for i in root.winfo_children():
            i.destroy()

        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        panel = tk.Label(
            frame,
            image=splash_icon,
            height=300,
            width=300
        )
        panel.pack()
        panel.place(relx=0.5, rely=0.4, anchor='center')
        # panel.pack(fill="both", expand=True)

        panel1 = tk.Label(
            frame,
            text="Tic Tac Toe",
            font=("Helvetica", 30)
        )
        panel1.place(relx=0.5, rely=0.7, anchor='center')
