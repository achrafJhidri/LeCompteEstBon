from controller.GameState import GameState
from controller.operControllers.LeftOperandController import LeftOperandController
from controller.operControllers.OperatorController import OperatorController
from controller.operControllers.RightOperandController import RightOperandController
from model.Game import Game
from model.NewGame import NewGame
from model.TrainingGame import TrainingGame
from view.View import View


class NewController:
    def __init__(self):
        self.controllerState = GameState()
        self.view = View(self)


    def run(self):
        self.view.mainloop()

    def setVue(self, view):
        self.view.frame = view

    def initTrainingGame(self):
        if self.controllerState.game :
            self.controllerState.game.init()
        else :
            self.controllerState.game = TrainingGame()
            self.controllerState.game.setName(self.playerName)


    def saveName(self,name):
        self.playerName=name



