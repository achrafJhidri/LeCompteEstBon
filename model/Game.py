from random import randrange

from assets.Constantes import Config
from model.Card import Card
from model.CardsProvider import CardsProvider
from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
from model.operators.binaryOperators import Plus, Minus, Multi, Divide


class Game:
    def __init__(self):
        self.target = 0
        self.initOperators()
        self.history = list()
        self.init()

    def initCards(self):
        if hasattr(self, "cards"):
            self.cards.clear()
        else:
            self.cards = list()

        cards = CardsProvider().getRandomCards()
        for card in cards:
            self.cards.append(Card(card))

    def init(self):
        self.initCards()
        self.setRandomNumber()
        self.end = False
        self.score = 0
        self.playerName = ""
        if hasattr(self,"history"):
            self.history.clear()
        else:
            self.history = list()
        self.left = None
        self.right =None
        self.op = None
    def initOperators(self):
        self.operators = dict()
        self.operators[0] = Plus()
        self.operators[1] = Minus()
        self.operators[2] = Multi()
        self.operators[3] = Divide()

    def setRandomNumber(self):
        self.target=randrange(Config().MIN,Config().MAX+1)

    def getCards(self):
        return self.cards

    def setName(self, name):
        if name != self.playerName:
            self.playerName=name
            self.score=0


    #valueAndRow = self.getGame().setLeftOperand(index)
    def setLeftOperand(self, index):
        card = self.cards[index]
        card.toggleUse()
        value = card.value
        row = len(self.history)
        self.left = index
        return (value, row)


    #currentOp:BinaryExpression = self.getGame().getCurrentOperation(index)
    def getCurrentOperation(self, indexRight):
        self.right = indexRight
        left = self.cards[self.left].value
        right = self.cards[indexRight].value
        op = self.op

        return BinaryExpression(Constant(left),op,Constant(right))

    #self.getGame().setRightOperand(index,result)
    def addOperation(self,result):
        row = len(self.history)
        self.cards[self.right].toggleUse()
        self.cards.append(Card(result))
        self.history.append((self.left, self.right))
        return row

    #operatorAndRow = self.getGame().setOperator(index)
    def setOperator(self, indexOp):
        self.op = self.operators[indexOp]
        row = len(self.history)
        return (str(self.op), row)

    #unUsedCards = self.getGame().getUnUsedCard()
    def getUnUsedCard(self):
        unUsedCards = list()
        i=0
        while i <len(self.cards):
            if not self.cards[i].isUsed():
                unUsedCards.append(i)
            i+=1
        return unUsedCards

    def eraseLeft(self):
        self.cards[self.left].toggleUse()
        self.left = None
        return len(self.history)

    def eraseOperator(self):
        self.op = None
        return len(self.history)

    def deleteLine(self):
        self.cards.pop()
        left, right = self.history.pop()
        self.cards[left].toggleUse()
        self.cards[right].toggleUse()
        return (left, right)


