from tokenize import String

from model.Card import Card
from model.CardsProvider import CardsProvider
from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
from model.operators.binaryOperators import *


class Game:
    MIN = 100 #constants
    MAX = 999

    def __init__(self):
        self.target = 0
        self.initOperators()
        self.init()

    def initCards(self):
        if hasattr(self,"cards") :
            self.cards.clear()
        else :
            self.cards=list()

        cards = CardsProvider().getRandomCards()
        for card in cards :
            self.cards.append(Card(card))
    def init(self):
        self.initCards()
        self.setRandomNumber()
        self.end=False
        self.currentOperation=None
        self.leftIndex=None
        self.score = 0
        self.playerName=""
        if hasattr(self,"history") :
            self.history.clear()  # list of vectors ( LeftOp , op , RighOp , value )
        else :
            self.history=list()



    def initOperators(self):
        self.operators = dict()
        self.operators[0]=Plus()
        self.operators[1]=Minus()
        self.operators[2]=Multi()
        self.operators[3]=Divide()

    def setRandomNumber(self):
        raise NotImplementedError("Not implemented at this level")

    def getCards(self):
        return self.cards

    def evaluate(self):
        if(type(self.currentOperation.op).isValid(self.currentOperation.left.evaluate(),self.currentOperation.right.evaluate())):
            result = self.currentOperation.evaluate()
            return result
        else:
            return "{0} {1} {2} n'est pas une opération valide".format(self.currentOperation.left,self.currentOperation.op,self.currentOperation.right)

    def onCard(self,indexCard):
        if not self.currentOperation:
            self.cards[indexCard].toggleUse()
            self.currentOperation=BinaryExpression(Constant(self.cards[indexCard].value),None,None)
            self.leftIndex= indexCard
            return 0
        else :#left exist
            self.currentOperation.right=Constant(self.cards[indexCard].value)
            result = self.evaluate()
            if type(result) == type(String) :
                self.cards[self.leftIndex].toggleUse()
            else :
                if result==self.target:
                    self.end=True
                    self.score+=1
                self.cards.append(Card(result))
                self.cards[indexCard].toggleUse()
            self.currentOperation=None
            self.leftIndex=None
            return -1

    def onOp(self, indexOp):
        self.currentOperation.op=self.operators[indexOp]

    def setName(self, name):
        if name != self.playerName :
            self.playerName=name
            self.score=0