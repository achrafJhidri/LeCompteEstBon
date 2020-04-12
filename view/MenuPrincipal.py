
import tkinter as tk

from view.EntrainementVue import EntrainementVue


class MenuPrincipal(tk.Frame):
    def __init__(self,controller,master):
        tk.Frame.__init__(self,master=master)
        self.config(width=200,height=200,bd=1,relief="sunken")

        self.pack()


        self.controller=controller
        self.createWidgets()

        self.entrainementVue=None





    def createWidgets(self):

        self.entrainement = tk.Button(self, text="entrainement", fg="blue",  command=self.on_entrainement)
        self.entrainement.pack(expand="no")


        self.multiPlayer = tk.Button(self, text="1vs1", command=self.on_1vs1)
        self.multiPlayer.pack(expand="no")


    def on_entrainement(self):
        self.controller.initTrainingGame()
        if ( self.entrainementVue is None):
            self.entrainementVue = EntrainementVue(controller=self.controller, previous=self, master=self.master)
        self.pack_forget()
        self.entrainementVue.pack()


    def on_1vs1(self):
        # self.controller.go1vs1()
        print("go etat 1vs1")


# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()