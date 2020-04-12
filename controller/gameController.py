from model.Game import Game
from view.MenuPrincipal import MenuPrincipal
from view.View import View


class Controller :
    def __init__(self):
        self.game = Game()
        self.vue=View(self)


    def run(self):
        self.vue.mainloop()

    def setVue(self,view):

        self.vue.frame=view

    def getListNumbers(self):
       return self.game.getListNumbers()

    def getNumberCible(self):
        return 5