from view.runnable.Runnable import Runnable

class HeGotIt(Runnable):
    def __init__(self,vue, decisionTime):
        Runnable.__init__(self,vue)
        self.decisionTime = decisionTime


    def run(self):
       self.vue.heGotIt(self.decisionTime)