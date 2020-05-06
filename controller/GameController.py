from controller.GameBoardController import GameBoardController
from model.training.TrainingGame import TrainingGame
from view.View import View


class GameController:
    def __init__(self):
        self.controllerState = GameBoardController(self)
        self.view = View(self)


    def run(self):
        self.view.mainloop()

    def setVue(self, view):
        self.view.frame = view

    def initTrainingGame(self):
        self.controllerState.game = TrainingGame()
        self.controllerState.game.setName(self.playerName)


    def saveName(self,name):
        self.playerName=name

    def goMenuPrincipal(self):
        self.view.goMenuPrincipale()

