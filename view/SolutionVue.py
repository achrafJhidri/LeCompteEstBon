

import tkinter as tk
import tkinter.font as tkFont

from view.MyButton import MyButton


class Solution(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller=controller
        self.actuelDepth=1
        self.solutionIteration = list()
        self.createWidgets()

    def createWidgets(self):
        self.cibleLabel = tk.Label(self, bd=1, width=40, font=tkFont.Font(size=10),
                                   text="Solution",justify="center")
        self.cibleLabel.grid(row=0,column=0,columnspan=2)

        self.askForSolution = MyButton(self, text="solve", width=13, font=tkFont.Font(size=10), fg="blue", command=self.onSolve)
        self.askForSolution.grid(row=6,column=0)

        self.resetSolution = MyButton(self, text="resetSolution", width=13, font=tkFont.Font(size=10),fg="blue", command=self.onResetSolution)
        self.resetSolution.grid(row=6, column=1)

    def onSolve(self):
        result = self.controller.askForSolution()
        if result :
            label = tk.Label(self, bd=1, width=40, font=tkFont.Font(size=10),
                                          text=result, justify="center")
            label.grid(row=self.actuelDepth, column=0,columnspan=2)
            self.solutionIteration.append(label)
            self.actuelDepth+=1
    def onResetSolution(self):
        self.controller.resetSolution()
        while len(self.solutionIteration) > 0 :
            self.solutionIteration.pop().destroy()
        self.actuelDepth =1

