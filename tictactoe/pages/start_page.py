import tkinter as tk
from typing import Callable


class StartPage:
    """Class to create game start page UI
    """
    selected_player: int = None
    label: tk.Label = None
    buttons: list[tk.Button] = [None, None]

    @staticmethod
    def render_page(root: tk.Tk, handler: Callable[[int], None]):
        """Render the page

        Args:
            root (tk.Tk): tkinter window
            handler (_type_): _description_
        """
        # Clear previous page
        for i in root.winfo_children():
            i.destroy()

        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(frame, text="Choose Player:", font=("Helvetica", 30))
        label.pack(pady=(20, 10))

        btn_x = tk.Button(
            frame, text="X", font=("Helvetica", 20),
            background='#%02x%02x%02x' % (250, 240, 237),
            command=lambda: StartPage.set_player(root, 0))

        # btn_x.place(x=100, y=400 // 2 - 50, height=50, width=50)
        btn_x.place(x=root.winfo_width() // 2 - 60,
                    y=root.winfo_width() // 2 - 50, height=50, width=50)
        StartPage.buttons[0] = btn_x

        btn_o = tk.Button(
            frame, text="O", font=("Helvetica", 20),
            background='#%02x%02x%02x' % (250, 240, 237),
            command=lambda: StartPage.set_player(root, 1))

        btn_o.place(x=root.winfo_width() // 2 + 10,
                    y=root.winfo_width() // 2 - 50, height=50, width=50)
        StartPage.buttons[1] = btn_o

        btn_continue = tk.Button(frame, text="Continue", font=(
            "Helvetica", 20), command=lambda: StartPage.confirm_selection(root, handler))
        btn_continue.place(y=300, x=100)

    @staticmethod
    def set_player(root: tk.Tk, player: int):
        """Set the selected player number

        Args:
            root (tk.Tk): tkinter window
            player (int): player number
        """
        StartPage.selected_player = player
        StartPage.label.config(
            text=f"Choose Player: {StartPage.selected_player}")

        # Highlight selected button
        for i, btn in enumerate(StartPage.buttons):
            if i == StartPage.selected_player:
                btn.config(background="salmon")
            else:
                btn.config(background='#%02x%02x%02x' % (250, 240, 237))

    @staticmethod
    def confirm_player(root: tk.Tk, handler: Callable[[int], None]):
        """Handle confirm button click

        Args:
            root (tk.Tk): tkinter window
            handler (Callable[[int], None]): function to call when confirm button is click
        """
        if StartPage.selected_player == None:
            print("Please select a player, then confirm it")
            StartPage.label.config(text="Please select a player first")
        else:
            print(f"Player {StartPage.selected_player} confirmed")
            handler(StartPage.selected_player)
