from tkinter import*
# Create class for main window of the application.
#  This class will handle the initialization of the main window, setting its title, size, and any other configurations.
#  It will also include methods for adding widgets and handling user interactions.⬇️
class Mainwindows:
        def __init__(self, tk):

#---------Start windows--------
                self.tk = tk
                self.tk.title("Study manager")
                self.tk.geometry("1200x700")
                self.tk.config(bg="white")
                self.tk.grid_rowconfigure(0, weight=1) 
                self.tk.grid_columnconfigure(1, weight=1)
                # self.tk.iconbitmap("..\\Icon_Image\\study-manager-icon.ico")
#---------End windows--------

