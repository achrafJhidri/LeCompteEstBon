
from random import randrange

from model.Game import Game
from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
from model.operators.binaryOperators import Minus, Divide


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

        while not valid :
            # making a copy of the list
            # so that we can at any moment do a backUp
            cardsCopy = self.cards.copy()
            opIndex = randrange(0, 4)  # choosing one random operator between + * / -
            left = self.popRandomCard(cardsCopy).value  # choosing one random operand between the 6 cards
            right = self.popRandomCard(cardsCopy).value  # choosing one random operand between the 5 cards left
            op = self.operators[opIndex]

            if TrainingGame.validate(left,op,right):
                leftC = Constant(left)
                rightC = Constant(right)

                self.solution = BinaryExpression(leftC, op, rightC)  # constructing the first operation ( 10+5)
                self.profondeur = 1  # setting the depth

                # choosing the number of cards to use
                rand = randrange(3, len(self.cards)) - 1

                for i in range(0, rand):
                    opIndex = randrange(0, 3)
                    op = self.operators[opIndex]

                    right = self.popRandomCard(cardsCopy).value

                    rightC = Constant(right)

                    self.solution = BinaryExpression(self.solution, op, rightC)#appending operations to the first operation (left side )

                    # print(self.solution)
                    self.profondeur += 1


                value = self.solution.evaluate()

                if Game.MIN <= value <= Game.MAX:
                    # valid = True
                    return value

    def displaySolution(self):
        depth = self.profondeur
        expr = self.solution
        while depth > self.solutionDepth+1:
            expr = expr.left
            depth -= 1

        self.solutionDepth+=1
        return expr

    def getSolution(self):
        if self.solutionDepth != self.profondeur:
           return str(self.displaySolution())
        else :
            return None


    def resetSolutionDepth(self):
        self.solutionDepth=0
