import time

from view.CountDownMsgBox import CountDownMsgBox
from view.runnable.Runnable import Runnable


class showMenuPrincipal(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
        self.vue.mpboard.endOfGame()
        CountDownMsgBox(master=self.vue.master, msg_text="Fin de la partie Retour au menu principal dans", sec=5, vue=self.vue)
