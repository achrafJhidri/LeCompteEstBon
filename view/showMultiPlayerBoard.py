from view.Runnable import Runnable
from tkinter import messagebox

class showMultiPlayerBoard(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
        self.vue.showMultiPlayerBoard()