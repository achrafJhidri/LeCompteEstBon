import tkinter as tk

from controller.MultiPlayerController import MPController
from view.MultiPlayerBoardView import MPBoard


class MenuMultiJoueur(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)

        self.config()

        self.controller=controller
        self.previous=previous
        self.createWidgets()

        self.entrainementVue =None
        self.mpboard=None


    def createWidgets(self):
        self.back = tk.Button(self, text="go back", fg="blue", command=self.on_back)
        self.back.pack(side="bottom",expand="yes")

        self.createGame = tk.Button(self, text="créer une partie", fg="blue",  command=self.onCreateGame)
        self.createGame.pack(side="left",padx=10,pady=20,expand="yes")

        self.joinGame = tk.Button(self, text="rejoindre une partie", command=self.onJoinGame)
        self.joinGame.pack(side="left",padx=10,pady=20,expand="yes")



    def onCreateGame(self):
        self.onJoin()
        self.mpCtrl.showOnWaitingFor(1)



    def onJoinGame(self):
        self.onJoin()


    def onJoin(self):
        self.mpCtrl = MPController(self,self.controller.playerName)
        self.mpCtrl.initClient()
        if not self.mpboard:
            self.mpboard = MPBoard( master=self.master,controller=self.controller,mpController=self.mpCtrl, previous=self)
            self.mpboard.pack_forget()
            print("ici")

    def initGameBoard(self):
        self.mpboard.initGameBoard()


    # def stopIvy(self):
    #     self.mpCtrl.stopIvy()

    def on_back(self):
        self.pack_forget()
        self.previous.pack(expand="yes")


    def showMultiPlayerBoard(self):
        print("après")
        self.pack_forget()
        self.mpboard.pack(expand="yes")


