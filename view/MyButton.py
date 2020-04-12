from tkinter import  Button
import tkinter as tk

class MyButton(tk.Button):

    def __init__(self,master,**options):
        tk.Button.__init__(self,master=master)
        self.config(options)
        self.used=False

    def use(self):
        self.used=True
        self.config(state="disabled")

    def unUse(self):
        self.used=False
        self.config(state="normal")

    def isUsed(self):
        return self.used
