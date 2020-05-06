from view.runnable.Runnable import Runnable

class SetOpponent(Runnable):
    def __init__(self,vue, opponent):
        Runnable.__init__(self,vue)
        self.opponent = opponent

    def run(self):
       self.vue.setOpponent(self.opponent)