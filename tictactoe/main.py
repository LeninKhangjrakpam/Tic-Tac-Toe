import tkinter as tk

from app import GameApp

WIN_WIDTH = 400
WIN_HEIGHT = 500


def main():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}")

    # Make window non resizable
    root.wm_resizable(width=False, height=False)

    root.iconbitmap("assets\icon.ico")

    app = GameApp(root, WIN_WIDTH, WIN_HEIGHT)

    root.mainloop()


if __name__ == "__main__":
    main()
