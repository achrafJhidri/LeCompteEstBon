import threading
import time

from model.ivy.std_api import  *

from controller.IvyControllers.state import State
from model.multiplayer.gameServer import Server


class Init(State):
    def __init__(self, next, manager, nbPlayers, countDownBeforeStart, timeOut):
        State.__init__(self, next, None, manager)
        self.nbPlayers = nbPlayers
        self.countDownBase = countDownBeforeStart
        self.waitingFor = nbPlayers
        self.timeOut = timeOut

    def init(self):
        self.countDown = self.countDownBase

    def run(self):
        #print("from server manager {0}".format(self.waitingFor))
        #if self.waitingFor > 0:
         #   self.waitingFor -= 1
          #  IvySendMsg("stil waiting for {0} players".format(self.waitingFor))

        #if self.waitingFor == 0:

        self.sendStartingIn()
        self.manager.goNext()

    def sendStartingIn(self):
        #names = self.manager.getPlayerNames()
        Server.sendMsgToPlayers("we're starting in {0}".format(self.countDown))
        while self.countDown > 0:
            self.countDown -= 1
            time.sleep(1)
        cards = self.manager.getCards()
        entiers = list()
        i = 0
        while i < len(cards):
            entiers.append(cards[i].value)
            i+=1
        target = self.manager.getTarget()
        Server.sendMsgToPlayers("Go {0}  =>>>>>  {1}, {2}".format(entiers, target, self.timeOut))
        Server.sendMsgToPlayers("ready")
        #IvySendMsg("Go {0}  =>>>>>  {1}, {2}".format(entiers, target, self.timeOut))
        #IvySendMsg("ready")

    def stop(self, val=0):
        self.countDown = val


class Started(State):
    def __init__(self, next, manager, timeOut):
        State.__init__(self, next, None, manager)
        self.timeOut = timeOut

    def init(self):
        self.countDown = self.timeOut

    def run(self):
        if self.countDown > 0 :
            self.countDown -= 1
            threading.Timer(1.0, self.run).start()
        elif self.countDown == -1:
            self.manager.goNext()
        elif self.countDown==0:
            Server.sendMsgToPlayers("How Much can you get ?")

    def stop(self, val=-1):
        self.countDown =val


class TimeOut(State):
    def __init__(self, next, manager, decisionTime):
        State.__init__(self, next, None, manager)
        self.decisionTime = decisionTime
        self.players = list()
    def init(self):
        self.players.clear()
        self.timer = self.decisionTime

    def run(self):

        if self.manager.getWinner() :
            self.players.append(self.manager.getWinner())
        else:
            self.players =  self.manager.pickTheNearest()

        if len(self.players) == 1:
            self.both =False
            IvySendMsg("{0} has {1} to proove it".format(self.players[0], self.decisionTime))
        else:
            self.both =True
            #IvySendMsg("You have {0} to proove it".format(self.decisionTime))
            Server.sendMsgToPlayers("You have {0} to proove it".format(self.decisionTime))
        self.countDown()


    def countDown(self):
        if self.timer > 0 and len(self.players) > 0:
            self.timer -= 1
            threading.Timer(1.0, self.countDown).start()
        elif self.timer == 0:
            if not self.both:
                IvySendMsg("{0} too late".format(self.players[0]))
            else:
                if len(self.players) == 2:
                    Server.sendMsgToPlayers("you both lost")
                else:
                    IvySendMsg("{0} you lost".format(self.players[0]))


    def stop(self, val=None, player=None):
        if val:
            self.timer = val
        if player:
            self.players.remove(player)


