from view.runnable.Runnable import Runnable

class HeHas(Runnable):
    def __init__(self,vue, number):
        Runnable.__init__(self,vue)
        self.num = number

    def run(self):
       self.vue.heHas(self.num)