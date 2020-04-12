
import tkinter as tk


class EntrainementVue(tk.Frame):
    def __init__(self,controller,master,previous):
        tk.Frame.__init__(self,master=master)
        self.config(width=500,height=500,bd=1,relief="sunken")

        # self.grid()
        self.previous=previous

        self.controller=controller
        self.createWidgets()



        # self.next1=EntrainementVue(nom,self)




    def createWidgets(self):
        # self.back = tk.Button(self, text="6", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=0,row=0)
        # self.back = tk.Button(self, text="9", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=1,row=0)
        # self.back = tk.Button(self, text="1", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=2,row=0)
        # self.back = tk.Button(self, text="75", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=3,row=0)
        # self.back = tk.Button(self, text="25", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=4,row=0)
        # self.back = tk.Button(self, text="100", fg="blue", command=self.on_back,padx=10)
        # self.back.grid(column=5,row=0)
        #
        #
        # self.back = tk.Button(self, text="go back", fg="blue",  command=self.on_back)
        # self.back.grid(row=4,columnspan=6)
        self.back = tk.Button(self, text=" 6 ", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=0, y=0)
        self.back = tk.Button(self, text=" 9 ", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=50, y=0)
        self.back = tk.Button(self, text=" 1 ", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=100, y=0)
        self.back = tk.Button(self, text=" 75", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=150, y=0)
        self.back = tk.Button(self, text=" 25", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=200, y=0)
        self.back = tk.Button(self, text="100", fg="blue", command=self.on_click,padx=10,pady=10)
        self.back.place(x=250, y=0)

        self.back = tk.Button(self, text="go back", fg="blue", command=self.on_back,padx=10)
        self.back.place(x=200, y=100)

    def on_back(self):
        self.forget()
        self.previous.pack()
    def on_click(self):
        print(self.back)



# root = tk.Tk()
# app = Application(master=root)
# app.mainloop()