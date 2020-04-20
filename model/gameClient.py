from ivy.std_api import *

from model.Card import Card
from model.Game import Game
from model.gameAgent import Agent, on_msg


class Client(Agent):
    def __init__(self,controller, name="Client", ip="127.0.0.1", port="9999", readyMsg=""):
        Agent.__init__(self, name, ip, port, readyMsg)

        IvyBindMsg(self.on_howMuchCanYouGet, "(How Much can you get ?)")
        # IvyBindMsg(on_msg, "(stil waiting for [0-9]* players)")
        IvyBindMsg(on_msg, "(we're starting in [0-9]*)")#onStartIn , cree l'objet runnable
        IvyBindMsg(self.onGameFinished, "the game is finished")

        IvyBindMsg(self.on_gettingCardAndTarget, "Go (.*) =>>>>>  ([0-9]*)")
        IvyBindMsg(on_msg, "(stop in [0-9]*)")
        IvyBindMsg(self.onProovIt,"{0} proov it !".format(name))
        # IvyBindMsg(self.onTimeOut, "finish !")
        IvyBindMsg(self.onReady,"ready")
        self.controller=controller

    def onGameFinished(self,agent):
        IvyStop()
        self.controller.goMenuPrincial()

    def on_gettingCardAndTarget(self,agent,cardList : str,target):
        self.game=Game()
        self.game.cards.clear()
        cardList = cardList[1:len(cardList)-2]
        tab = cardList.split(",")
        for card in tab :
            self.game.cards.append(Card(card))
        self.game.target = int(target)
        self.controller.showMPBoard()

    def onReady(self,agent):
        self.controller.initGameBoard()

    def getGame(self):
        return self.game

    def onTimeOut(self,agent):
        self.controller.askHowMuch()




    # def on_direct_msg(self, agent, num_id, msg):
    #     print("***** {0} *****".format(msg))

    def onProovIt(self, agent):
        self.controller.enableBoard()

    def on_connection_change(self, agent, event):
        pass

    def on_die(self, agent, _id):
        pass

    def on_howMuchCanYouGet(self, agent,msg):
        self.controller.askHowMuch()


    def stop(self):
        IvyStop()
        print('isstopped')

    def previentServeur(self):
        print('jai prévenu le serveur')
        IvySendMsg("Server je quitte la partie")