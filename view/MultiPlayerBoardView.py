
import tkinter as tk
import tkinter.font as tkFont
from tkinter import simpledialog, messagebox



from view.GameBoardView import  GameBoardMultiPlayer


class MPBoard(tk.Frame):
    def __init__(self,master,controller,mpController,previous):
        tk.Frame.__init__(self,master=master)
        self.previous=previous
        self.controllerIvy=mpController
        self.controller=controller
        self.initBottomFrame()
        self.initTitleFrame()
        self.createWidgets()

    def initGameBoard(self):
        game = self.controllerIvy.getGame()
        self.controller.controllerState.game = game
        self.gameBoard = GameBoardMultiPlayer(self, self.controller.controllerState)
        self.gameBoard.pack(side="left")
        self.gameBoard.disable()

    def enableBoard(self):
        self.gameBoard.enable()

    def initBottomFrame(self):
        self.bottomFrame = tk.Frame(self)
        self.bottomFrame.pack(side="bottom",expand="yes",fill="both",pady=50)

    def initTitleFrame(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(side="top")
        tk.Label(self.titleFrame, text="score x 1 - 0 y", font=tkFont.Font(size="20")).pack(side="bottom")
        tk.Label(self.titleFrame, text="MultiPlayer", font=tkFont.Font(size="32")).pack()


    def createWidgets(self):
        self.abondonner = tk.Button(self.bottomFrame, text="abondonner", fg="blue",  command=self.onGiveUp,width=20)
        self.abondonner.grid(column=0 ,row = 0 ,padx=120)
        self.trouver = tk.Button(self.bottomFrame, text="j'ai trouvé", fg="blue", command=self.onGotIt,width=20)
        self.trouver.grid(column=1,row = 0)

    def askHowMuch(self):
        box = simpledialog.askinteger(title="title", prompt="saisissez une valeur entre entière ", initialvalue=0,
                                      minvalue=0, parent=self.master)
        if box == None :
            messagebox.showerror("hello", "no entry")
        else:
            self.controller.controllerState.game.target=box
            self.controllerIvy.sendMsg("Server i can get {0}".format(box))

    def stopIvy(self):
        self.controllerIvy.stopIvy()



    def onGiveUp(self):
        pass
        # self.forget()
        # self.previous.pack(expand="yes")

    def onGotIt(self):
        pass
        # self.gameBoard.replay()
        # self.solutionBoard.onResetSolution()

    def arreterLaPartie(self):
        self.controllerIvy.arreterLaPartie()