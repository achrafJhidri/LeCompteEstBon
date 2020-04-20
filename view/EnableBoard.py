from view.Runnable import Runnable

class EnableBoard(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
       self.vue.enableBoard()