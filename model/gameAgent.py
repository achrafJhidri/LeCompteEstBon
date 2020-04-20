from ivy.std_api import *
import os


class Agent:
    def __init__(self, name, ip, port, readyMsg=""):
        # initialising the bus
        IvyInit(name,  # application name for Ivy
                readyMsg,  # ready message
                0,  # parameter ignored
                self.on_connection_change,  # handler called on connection/disconnection
                self.on_die)  # handler called when a die msg is received

        ivybus = "{0}:{1}".format(ip, port)
        # starting the bus
        IvyStart(ivybus)

        IvyBindDirectMsg(self.on_direct_msg)


    def on_direct_msg(self, agent, num_id, msg):
        print("i received a direct msg from {0} \n the msg is {1} \n the id is {2}".format(agent, msg, num_id))
        app = IvyGetApplication(agent.agent_name)
        IvySendDirectMsg(app, 0, "ack")

    def sendMsg(self, msg):
        IvySendMsg(msg)


    def sendDirectMsg(self, agent, msg, id=0):
        app = IvyGetApplication(agent.agent_name)
        IvySendDirectMsg(app, id, msg)

    def on_die(self, agent, _id):
        raise NotImplementedError("not implemented at this level")

    def on_connection_change(self, agent, event):
        raise NotImplementedError("not implemented at this level")


def info(fmt, *arg):
    print(fmt % arg)


def on_die(agent, _id):
    info('Received the order to die from %r with id = %d', agent, _id)
    global on_die_accepted
    on_die_accepted = True
    # will interrupt the raw_input()/input() in the main loop, below
    os.kill(os.getpid(), signal.SIGINT)


def ack(agent, num_id, msg):
    info("ack")


def on_msg(agent, msg):
    print(msg)


def on_stop(agent):
    os.kill(os.getpid(), signal.SIGINT)