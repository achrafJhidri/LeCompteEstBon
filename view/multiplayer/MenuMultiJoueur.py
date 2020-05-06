import tkinter as tk

from controller.MultiPlayerController import MPController
from view.CountDownMsgBox import CountDownMsgBox
from view.multiplayer.MultiPlayerBoardView import MPBoard


class MenuMultiJoueur(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)

        self.config()

        self.controller=controller
        self.previous=previous
        self.createWidgets()

        #self.entrainementVue =None
        self.mpboard=None


    def createWidgets(self):
        self.back = tk.Button(self, text="Retour", fg="blue", command=self.on_back)
        self.back.pack(side="left",expand="yes")

        self.joinGame = tk.Button(self, text="Rejoindre une partie", command=self.onJoinGame)
        self.joinGame.pack(side="left",padx=10,pady=20,expand="yes")

        self.infoLabel = tk.Label(self, text="")
        self.infoLabel.pack(fill="both", expand="yes")



    def onJoinGame(self):
        self.onJoin()
        self.joinGame.config(state="disable")



    def onJoin(self):
        if not hasattr(self, "mpCtrl"):
            self.mpCtrl = MPController(self,self.controller.playerName)
            self.mpCtrl.initClient()

        else:
           self.mpCtrl.iAmBack()

        if not self.mpboard:
            self.mpboard = MPBoard( master=self.master,controller=self.controller,mpController=self.mpCtrl, previous=self.previous)
            self.mpboard.pack_forget()


    def initGameBoard(self):
        self.mpboard.initGameBoard()



    def on_back(self):
        if self.mpboard:
            self.mpboard.pack_forget()
        self.pack_forget()
        self.joinGame.config(state="normal")
        self.infoLabel.config(text="")
        self.previous.pack(expand="yes")

    def onWait(self, msg):
        self.infoLabel.config(text=msg)


    def showMultiPlayerBoard(self, sec):
        self.pack_forget()
        self.mpboard.start(sec)
        self.joinGame.config(state="normal")
        self.back.config(state="normal")



    def startingIn(self, sec):
        self.infoLabel.config(text="")
        self.countdown(int(sec))
        self.back.config(state="disable")
        #CountDownMsgBox(self.master, "La partie commence dans ")

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.infoLabel.configure(text="")
        else:
            self.infoLabel.configure(text="Début de la partie dans %d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
