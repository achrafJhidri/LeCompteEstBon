import os
import time

from model.ivy.std_api import *

from model.multiplayer.gameAgent import Agent, info


class Server(Agent):
    players = list()

    def __init__(self, manager, name="Server", nbPlayers=1, ip="127.0.0.1", port="9999",
                 readyMsg="still waiting for {0}", guessTime=45, startingIn=10):

        Agent.__init__(self, name, ip, port, "")

        self.nbPlayers = nbPlayers
        self.waitingFor = nbPlayers
        self.guessTime = guessTime
        self.startingIn = startingIn
        self.manager = manager
        IvyBindMsg(self.on_ICanGet, "{0} i can get ([0-9]*)".format(name))
        IvyBindMsg(self.OnJeQuitte,"{0} je quitte la partie".format(name))
        IvyBindMsg(self.heGotIt,"I got it")
        IvyBindMsg(self.heFoundIt,"I found it")
        IvyBindMsg(self.wantToReplay,"I want to replay")
        IvyBindMsg(self.playerIsBack,"I am back")


        self.init()

    def OnJeQuitte(self,agent):
        Server.sendMsgToPlayers("the game is finished")
        Server.players.clear()
        self.manager.stop()
        self.manager.init()
        self.init()

    def on_ICanGet(self, agent, number):
        self.answers[agent.agent_name] = int(number)
        print("{0} has {1}".format(agent.agent_name, number))
        IvySendMsg("{0} has {1}".format(agent.agent_name, number))
        if len(self.answers) == self.nbPlayers:
            print(self.answers)
            self.manager.goNext()

    def heGotIt(self, agent):
        #print("{0} got it".format(agent.agent_name))
        #IvySendMsg("{0} got it".format(agent.agent_name))
        self.stop = True
        self.manager.winner = agent.agent_name
        self.manager.stopTimeout()

    def heFoundIt(self, agent):
        self.manager.stopDecisionTime(agent.agent_name)
        IvySendMsg("{0} found it".format(agent.agent_name))


    def wantToReplay(self, agent):
        self.nbReplay+=1
        if self.nbReplay == 2:
            self.init()
            self.manager.restart()

    def playerIsBack(self, agent):
        if self.addPlayerIfPossible(agent):
            self.init()
            #self.manager.restart()

    def init(self):
        self.nbReplay = 0
        self.stop =False
        if hasattr(self, "answers"):
            self.answers.clear()
        else:
            self.answers = dict()

    def addPlayerIfPossible(self, agent):
        nbPlayer = len(Server.players)
        if nbPlayer < 2:
            Server.players.append(agent.agent_name)
            #info('Ivy application %r has connected', agent)
            info('Ivy applications currently on the bus: %s',
                ','.join(IvyGetApplicationList()))
            if nbPlayer == 1:
                IvySendMsg("{0} your opponent is {1}".format(Server.players[0], Server.players[1]))
                IvySendMsg("{0} your opponent is {1}".format(Server.players[1], Server.players[0]))
                self.manager.run()
                return True
            else:
                IvySendMsg("{0} Wait for another player".format(agent.agent_name))

        else:
            IvySendMsg("{0} already two players".format(agent.agent_name))
        return False



    @staticmethod
    def sendMsgToPlayers(msg):
        for player in Server.players:
            IvySendMsg(player +" "+ msg)


    def on_connection_change(self, agent, event):
        self.addPlayerIfPossible(agent)

                # if self.manager.waitingForPlayers() :
                #     app=IvyGetApplication(agent.agent_name)
                #     IvySendDirectMsg(app,0,"stil waiting for {0} players".format(self.waitingFor+1))
                #     self.manager.reduceWaitingForPlayers();
                # else :
                #     self.sendStartingIn()

    def on_die(self, agent, _id):
        info('Received the order to die from %r with id = %d', agent, _id)
        global on_die_accepted
        on_die_accepted = True
        # will interrupt the raw_input()/input() in the main loop, below
        os.kill(os.getpid(), signal.SIGINT)

#
# if __name__ == "__main__":
#     import time
#     agent = Server()
#
#     while not agent.stop:
#         time.sleep(3)
#         print("stil awake")




