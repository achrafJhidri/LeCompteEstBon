from controller.operControllers.StateController import StateController


class OperatorController(StateController):
    def __init__(self,gameState, next, previous):
        super().__init__(gameState, next, previous)

    def onClick(self, index):
        #set operator associated with index, and get the char associated with
        operator, row = self.getGame().setOperator(index)
        #we add operator to the view at level = row
        self.getView().addOperator(operator,row)
        #get unused card's index to enable them
        unUsedCards = self.getGame().getUnUsedCard()
        #enable unused card and disable operator
        self.getView().enableCards(unUsedCards)
        self.gameState.currentController = self.next

    def unDo(self):
        print("undoOperator")
        row = self.getGame().eraseLeft()
        self.getView().disableUnDo()
        unUsedCards = self.getGame().getUnUsedCard()
        self.getView().enableCards(unUsedCards)
        self.getView().erase(row,0)
        self.gameState.currentController = self.previous




