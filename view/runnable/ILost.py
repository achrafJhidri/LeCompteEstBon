from view.runnable.Runnable import Runnable

class ILost(Runnable):
    def __init__(self,vue, nothing):
        Runnable.__init__(self,vue)
        self.nothing = nothing

    def run(self):
       self.vue.iLost(self.nothing)