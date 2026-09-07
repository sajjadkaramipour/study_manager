from ui.main_windows import Mainwindows
from tkinter import*


if __name__ == "__main__":      # This code runs main_windows.py at starting of application.
    tk = Tk()
    app = Mainwindows(tk)
    app.run()