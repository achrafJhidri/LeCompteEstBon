
import tkinter as tk
import tkinter.font as tkFont
from view.gameBoard.GameBoardView import GameBoard
from view.training.SolutionVue import Solution



class EntrainementVue(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
        self.previous=previous
        self.controller=controller
        self.initBottomFrame()
        self.initTitleFrame()
        self.createWidgets()

        self.gameBoard = GameBoard(self, self.controller.controllerState)
        self.gameBoard.pack(side="left")

        self.solutionBoard = Solution(master=self,controller=self.controller.controllerState)
        self.solutionBoard.pack(side="left")


    def initBottomFrame(self):
        self.bottomFrame = tk.Frame(self)
        self.bottomFrame.pack(side="bottom",expand="yes",fill="both",pady=50)

    def initTitleFrame(self):
        self.title = tk.Frame(self)
        self.title.pack(side="top")
        tk.Label(self.title, text="ENTRAINEMENT", font=tkFont.Font(size="32")).pack()

    def createWidgets(self):
        self.back = tk.Button(self.bottomFrame, text="Retour", fg="blue",  command=self.on_back,width=20)
        self.back.grid(column=0 ,row = 0 ,padx=120)
        self.replay = tk.Button(self.bottomFrame, text="Rejouer", fg="blue", command=self.on_replay,width=20)
        self.replay.grid(column=1,row = 0)

    def onResetSolution(self):
        self.solutionBoard.onResetSolution()
    def on_back(self):
        self.forget()
        self.previous.pack(expand="yes")

    def on_replay(self):
        self.gameBoard.replay()
        self.solutionBoard.onResetSolution()
