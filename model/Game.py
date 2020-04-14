from tokenize import String

from model.Card import Card
from model.CardsProvider import CardsProvider
from model.History import History
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
        #self.currentOperation=None
        #self.leftIndex=None
        self.score = 0
        self.playerName=""
        #self.history=History()

        if hasattr(self,"history") :
            self.history.init()  # list of vectors ( LeftOp , op , RighOp , value )
        else :
            self.history=History()



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

    def evaluate(self, indexRight):
        left=self.cards[self.history.getLeft()].value
        right=self.cards[indexRight].value
        if(type(self.history.currentOperation.op).isValid(left,right)):
            result = self.history.evaluateCurrentOp(left,right)
            return result
        else:
            return "{0} {1} {2} n'est pas une opération valide".format(left,self.history.getOp(),right)

    def onCard(self,indexCard):
        if  self.history.currentOperation is None:
            self.cards[indexCard].toggleUse()
            self.history.addOperande(indexCard)
            return 0
        else :#left exist
            result = self.evaluate(indexCard)

            #    self.cards[self.history.getLeft()].toggleUse()
            if type(result) != type(String):
                if result==self.target:
                    self.end=True
                    self.score+=1
                self.cards.append(Card(result))
                self.cards[indexCard].toggleUse()
                self.history.addOperande(indexCard)
            return result

    def onOp(self, indexOp):
        self.history.addOperator(self.operators[indexOp])
        return str(self.operators[indexOp])

    def setName(self, name):
        if name != self.playerName:
            self.playerName=name
            self.score=0

    def rollBack(self):
        self.cards.pop()
        lastCards = self.history.getLastCards()
        for card in lastCards:
            if(card is not None):
                self.cards[card].toggleUse()

    def getUnUsedCards(self):
        unUsedCards = list()
        i=0
        while i < len(self.cards):
            if not self.cards[i].isUsed():
                unUsedCards.append(i)
            i+=1

        return unUsedCards

    def operatorIsNext(self):
         return (self.history.getLeft() is not None and self.history.getOp() is None)

    def unDo(self):
        left = self.history.getLeft()
        op = self.history.getOp()
        if(left is not None and op is None):
            self.cards[left].toggleUse()
        self.history.erase()
