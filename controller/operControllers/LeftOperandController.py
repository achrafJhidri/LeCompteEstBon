from controller.operControllers.StateController import StateController


class LeftOperandController(StateController):
    def __init__(self,gameState, next, previous):
        super().__init__(gameState, next, previous)


    def onClick(self, index):
        #get the value of the left operand and the row of last operation of history
        value, row = self.getGame().setLeftOperand(index)
        #we add left operand to the view history at level = row
        self.getView().addLeftOperand(value, row)
        #enable Operators and disable Numbers
        self.getView().enableOperators()
        #enable UnDo Button
        self.getView().enableUnDo()
        self.gameState.currentController = self.next


    def unDo(self):
        return




