from view.runnable.Runnable import Runnable


class showMultiPlayerBoard(Runnable):
    def __init__(self,vue, sec):
        Runnable.__init__(self,vue)
        self.sec = sec


    def run(self):
        self.vue.showMultiPlayerBoard(self.sec)