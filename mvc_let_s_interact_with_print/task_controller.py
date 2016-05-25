import Tkinter as tk
from task_model import TaskModel
from task_view import TaskView

class TaskController:

    def __init__(self, master, model):
        if not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        if not isinstance(model, TaskModel):
            raise Exception("model is not a TaskModel")

        self.__model = model
        self.__view = TaskView(master)
        self.__view.update_title(self.__model.get_title())
        self.__model.set_callback_title(self.__view.update_title)
        self.__view.toggle_button.config(command=self.__model.toggle)
