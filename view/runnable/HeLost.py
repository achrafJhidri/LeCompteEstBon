from view.runnable.Runnable import Runnable

class HeLost(Runnable):
    def __init__(self,vue,  nothing):
        Runnable.__init__(self,vue)
        self.nothing = nothing


    def run(self):
       self.vue.heLost(self.nothing)