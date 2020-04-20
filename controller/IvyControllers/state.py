class State:

    def __init__(self, next, previous, manager):
        self.previous = previous
        self.next = next
        self.manager = manager

    def run(self):
        raise NotImplementedError("Not implemented at this level")

    def goNext(self):
        self.setState( self.next)

    def goPrevious(self):
        self.setState(self.previous)

    def setState(self,state):
        self.manager.setState(state)
        self.manager.current.run()