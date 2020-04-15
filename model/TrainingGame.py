
from random import randrange

from model.Game import Game
from model.Solution import Solution


class TrainingGame(Game):
    def __init__(self):
        Game.__init__(self)
        self.resetSolutionDepth()



    def setRandomNumber(self):
        self.target = self.load()

    @staticmethod
    def popRandomCard(cardsCopy):
        rand = randrange(0, len(cardsCopy))
        card = cardsCopy.pop(rand)
        return card

    @staticmethod
    def validate(left, op, right):
        return type(op).isValid(left,right)

    def load(self):
        valid = False

    def solve(self):
        self.solution = Solution()
        solutionFound = self.solution.solve(self.cards, self.target)
        while not solutionFound:
            print("not found")
            self.initCards()
            self.setRandomNumber()
            solutionFound = self.solution.solve(self.cards, self.target)

    def getSolution(self):
        if self.solutionDepth != self.profondeur:
           return str(self.displaySolution())
        else :
            return None


    def init(self):
        Game.init(self) #call the init of the parent
        self.solve()
