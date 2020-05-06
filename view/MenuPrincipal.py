import tkinter as tk

from view.training.EntrainementVue import EntrainementVue
from view.multiplayer.MenuMultiJoueur import MenuMultiJoueur


class MenuPrincipal(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
        self.previous = previous
        self.config()

        self.controller=controller
        self.createWidgets()

        self.entrainementVue =None






    def show(self):
        self.pack(expand="yes")

    def createWidgets(self):
        self.back = tk.Button(self, text="Retour", fg="blue", command=self.on_back)
        self.back.pack(side="bottom",expand="yes")

        self.entrainement = tk.Button(self, text="Entrainement", fg="blue",  command=self.on_entrainement)
        self.entrainement.pack(side="left",padx=10,pady=20,expand="yes")

        self.multiPlayer = tk.Button(self, text="Multijoueurs", command=self.on_1vs1)
        self.multiPlayer.pack(side="left",padx=10,pady=20,expand="yes")


    def on_entrainement(self):
        self.controller.initTrainingGame()
        if self.entrainementVue  :
                self.entrainementVue.destroy()
        self.entrainementVue = EntrainementVue(controller=self.controller, previous=self, master=self.master)
        self.pack_forget()
        self.entrainementVue.pack()


    def on_1vs1(self):
        if not hasattr(self, "multiPlayerVue"):
            self.multiPlayerVue = MenuMultiJoueur(controller=self.controller, previous=self, master=self.master)

        #   self.multiPlayerVue.destroy()
        self.pack_forget()
        self.multiPlayerVue.pack(expand="yes")

    def on_back(self):
        self.pack_forget()
        self.previous.pack(expand="yes")


