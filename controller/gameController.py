from view.View import View
from model.Game import Game
from model.TrainingGame import TrainingGame



class Controller :
    def __init__(self):
        self.game : Game = None
        self.vue=View(self)


    def run(self):
        self.vue.mainloop()

    def setVue(self,view):
        self.vue.frame=view

    def getListNumbers(self):
        listNumbers = list()
        for card in self.game.getCards():
            listNumbers.append(card.value)
        return listNumbers

    def getNumberCible(self):
        return int(self.game.target)
    def initTrainingGame(self):
        if self.game :
            self.game.init()
        else :
            self.game = TrainingGame()
            self.game.setName(self.playerName)




    def onCard(self,indexCard):
        if self.game.end :
            return -1
        return self.game.onCard(indexCard)

    def onOp(self,indexOp):
        return self.game.onOp(indexOp)

    def getOperators(self):
        return self.game.operators

    def getLeft(self):
        return self.game.history.getLeft()

    def goMenuPrincipal(self):
        self.vue.goMenuPrincipale()

    def rollBack(self):
        self.game.rollBack()

    def getUnUsedCards(self):
        return self.game.getUnUsedCards()

    def operatorIsNext(self):
        return self.game.operatorIsNext()

    def unDo(self):
        self.game.unDo()
        isOperator = self.operatorIsNext()
        return isOperator



    def saveName(self,name):
        self.playerName=name


    def askForSolution(self):
        return self.game.getSolution()

    def resetSolution(self):
        return self.game.resetSolution()
