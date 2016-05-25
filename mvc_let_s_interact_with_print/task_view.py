import Tkinter as tk

class TaskView:

    def __init__(self, master):
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        print "Moving on"

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(master, textvariable=self.__title_var)
        self.toggle_button = tk.Button(master, text="Reverse")
        self.toggle_button.pack(side='left')

    def update_title(self, title):
        if not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var.set(title)
        self.__title_label.pack(side='right')
