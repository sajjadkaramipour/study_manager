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

#---------Start sidebar--------
                sidebar = Frame(self.tk, bg="indigo", width=240)
                sidebar.grid(row=0, column=0, sticky="nsew")
                sidebar.grid_propagate(False)
                sidebar.grid_columnconfigure(0, weight=1)
                sidebar.grid_rowconfigure(0, weight=1)

                subjects_button=Button(sidebar, text="Subjects", bg="indigo", font=("Segoe UI",16)
                , fg="white", bd=0, highlightthickness = 0, pady=5)
                subjects_button.grid(row=0, column=0, sticky="new")

                timer_button=Button(sidebar, text="Timer", bg="indigo", font=("Segoe UI",16)
                , fg="white", bd=0,highlightthickness = 0, pady=5)
                timer_button.grid(row=1, column=0, sticky="new")

                settings_button=Button(sidebar, text="Settings", bg="indigo", font=("Segoe UI",16)
                , fg="white", bd=0, highlightthickness = 0, pady=5)
                settings_button.grid(row=2, column=0, sticky="new")

#---------End sidebar---------

