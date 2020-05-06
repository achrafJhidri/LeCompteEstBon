import threading
import tkinter as tk
import tkinter.font as tkFont
from tkinter import simpledialog, messagebox

from view.gameBoard.GameBoardView import  GameBoardMultiPlayer


class MPBoard(tk.Frame):
    def __init__(self,master,controller,mpController,previous):
        tk.Frame.__init__(self,master=master)
        self.previous=previous
        self.controllerIvy=mpController
        self.controller=controller
        self.initBottomFrame()
        self.initTitleFrame()
        self.createWidgets()
        self.init()
        self.after_id = None


    def init(self):
        self.stop = False
        self.opTarget = ""
        self.gotIt = False
        self.both = False

    def initGameBoard(self):
        game = self.controllerIvy.getGame()

        if hasattr(self, "gameBoard"):
            self.gameBoard.replay(game)
        else:
            self.controller.controllerState.game = game
            self.gameBoard = GameBoardMultiPlayer(self, self.controller.controllerState)
            self.gameBoard.pack(fill="x")
        self.gameBoard.disable()
        self.trouver.config(state="normal")
        self.stop =False

    def enableBoard(self, decisionTime, both):
        self.both = both
        self.gameBoard.enable()
        self.trouver.config(state="disable")
        self.callCountDown(msg=self.getMessage(),
                               remaining=int(decisionTime))

        self.callCountDown(msg=self.getMessage(),
                           remaining=int(decisionTime))
        self.gameBoard.setTarget(self.controller.controllerState.game.target)

    def initBottomFrame(self):
        self.bottomFrame = tk.Frame(self)
        self.bottomFrame.pack(side="bottom",expand="yes",fill="both",pady=50)

    def initTitleFrame(self):
        self.titleFrame = tk.Frame(self)
        self.titleFrame.pack(side="top")
        #tk.Label(self.titleFrame, textvariable=self.scoreString, font=tkFont.Font(size="20")).pack(side="bottom")
        self.initScoreFrame()
        tk.Label(self.titleFrame, text="MultiPlayer", font=tkFont.Font(size="32")).pack()


    def initScoreFrame(self):
        self.scoreFrame = tk.Frame(self.titleFrame)
        self.meLabel = tk.Label(self.scoreFrame, text="Moi", font=tkFont.Font(size="20"))
        self.meLabel.grid(row=0,column=0)

        self.myScore = tk.IntVar()
        self.myScoreLabel = tk.Label(self.scoreFrame, textvariable=self.myScore, font=tkFont.Font(size="20"))
        self.myScoreLabel.grid(row=0, column=1)

        self.versusLabel = tk.Label(self.scoreFrame, text="-", font=tkFont.Font(size="20"))
        self.versusLabel.grid(row=0, column=2)

        self.opScore = tk.IntVar()
        self.opScoreLabel = tk.Label(self.scoreFrame, textvariable=self.opScore, font=tkFont.Font(size="20"))
        self.opScoreLabel.grid(row=0, column=3)

        self.opName= tk.StringVar()
        self.opNameLabel = tk.Label(self.scoreFrame, textvariable=self.opName, font=tkFont.Font(size="20"))
        self.opNameLabel.grid(row=0, column=4)
        self.scoreFrame.pack(side="bottom")


    def createWidgets(self):
        self.infoLabel = tk.Label(self.bottomFrame, font=tkFont.Font(size="14"))
        self.infoLabel.grid(row=0, column=0, columnspan=2)
        self.abondonner = tk.Button(self.bottomFrame, text="Quitter la partie", fg="blue",  command=self.onGiveUp,width=20)
        self.abondonner.grid(column=0 ,row = 1 ,padx=120)
        self.trouver = tk.Button(self.bottomFrame, text="J'ai trouvé", fg="blue", command=self.onGotIt,width=20)
        self.trouver.grid(column=1,row = 1)

    def askHowMuch(self):
        self.setInfo("Combien peux-tu trouver ?")
        box = simpledialog.askinteger(title="Combien peux-tu trouvé", prompt="Saisissez une valeur entière ", initialvalue=0,
                                      minvalue=0, parent=self.master)
        if box == None :
            messagebox.showerror("Saisie non valide", "Veuillez saisir une valeur entière")
        else:
            threading.Timer(0.1, self.checkOpTarget).start()
            self.controller.controllerState.game.target=box
            self.controllerIvy.sendMsg("Server i can get {0}".format(box))


    def checkOpTarget(self):
        if self.opTarget == "":
            self.setInfo("En attente de la réponse de {0}".format(self.opName.get()))

    def stopIvy(self):
        self.controllerIvy.stopIvy()

    def heHas(self, number):
        self.opTarget = number
        #self.setInfo(self.opName.get() + " pense pouvoir trouver {0}.".format(number))

    def onGiveUp(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        self.controllerIvy.arreterLaPartie()
        # self.forget()
        # self.previous.pack(expand="yes")

    def onGotIt(self):
        self.stop = True
        self.gotIt =True
        self.setInfo("")
        self.controllerIvy.IGotIt()

        # self.gameBoard.replay()
        # self.solutionBoard.onResetSolution()

    def start(self, sec):
        self.init()
        self.pack(expand="yes")
        self.callCountDown(msg="Il vous reste", remaining=int(sec))


    def countdown(self, msg="", remaining = None):

        if remaining is not None:
            self.remaining = remaining
        print("countdown {0}".format(self.remaining))
        if self.remaining <= 0 and self.stop == False:
            pass
        elif self.stop == False :
            self.setInfo(msg + " {0} secondes ".format(self.remaining))
            self.remaining = self.remaining - 1
            self.after_id = self.after(1000, self.countdown, msg)

    def setOpponent(self, opponent):
        self.opName.set(opponent)
        self.myScore.set(0)
        self.opScore.set(0)




    def heGotIt(self, decisionTime):
         self.trouver.config(state="disable")
         self.callCountDown(msg=self.opName.get() + " pense pouvoir trouver {0}. \n Il lui reste ".format(self.opTarget), remaining=int(decisionTime))


    def targetFound(self):
        self.gameBoard.disable()
        self.myScore.set(self.myScore.get() + 1)
        self.controllerIvy.targetFound()
        if self.both:
            self.callCountDown(msg="Bravo ! +1 pour toi. En attente du résultat de {0} \n Il lui reste ".
                             format(self.opName.get()), remaining=self.remaining)
            self.both = False
        else:
            self.stop = True
            self.setInfo("Bravo ! Vous avez trouvé !")
            self.askForReplay()





    def heFoundIt(self):
        self.opScore.set(self.opScore.get()+1)
        if self.both:
            self.callCountDown(msg="{0} a trouvé !  \n Il te reste ".
                               format(self.opName.get()), remaining=self.remaining)
            self.both =False
        else:
            self.stop = True
            self.setInfo("{0} a trouvé :/".format(self.opName.get()))
            self.askForReplay()


    def askForReplay(self):
        answer = messagebox.askyesno("Rejouer", "Voulez-vous rejouer ?", )

        if answer:
            self.controllerIvy.yesReplay()
            self.setInfo("En attente de la réponse de "+self.opName.get())
            self.gameBoard.disable()
            self.both = False
        else:
            self.controllerIvy.arreterLaPartie()

    def replayIn(self, sec):
        self.callCountDown(msg="C'est reparti dans", remaining=int(sec))


    def setInfo(self, msg):
        self.infoLabel.config(text=msg)

    def heLost(self, nothing):
        self.stop =True
        if nothing:
            self.setInfo("{0} n'a pas trouvé, tu remportes cette partie.".format(self.opName.get()))
        else:
            self.setInfo("{0} n'a pas trouvé. Tu gagnes un point".format(self.opName.get()))
            self.myScore.set(self.myScore.get()+1)
        self.askForReplay()

    def iLost(self, nothing):
        self.stop = True

        if nothing:
            self.setInfo("{0} a trouvé il remporte cette partie.".format(self.opName.get()))
        else:
            self.setInfo("Tu n'as pas trouvé. {0} gagne un point".format(self.opName.get()))
            self.opScore.set(self.opScore.get()+1)
        self.gameBoard.disable()
        self.askForReplay()

    def weLost(self):
        self.stop = True
        self.setInfo("Personne n'a réussi a trouvé pas de point...".format(self.opName.get()))
        self.gameBoard.disable()
        self.askForReplay()


    def callCountDown(self, msg="",remaining=10):
        self.stop = False
        print(self.after_id)
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        self.countdown(msg=msg, remaining=int(remaining))

    def getMessage(self):
        print(self.gotIt)
        if self.gotIt:
            return " A toi de jouer, il te reste "
        else:
            return "{0} pense avoir trouvé {1} \n A toi de jouer, il te reste ".format(self.opName.get(),self.opTarget)

    def endOfGame(self):
        if self.after_id is not None:
            self.after_cancel(self.after_id)
        if self.myScore.get() > self.opScore.get():
            msg=" Vous avez gagné "
        elif self.myScore.get() == self.opScore.get():
            msg=" Match Nul, pas de gagnant"
        else:
            msg=" Vous avez perdu "

        self.setInfo("Fin de la partie."+msg)







