from controller.operControllers.LeftOperandController import LeftOperandController
from controller.operControllers.OperatorController import OperatorController
from controller.operControllers.RightOperandController import RightOperandController
from model.game.Game import Game
from model.training.TrainingGame import TrainingGame


class GameBoardController:
    def __init__(self,controller):
        self.game: Game = None
        self.controller=controller
        self.installControllers()



    def installControllers(self):

        self.rightOperand = RightOperandController(self,None,None)
        self.operator = OperatorController(self, self.rightOperand,None)
        self.leftOperand = LeftOperandController(self,self.operator,None)

        self.rightOperand.next = self.leftOperand
        self.rightOperand.previous = self.operator
        self.operator.previous = self.leftOperand

        self.currentController = self.leftOperand

    def deleteLine(self):
        leftIndex, rightIndex = self.currentController.deleteLine()
        return leftIndex, rightIndex


    def onClick(self, index):
        self.currentController.onClick(index)

    def unDo(self):
        self.currentController.unDo()

    def replay(self, game=None):
        if game is None:
            self.game.init()
        else:
            self.game = game
        self.currentController = self.leftOperand

    def getNumberCible(self):
        return int(self.game.target)

    def getOperators(self):
        return self.game.operators

    def getListNumbers(self):
        listNumbers = list()
        for card in self.game.getCards():
            listNumbers.append(card.value)
        return listNumbers

    def setView(self, view):
        self.view =view

    def resetSolution(self):
        self.game.resetSolution()

    def askForSolution(self):
        return self.game.getSolution()

    def goMenuPrincipal(self):
        self.controller.goMenuPrincipal()

