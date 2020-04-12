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
        self.game=TrainingGame()