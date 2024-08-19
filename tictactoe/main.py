import tkinter as tk
import os

from app import GameApp

WIN_WIDTH = 400
WIN_HEIGHT = 500


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # Make window non resizable
    root.wm_resizable(width=False, height=False)
    # Icon
    root.iconbitmap(os.path.join("assets", "icon.ico"))

    splash_icon_loc = os.path.join("assets", "icon.png")
    app = GameApp(root, WIN_WIDTH, WIN_HEIGHT, splash_icon_loc)

    root.mainloop()


if __name__ == "__main__":
    main()
