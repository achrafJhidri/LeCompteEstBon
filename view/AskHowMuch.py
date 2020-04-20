from view.Runnable import Runnable

class AskHowMuch(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
       self.vue.askHowMuch()