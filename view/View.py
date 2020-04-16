from view.Pseudo import Pseudo
import tkinter as tk


class View(tk.Tk):
    def __init__(self, controller):
        tk.Tk.__init__(self)
        self.frame = Pseudo(controller, self)

        screen_height = int(self.winfo_screenheight() * 1/2)
        screen_width = self.winfo_screenwidth()

        screen_width = int(screen_width *3/8)

        self.geometry("{0}x{1}".format(screen_width, screen_height))

        self.controller = controller


    def goMenuPrincipale(self):
        self.frame=Pseudo(controller=self.controller,master=self)