
import tkinter as tk


class EntrainementVue(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
        self.config(width=200,height=200,bd=1,relief="sunken")

        self.pack()
        self.previous=previous

        self.controller=controller
        self.createWidgets()



        # self.next1=EntrainementVue(nom,self)




    def createWidgets(self):

        self.back = tk.Button(self, text="go back", fg="blue",  command=self.on_back)
        self.back.pack(expand="no")





    def on_back(self):
        self.pack_forget()
        self.previous.pack()



# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()