import tkinter as tk
from view.MenuPrincipal import MenuPrincipal
import tkinter.font as tkFont

class Pseudo(tk.Frame):
    def __init__(self,controller,master):
        tk.Frame.__init__(self,master=master)
        self.config()
        self.pack(expand="yes")
        self.controller=controller
        self.createWidgets()


        self.menu=MenuPrincipal(controller=controller,master=master,previous=self)
        self.menu.pack_forget()





    def createWidgets(self):
        self.validate = tk.Button(self, text="valider", fg="blue", command=self.on_validate, padx=5,
                                  default="normal")
        self.validate.pack(side="bottom")
        self.title = tk.Label(self, text="Le Compte est bon", justify="right", font=tkFont.Font(size="32"))
        self.title.pack(expand="yes")

        self.label = tk.Label(self, text="Entrez votre prénom",justify="right")
        self.label.pack(expand="yes")

        r = self.master.winfo_screenwidth()
        screen_width = int(r*1/24)



        self.pseudo = tk.Entry(self,width=screen_width,justify="center")
        self.pseudo.pack()



    def on_validate(self):
        if not self.pseudo.get() :
            pass
        else :
            self.controller.saveName(self.pseudo.get())
            self.pack_forget()
            self.menu.pack(expand="yes")