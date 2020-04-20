
from model.Game import Game
from model.Solution import Solution

class TrainingGame(Game):
    def __init__(self):
        Game.__init__(self)

    def solve(self):
        self.solution = Solution()
        solutionFound = self.solution.solve(self.cards, self.target)
        while not solutionFound:
            self.initCards()
            self.setRandomNumber()
            solutionFound = self.solution.solve(self.cards, self.target)

    def getSolution(self):
        return self.solution.getSolution()

    def resetSolution(self):
        self.solution.resetSolution()

    def init(self):
        Game.init(self) #call the init of the parent
        self.solve()
