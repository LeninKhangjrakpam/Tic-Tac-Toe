import tkinter as tk


class EndPage:
    """Class to create game result page UI
    """

    @staticmethod
    def render_page(root: tk.Tk):
        """Render the page

        Args:
            root (tk.Tk): tkinter window
        """
        # Clear screen
        for i in root.winfo_children():
            i.destroy()

        frame = tk.Frame(root)
        frame.pack(fill=tk.BOTH, expand=True)

        label = tk.Label(frame, text="Bye !", font=("Helvetica", 30))
        label.pack(fill=tk.BOTH, expand=True)
