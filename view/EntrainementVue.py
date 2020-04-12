
import tkinter as tk
import tkinter.font as tkFont

from view.GameBoardVue import GameBoard


class EntrainementVue(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
#       self.config(width=400,height=400,bd=1,relief="sunken")
        self.previous=previous
        self.controller=controller
        self.title = tk.Frame(self,bd=1,relief=tk.SUNKEN).grid(row=0)
        tk.Label(self.title, text="ENTRAINEMENT", font=tkFont.Font(size="32"))
        self.bottomFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN).grid(row=2)
        self.createWidgets()
        self.gameBoard = GameBoard(self, self.controller)
        self.gameBoard.grid(row=1)



        # self.next1=EntrainementVue(nom,self)




    def createWidgets(self):

        self.back = tk.Button(self.bottomFrame, text="BACK", fg="blue",  command=self.on_back).pack()
        self.back = tk.Button(self.bottomFrame, text="REPLAY", fg="blue", command=self.on_replay).pack()






    def on_back(self):
        self.pack_forget()
        self.previous.pack()

    def on_replay(self):
        print("replay")



# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()