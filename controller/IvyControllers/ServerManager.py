from assets.Constantes import Config
from controller.IvyControllers.ServerStates import Init, Started, TimeOut
from model.training.TrainingGame import TrainingGame
from model.multiplayer.gameServer import Server


class ServerManager:

    def __init__(self,game=None, nbPlayers=1, timeOut=45, countDownBeforeStart=10, decisionTime=20):
        self.game = game
        self.server: Server = Server(self, nbPlayers=nbPlayers)
        self.nbPlayer=nbPlayers
        self.timeOut=timeOut
        self.countDBS=countDownBeforeStart
        self.initAllStates(nbPlayers, timeOut, countDownBeforeStart, decisionTime)
        self.winner = None


    def setGame(self,game):
        self.game=game

    def initAllStates(self, nbPlayers, timeOut, countDownBeforeStart, decisionTime):
        self.initState: Init = Init(None, self, nbPlayers, countDownBeforeStart, timeOut)
        start = Started(None, self, timeOut)
        timeOutState = TimeOut(None, self,decisionTime)
        start.next = timeOutState
        self.initState.next = start
        timeOutState.next = self.initState
        self.current = self.initState

    def goNext(self):
        self.current = self.current.next
        self.run()

    def getCards(self):
        return self.game.cards

    def getTarget(self):
        return self.game.target

    def run(self):
        self.current.init()
        self.current.run()

    def init(self):
        self.game.init()
        self.current=self.initState
        self.winner = None


    def restart(self):
        #self.game.init()
        #self.winner = None
        #self.goNext()
        self.init()
        self.run()

    def pickTheNearest(self):
        theNearest =  list()

        distance = Config().MAX * 2
        for key in self.server.answers.keys():
            newdist = abs(self.getTarget() - self.server.answers[key])
            if distance == Config().MAX * 2:
                distance = newdist
                theNearest.append(key)
            elif newdist < distance:
                theNearest.pop()
                theNearest.append(key)
            elif newdist == distance:
                theNearest.append(key)

        return theNearest


    def stopTimeout(self):
        self.current.stop()

    def stopDecisionTime(self, player):
        self.current.stop(player=player)

    def getWinner(self):
        return self.winner

    def stop(self):
        self.current.stop(val=-2)

game = TrainingGame()
manager = ServerManager(game, nbPlayers=2, timeOut=10, countDownBeforeStart=5, decisionTime=15)
