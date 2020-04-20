import time

from ivy.std_api import  IvySendMsg

from controller.IvyControllers.state import State


class Init(State):
    def __init__(self, next, manager, nbPlayers, countDownBeforeStart):
        State.__init__(self, next, None, manager)
        self.nbPlayers = nbPlayers
        self.countDownBeforeStart = countDownBeforeStart
        self.waitingFor = nbPlayers

    def run(self):

        if self.waitingFor > 0:
            self.waitingFor -= 1
            IvySendMsg("stil waiting for {0} players".format(self.waitingFor))

        if self.waitingFor == 0:

            self.sendStartingIn()
            self.manager.goNext()

    def sendStartingIn(self):
        while self.countDownBeforeStart > 0:
            IvySendMsg("we're starting in {0}".format(self.countDownBeforeStart))
            self.countDownBeforeStart -= 1
            time.sleep(1)
        cards = self.manager.getCards()
        entiers = list()
        i = 0
        while i < len(cards):
            entiers.append(cards[i].value)
            i+=1
        target = self.manager.getTarget()
        IvySendMsg("Go {0}  =>>>>>  {1}".format(entiers, target))
        IvySendMsg("ready")


class Started(State):
    def __init__(self, next, manager, timeOut):
        State.__init__(self, next, None, manager)
        self.timeOut = timeOut

    def run(self):
        while self.timeOut > 0:
            IvySendMsg("stop in {0}".format(self.timeOut))
            self.timeOut -= 1
            time.sleep(1)
        IvySendMsg("finish !")
        IvySendMsg("How Much can you get ?")
        # self.manager.goNext()


class TimeOut(State):
    def __init__(self, next, manager):
        State.__init__(self, next, None, manager)

    def run(self):

        theNearestPlayer  = self.manager.pickTheNearest()
        playerName= theNearestPlayer[0]
        value = theNearestPlayer[1]
        print("the nearest is {0} = {1}".format(playerName,value))

        IvySendMsg("{0} proov it !".format(playerName))



        # self.manager.goNext()
