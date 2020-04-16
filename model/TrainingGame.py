from model.Game import Game

from model.NewGame import NewGame
from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
from model.operators.binaryOperators import Minus, Divide
from model.Solution import Solution




#class TrainingGame(Game):
class TrainingGame(NewGame):
    def __init__(self):
        Game.__init__(self)

    def solve(self):
        self.solution = Solution()
        solutionFound = self.solution.solve(self.cards, self.target)
        while not solutionFound:
            print("not found")
            self.initCards()
            self.setRandomNumber()
            solutionFound = self.solution.solve(self.cards, self.target)

    def getSolution(self):
        return self.solution.getSolution()

    def resetSolution(self):
        return self.solution.resetSolution()

    def init(self):
        Game.init(self) #call the init of the parent
        self.solve()
