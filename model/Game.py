from model.CardsProvider import CardsProvider
from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
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

        self.currentOperation : BinaryExpression =None


    def initOperators(self):
        self.operators = dict()
        self.operators["+"]=Plus()
        self.operators["-"]=Minus()
        self.operators["x"]=Multi()
        self.operators["/"]=Divide()

    def setRandomNumber(self):
        raise NotImplementedError("Not implemented at this level")

    def getCards(self):
        return self.cards

    def evaluate(self,left,op,right):
        if(type(self.operators[op]).isValid(left,right)):
            self.currentOperation=BinaryExpression(Constant(left),self.operators[op],Constant(right))
            result = self.currentOperation.evaluate()
            self.currentOperation=None
            return result
        else:
            return None