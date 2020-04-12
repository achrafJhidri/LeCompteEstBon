import tkinter as tk
import tkinter.font as tkFont

class GameBoard(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller=controller
        self.cibleFrame = tk.Frame(self,bd=1,relief=tk.SUNKEN)
        self.cible = tk.Label(self.cibleFrame,bd=1,relief=tk.SUNKEN, width= 5, font= tkFont.Font(size=62), text=self.controller.getNumberCible())
        self.cible.pack()
        self.cibleFrame.grid(row=0)
        self.listNumbersFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.listNumbersFrame.grid(row=1)
        self.createWidgets()


    def createWidgets(self):
        numbers = self.controller.getListNumbers()
        i = 0
        while i<len(numbers):
            button = tk.Button(self.listNumbersFrame, text=numbers[i], width=4, height=2, font= tkFont.Font(size=30),  fg="blue")
            button.grid(row=0, column=i, padx=4, pady=4,)
            i+=1
