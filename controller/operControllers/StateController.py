from abc import abstractmethod


class StateController:
    def __init__(self, gameState, next, previous):
        self.gameState = gameState
        self.next = next
        self.previous = previous

    def getGame(self):
        return self.gameState.game

    def getView(self):
        return self.gameState.view

    def deleteLine(self):
        return self.getGame().deleteLine()

    @abstractmethod
    def onClick(self, index):
        pass

    @abstractmethod
    def unDo(self):
        return





