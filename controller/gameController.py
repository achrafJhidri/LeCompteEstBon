from model.TrainingGame import TrainingGame
from view.View import View


class Controller :
    def __init__(self):
        self.game = None
        self.vue=View(self)


    def run(self):
        self.vue.mainloop()

    def setVue(self,view):

        self.vue.frame=view

    def getListNumbers(self):
       return self.game.getCards()

    def getNumberCible(self):
        return int(self.game.target)
    def initTrainingGame(self):
        if self.game :
            self.game.init()
        else :
            self.game = TrainingGame()
            self.game.setName(self.playerName)


    # def evaluate(self,left,op,right):
    #     return int(self.game.evaluate(left,op,right))

    def onCard(self,indexCard):
        if self.game.end :
            return -1
        return self.game.onCard(indexCard)

    def onOp(self,indexOp):
        self.game.onOp(indexOp)

    def evaluate(self,left,op,right):
        return self.game.evaluate(left,op,right)