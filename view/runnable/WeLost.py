from view.runnable.Runnable import Runnable

class WeLost(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
       self.vue.weLost()