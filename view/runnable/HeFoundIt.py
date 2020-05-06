from view.runnable.Runnable import Runnable

class HeFoundIt(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
       self.vue.heFoundIt()