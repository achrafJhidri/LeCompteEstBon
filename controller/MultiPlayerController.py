
from model.gameClient import Client
from view.AskHowMuch import AskHowMuch
from view.EnableBoard import EnableBoard
from view.WaitingFor import WaitingFor
from view.showMenuPrincipal import showMenuPrincipal
from view.showMultiPlayerBoard import showMultiPlayerBoard


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

    def showOnWaitingFor(self,nbPlayer):
        waitingForObj = WaitingFor(vue=self.view)
        self.view.master.queue.put(waitingForObj)

    def goMenuPrincial(self):
        menuPrincipalViewObj = showMenuPrincipal(self.view.master)
        self.view.master.queue.put(menuPrincipalViewObj)

    def showMPBoard(self):
        multiPlayerBoardObj = showMultiPlayerBoard(self.view)
        self.view.master.queue.put(multiPlayerBoardObj)

    def initGameBoard(self):
        self.view.initGameBoard()

    def askHowMuch(self):
        howMuch = AskHowMuch(self.view.mpboard)
        self.view.master.queue.put(howMuch)
    def sendMsg(self,msg):
        self.ivyClient.sendMsg(msg)

    def enableBoard(self):
        enableBoard = EnableBoard(self.view.mpboard)
        self.view.master.queue.put(enableBoard)

