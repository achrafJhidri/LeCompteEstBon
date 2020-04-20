import model
from controller.operControllers.StateController import StateController
from model.TrainingGame import TrainingGame
from model.expressions.binaryEx import BinaryExpression


class RightOperandController(StateController):
    def __init__(self,gameState, next, previous):
        super().__init__(gameState, next, previous)


    def onClick(self, index):
        #getCurrentOp not with index
        currentOp:BinaryExpression = self.getGame().getCurrentOperation(index)

        op = currentOp.op
        left = currentOp.left
        right = currentOp.right
        #if operation is valid
        if (type(op).isValid(left.evaluate(), right.evaluate())):
            result = currentOp.evaluate()


            #we add a new line in history and add New card
            row = self.getGame().addOperation(result)
            #we add right operand in the view and Add new Card
            self.getView().addRightOperand(right,result, row)
            # card clicked is used so we disable it
            self.getView().disableCard(index)
            #disable UnDo Button
            self.getView().disableUnDo()

            if result == self.getGame().target:
                self.getView().askForReplay()
            self.gameState.currentController = self.next



        else:
            #otherwise we write an error message
            self.getView().operationNotValid(left, op, right)

    def unDo(self):
        row = self.getGame().eraseOperator()
        self.getView().disableCards()
        self.getView().erase(row,1)
        self.gameState.currentController = self.previous

