
from model.multiplayer.gameClient import Client
from view.runnable.AskHowMuch import AskHowMuch
from view.runnable.EnableBoard import EnableBoard
from view.runnable.HeFoundIt import HeFoundIt
from view.runnable.HeGotIt import HeGotIt
from view.runnable.HeHas import HeHas
from view.runnable.HeLost import HeLost
from view.runnable.ILost import ILost
from view.runnable.OnWait import OnWait
from view.runnable.ReplayIn import ReplayIn
from view.runnable.SetOpponent import SetOpponent
from view.runnable.StartingIn import StartingIn
from view.runnable.WaitingFor import WaitingFor
from view.runnable.WeLost import WeLost
from view.runnable.showMenuPrincipal import showMenuPrincipal
from view.runnable.showMultiPlayerBoard import showMultiPlayerBoard


class MPController(object):

    def __init__(self,view,name):
        self.view = view
        self.name = name

    def initClient(self):
        self.ivyClient = Client(name=self.name,controller=self)

    def arreterLaPartie(self):
        self.ivyClient.previentServeur()

        # self.ivyClient.stop()
    def getGame(self):
        return self.ivyClient.getGame()

    def iAmBack(self):
        self.ivyClient.iAmBack()

    def showOnWaitingFor(self,nbPlayer):
        waitingForObj = WaitingFor(vue=self.view)
        self.view.master.queue.put(waitingForObj)

    def goMenuPrincial(self):
        menuPrincipalViewObj = showMenuPrincipal(self.view)
        self.view.master.queue.put(menuPrincipalViewObj)

    def onWait(self, msg):
        onWait = OnWait(self.view, msg)
        self.view.master.queue.put(onWait)


    def showMPBoard(self, sec):
        multiPlayerBoardObj = showMultiPlayerBoard(self.view, sec)
        self.view.master.queue.put(multiPlayerBoardObj)

    def initGameBoard(self):
        self.view.initGameBoard()

    def askHowMuch(self):
        howMuch = AskHowMuch(self.view.mpboard)
        self.view.master.queue.put(howMuch)

    def sendMsg(self,msg):
        self.ivyClient.sendMsg(msg)

    def iLost(self, nothing=False):
        iLost = ILost(self.view.mpboard, nothing)
        self.view.master.queue.put(iLost)

    def enableBoard(self, decisionTime, both):
        enableBoard = EnableBoard(self.view.mpboard, decisionTime, both)
        self.view.master.queue.put(enableBoard)

    def startingIn(self, sec):
        startingIn = StartingIn(self.view, sec)
        self.view.master.queue.put(startingIn)

    def replayIn(self, sec):
        replayIn = ReplayIn(self.view.mpboard, sec)
        self.view.master.queue.put(replayIn)

    def setOpponent(self, opponent):
        setOpponent = SetOpponent(self.view.mpboard, opponent)
        self.view.master.queue.put(setOpponent)

    def heGotIt(self, decisionTime):
        heGotIt = HeGotIt(self.view.mpboard, decisionTime)
        self.view.master.queue.put(heGotIt)

    def heHas(self, number):
        heHas= HeHas(self.view.mpboard, number)
        self.view.master.queue.put(heHas)

    def heLost(self, nothing=False):
        heLost = HeLost(self.view.mpboard, nothing)
        self.view.master.queue.put(heLost)

    def weLost(self):
        weLost = WeLost(self.view.mpboard)
        self.view.master.queue.put(weLost)



    def IGotIt(self):
        self.ivyClient.IGotIt()

    def targetFound(self):
        self.ivyClient.targetFound()

    def heFoundIt(self):
        heFoundIt = HeFoundIt(self.view.mpboard)
        self.view.master.queue.put(heFoundIt)

    def yesReplay(self):
        self.ivyClient.yesReplay()



