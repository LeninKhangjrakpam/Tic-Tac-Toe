import tkinter as tk
import sys
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
    root.iconbitmap(resource_path(os.path.join("assets", "icon.ico")))

    splash_icon_loc = resource_path(os.path.join("assets", "icon.png"))
    app = GameApp(root, WIN_WIDTH, WIN_HEIGHT, splash_icon_loc)

    root.mainloop()


def resource_path(rel_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = getattr(sys, '_MEIPASS')
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, rel_path)


if __name__ == "__main__":
    main()
