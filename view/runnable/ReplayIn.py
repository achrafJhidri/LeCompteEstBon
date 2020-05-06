from view.runnable.Runnable import Runnable

class ReplayIn(Runnable):
    def __init__(self,vue, sec):
        Runnable.__init__(self,vue)
        self.sec = sec


    def run(self):
        self.vue.replayIn(self.sec)
