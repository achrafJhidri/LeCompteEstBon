import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tokenize import String


from view.MyButton import MyButton


class GameBoard(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller=controller
        self.cibleFrame = tk.Frame(self,bd=1,relief=tk.SUNKEN)
        self.cibleValue= tk.StringVar()
        self.cibleValue.set(self.controller.getNumberCible())
        self.cibleLabel = tk.Label(self.cibleFrame,bd=1,relief=tk.SUNKEN, width= 5, font= tkFont.Font(size=62), textvariable=self.cibleValue)
        self.cibleLabel.pack()
        self.cibleFrame.grid(row=0)
        self.listNumbersFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.listNumbersFrame.grid(row=1,column=0)
        self.listOperatorsFrame=tk.Frame(self,bd=1 , relief=tk.SUNKEN)
        self.listOperatorsFrame.grid(row=2,column=1)

        self.listCards :list<MyButton>=None
        self.listOperators: list=None


        self.createWidgets()

        self.numberOfAdditionnalCards=0



    def createWidgets(self):
        self.createOperators()
        self.createCards()

        self.toggleAll(self.listOperators,"disabled")
        self.toggleAll(self.listCards,"normal")


    def createOperators(self):
        listOp = self.controller.getOperators()
        i = 0
        self.listOperators = list()
        while i < len(listOp):
            button = MyButton(self.listOperatorsFrame, text=str(listOp[i]), width=2, font=tkFont.Font(size=30), fg="blue",
                              command=lambda c=i: self.onOp(c))
            button.grid(row=i)
            self.listOperators.append(button)
            i+=1

    def createCards(self):
        numbers = self.controller.getListNumbers()
        i = 0
        self.listCards = list()
        while i < len(numbers):
            button = MyButton(self.listNumbersFrame, text=numbers[i], width=4, height=2, font=tkFont.Font(size=30),
                              fg="blue", command=lambda c=i: self.on_card(c))
            button.grid(row=0, column=i, padx=4, pady=4, )
            self.listCards.append(button)
            i += 1

    def on_card(self,index):
        result = self.controller.onCard(index)
        if  type(result) == type(String)  :
            messagebox.showerror("error",result,default=messagebox.OK)
            self.listCards[self.leftIndex].unUse()
            self.leftIndex=None
        elif result == 0 :
            #op gauche
            self.toggleAll(self.listOperators, "normal")
            self.toggleAll(self.listCards,    "disable")
            self.listCards[index].config(highlightbackground="green")
            self.listCards[index].use()
            self.leftIndex=index
        elif result == -1 :#fin du game
            answer = messagebox.askyesno("replay","vous voulez rejouer ?")
            if answer:
                self.replay()
            else :
                self.master.forget()
                self.controller.goMenuPrincipal()

        else :
            button = MyButton(self.listNumbersFrame, text=result, width=4, height=2, font=tkFont.Font(size=30),
                              fg="blue", command=lambda c=len(self.listCards): self.on_card(c))
            button.grid(row=1, column=self.numberOfAdditionnalCards, padx=4, pady=4)
            self.numberOfAdditionnalCards += 1
            self.listCards.append(button)
            self.listCards[index].use()
            self.updateAfterValidOperation()

    def updateAfterValidOperation(self):
        i=0
        while i  < len(self.listCards):
            self.listCards[i].config(highlightbackground="red")
            i+=1


    def onOp(self,index):
        self.toggleAll(self.listCards, "normal")
        self.toggleAll(self.listOperators, state="disabled")
        self.controller.onOp(index)


    @staticmethod
    def toggleAll(buttons,state):
        for button in buttons:
            if not button.isUsed() :
                button.config(state=state)

    def replay(self):
        self.controller.initTrainingGame()
        self.cibleValue.set(self.controller.getNumberCible())

        while len(self.listCards) != 0:
            self.listCards.pop().destroy()
        self.createCards()
        self.numberOfAdditionnalCards=0
