
import tkinter as tk
import tkinter.font as tkFont

from view.GameBoardVue import GameBoard
from view.SolutionVue import Solution


class EntrainementVue(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
        self.previous=previous
        self.controller=controller
        self.title = tk.Frame(self,bd=1)
        self.title.grid(row=0,column=0,columnspan=2)
        tk.Label(self.title, text="ENTRAINEMENT", font=tkFont.Font(size="32")).pack()
        self.bottomFrame = tk.Frame(self, bd=1)
        self.bottomFrame.grid(row=2,column=0,columnspan=2)
        self.createWidgets()
        self.gameBoard = GameBoard(self, self.controller)
        self.gameBoard.grid(row=1,column=0)

        self.solutionBoard = Solution(master=self,controller=self.controller)
        self.solutionBoard.grid(row=1,column=1,padx=100,pady=100)


    def createWidgets(self):
        self.back = tk.Button(self.bottomFrame, text="BACK", fg="blue",  command=self.on_back,width=20)
        self.back.grid(column=0 ,row = 0 )
        self.replay = tk.Button(self.bottomFrame, text="REPLAY", fg="blue", command=self.on_replay,width=20)
        self.replay.grid(column=1,row = 0)

    def onResetSolution(self):
        self.solutionBoard.onResetSolution()



    def on_back(self):
        self.forget()
        self.previous.pack(expand="yes")
    def on_click(self):
        print(self.back)

    def on_replay(self):
        self.gameBoard.replay()
        self.solutionBoard.onResetSolution()



# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()