from model.CardsProvider import CardsProvider
from model.operators.binaryOperators import *


class Game:
    MIN = 100 #constants
    MAX = 999

    def __init__(self):
        self.target = 0
        self.cards = CardsProvider().getRandomCards()
        self.initOperators()
        self.setRandomNumber()
        self.history = list()  # list of vectors ( LeftOp , op , RighOp )


    def initOperators(self):
        self.operators = list()
        self.operators.append(Plus())
        self.operators.append(Minus())
        self.operators.append(Multi())
        self.operators.append(Divide())

    def setRandomNumber(self):
        raise NotImplementedError("Not implemented at this level")

    def getCards(self):
        return self.cards