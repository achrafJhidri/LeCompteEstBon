
from model.game.Card import Card
from model.game.Game import Game
from model.multiplayer.gameAgent import Agent, on_msg
from model.ivy.std_api import *
from model.training.TrainingGame import TrainingGame


class Client(Agent):
    def __init__(self,controller, name="Client", ip="127.0.0.1", port="9999", readyMsg=""):
        Agent.__init__(self, name, ip, port, readyMsg)
        self.name =name

        IvyBindMsg(self.onWaitForPlayer, "{0} Wait for another player".format(name))
        IvyBindMsg(self.onWaitForEnd, "{0} already two players".format(name))
        IvyBindMsg(self.setOpponent, "{0} your opponent is ([a-zA-Z0-9]*)".format(name))
        IvyBindMsg(self.onStarting, "{0} we're starting in ([0-9]*)".format(name))
        IvyBindMsg(self.on_howMuchCanYouGet, "{0} How Much can you get ?".format(name))
        IvyBindMsg(self.onGameFinished, "{0} the game is finished".format(name))
        IvyBindMsg(self.on_gettingCardAndTarget, "{0} Go (.*) =>>>>>  ([0-9]*), ([0-9]*)".format(name))
        IvyBindMsg(self.iLost, "{0} too late".format(name))
        IvyBindMsg(self.proovItToo, "{0} You have ([0-9]*) to proove it".format(name))
        IvyBindMsg(self.onProovIt, "{0} has ([0-9]*) to proove it".format(name))
        IvyBindMsg(self.onReady, "{0} ready".format(name))
        IvyBindMsg(self.weLost, "{0} you both lost".format(name))
        IvyBindMsg(self.iLostNothing, "{0} you lost".format(name))



        self.binds = list()
        self.controller=controller
        self.again = False


    def heLostNothing(self,agent):
        self.controller.heLost(nothing=True)

    def iLostNothing(self, agent):
        self.controller.heLost(nothing=True)

    def weLost(self):
        self.controller.weLost()

    def proovItToo(self, agent, decisionTime):
        self.onProovIt(agent, decisionTime, both=True)

    def onStarting(self, agent, sec):
        if self.again:
            self.controller.replayIn(sec)
        else:
            self.controller.startingIn(sec)


    def onGameFinished(self,agent):
        self.again = False
        for id_bind in self.binds:
            IvyUnBindMsg(id_bind)
        self.binds.clear()
        self.controller.goMenuPrincial()

    def onWaitForPlayer(self, agent):
        print("onWait")
        msg = "En attente d'un deuxième joueur"
        self.controller.onWait(msg)

    def onWaitForEnd(self, agent):
        msg = "Une partie est déjà en cours "
        self.controller.onWait(msg)



    def on_gettingCardAndTarget(self,agent,cardList : str,target, sec):
        if not hasattr(self, "game"):
            self.game=Game()
        self.game.cards.clear()
        cardList = cardList[1:len(cardList)-2]
        tab = cardList.split(",")
        for card in tab :
            self.game.cards.append(Card(card))
        self.game.target = int(target)
        self.controller.showMPBoard(sec)

    def onReady(self,agent):
        self.controller.initGameBoard()

    def getGame(self):
        return self.game

    def iAmBack(self):
        IvySendMsg("I am back")

    def onTimeOut(self,agent):
        self.controller.askHowMuch()

    def yesReplay(self):
        self.again = True
        IvySendMsg("I want to replay")

    def iLost(self, agent):
        self.controller.iLost()





    # def on_direct_msg(self, agent, num_id, msg):
    #     print("***** {0} *****".format(msg))

    def onProovIt(self, agent, decisionTime, both=False):
        self.controller.enableBoard(decisionTime, both)

    def on_connection_change(self, agent, event):
        print("connection change : event = {0}".format(event))
        pass

    def on_die(self, agent, _id):
        pass

    def on_howMuchCanYouGet(self, agent):
        self.controller.askHowMuch()

    def previentServeur(self):
        IvySendMsg("Server je quitte la partie")



    def setOpponent(self, agent, opponent):
        self.opponent = opponent

        self.binds.append(IvyBindMsg(self.heGotIt,"{0} has ([0-9]*) to proove it".format(self.opponent)))
        self.binds.append(IvyBindMsg(self.heFoundIt,"{0} found it".format(self.opponent)))
        self.binds.append(IvyBindMsg(self.heHas, "{0} has ([0-9]*)".format(self.opponent)))
        self.binds.append(IvyBindMsg(self.heLost, "{0} too late".format(self.opponent)))
        self.binds.append(IvyBindMsg(self.heLostNothing,"{0} you lost".format(self.opponent)))
        self.controller.setOpponent(opponent)

    def heHas(self, agent, number):
        self.controller.heHas(number)

    def heLost(self, agent):
        self.controller.heLost()

    def IGotIt(self):
        IvySendMsg("I got it")

    def heGotIt(self,agent, decisionTime):
        self.controller.heGotIt(decisionTime)

    def targetFound(self):
        IvySendMsg("I found it")

    def heFoundIt(self, agent):
        self.controller.heFoundIt()



