
import tkinter as tk

from view.MenuPrincipal import MenuPrincipal


class View(tk.Tk):
    def __init__(self,controller):
        tk.Tk.__init__(self)
        self.frame = MenuPrincipal(controller,self)


        self.geometry("500x500")

        self.controller=controller
