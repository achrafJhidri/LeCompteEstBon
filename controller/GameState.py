from controller.operControllers.LeftOperandController import LeftOperandController
from controller.operControllers.OperatorController import OperatorController
from controller.operControllers.RightOperandController import RightOperandController
from model.Game import Game
from model.NewGame import NewGame
from model.TrainingGame import TrainingGame
from view.View import View


class GameState:
    def __init__(self):
        self.game: NewGame =None
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

    def replay(self):
        self.game.init()
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