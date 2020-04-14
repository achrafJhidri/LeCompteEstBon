
import tkinter as tk

from view.EntrainementVue import EntrainementVue


class MenuPrincipal(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)

        self.config()

        self.controller=controller
        self.previous=previous
        self.createWidgets()

        self.entrainementVue =None



    def show(self):
        self.pack(expand="yes")


    def createWidgets(self):
        self.back = tk.Button(self, text="go back", fg="blue", command=self.on_back)
        self.back.pack(side="bottom",expand="yes")

        self.entrainement = tk.Button(self, text="entrainement", fg="blue",  command=self.on_entrainement)
        self.entrainement.pack(side="left",padx=10,pady=20,expand="yes")

        self.multiPlayer = tk.Button(self, text="multi-joueurs", command=self.on_1vs1)
        self.multiPlayer.pack(side="left",padx=10,pady=20,expand="yes")


    def on_entrainement(self):
        self.controller.initTrainingGame()
        if self.entrainementVue is None :
            self.entrainementVue = EntrainementVue(controller=self.controller, previous=self, master=self.master)
        self.pack_forget()
        self.entrainementVue.pack()


    def on_1vs1(self):
        # self.controller.go1vs1()
        print("go etat 1vs1")

    def on_back(self):
        self.pack_forget()
        self.previous.pack(expand="yes")


