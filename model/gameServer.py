import os

from ivy.std_api import *

from model.gameAgent import Agent, info


class Server(Agent):
    def __init__(self, manager, name="Server", nbPlayers=1, ip="127.0.0.1", port="9999",
                 readyMsg="still waiting for {0}", guessTime=45, startingIn=10):

        Agent.__init__(self, name, ip, port, "")

        self.nbPlayers = nbPlayers
        self.waitingFor = nbPlayers
        self.guessTime = guessTime
        self.startingIn = startingIn
        self.stop = False
        self.manager = manager
        self.answers = dict()
        print(name)
        IvyBindMsg(self.on_ICanGet, "{0} i can get ([0-9]*)".format(name))
        IvyBindMsg(self.OnJeQuitte,"{0} je quitte la partie".format(name))

    def OnJeQuitte(self,agent):
        IvySendMsg("the game is finished")
        self.manager.restart()
        # IvyStop()
        # os.kill(os.getpid(), signal.SIGINT)

    def on_ICanGet(self, agent, number):
        self.answers[agent.agent_name] = int(number)
        print("{0} has {1}".format(agent.agent_name, number))

        if len(self.answers) == self.nbPlayers:
            print(self.answers)
            self.manager.goNext()


    def on_connection_change(self, agent, event):
        if self.waitingFor > 0:
            if event == IvyApplicationDisconnected:
                info('Ivy application %r has disconnected', agent)
            else:
                info('Ivy application %r has connected', agent)
                info('Ivy applications currently on the bus: %s',
                     ','.join(IvyGetApplicationList()))
                self.waitingFor -= 1
                self.manager.run()
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




