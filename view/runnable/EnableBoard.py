from view.runnable.Runnable import Runnable

class EnableBoard(Runnable):
    def __init__(self,vue, decisionTime, both):
        Runnable.__init__(self,vue)
        self.decisionTime = decisionTime
        self.both = both


    def run(self):
       self.vue.enableBoard(self.decisionTime, self.both)