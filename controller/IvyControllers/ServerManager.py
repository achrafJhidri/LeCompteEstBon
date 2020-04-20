from assets.Constantes import Config
from controller.IvyControllers.ServerStates import Init, Started, TimeOut
from model.TrainingGame import TrainingGame
from model.gameServer import Server


class ServerManager:

    def __init__(self,game=None, nbPlayers=1, timeOut=45, countDownBeforeStart=10):
        self.game = game
        self.server: Server = Server(self, nbPlayers=nbPlayers)
        self.nbPlayer=nbPlayers
        self.timeOut=timeOut
        self.countDBS=countDownBeforeStart
        self.initAllStates(nbPlayers, timeOut, countDownBeforeStart)

    def setGame(self,game):
        self.game=game

    def initAllStates(self, nbPlayers, timeOut, countDownBeforeStart):
        init: Init = Init(None, self, nbPlayers, countDownBeforeStart)
        start = Started(None, self, timeOut)
        timeOutState = TimeOut(None, self)
        start.next = timeOutState
        init.next = start
        self.current = init

    def goNext(self):
        self.current = self.current.next
        self.current.run()

    def getCards(self):
        return self.game.cards

    def getTarget(self):
        return self.game.target

    def run(self):
        self.current.run()
    def restart(self):
        self.initAllStates(self.nbPlayer,self.timeOut,self.countDBS)

    def pickTheNearest(self):
        theNearest =  None

        distance = Config().MAX * 2
        for key in self.server.answers.keys():
            print("{0} = {1}".format( key,self.server.answers[key]))
            newdist = abs(self.getTarget() - self.server.answers[key])
            if newdist < distance:
                distance = newdist
                theNearest = [key, self.server.answers[key]]

        return theNearest


game = TrainingGame()
manager = ServerManager(game, nbPlayers=2, timeOut=2, countDownBeforeStart=5)
