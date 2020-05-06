from view.runnable.Runnable import Runnable


class OnWait(Runnable):
    def __init__(self,vue, msg):
        Runnable.__init__(self,vue)
        self.msg = msg


    def run(self):
        self.vue.onWait(self.msg)