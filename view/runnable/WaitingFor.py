from view.runnable.Runnable import Runnable
from tkinter import messagebox

class WaitingFor(Runnable):
    def __init__(self,vue):
        Runnable.__init__(self,vue)


    def run(self):
        #messagebox.showinfo(title="please wait" ,message="still waiting for the second player")
        print(self.vue)
        print(self.vue.infoLabel.cget('text'))
        self.vue.infoLabel.config(text="En attente d'un deuxième joueur")
        print(self.vue.infoLabel.cget('text'))
