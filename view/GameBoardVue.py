import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tokenize import String

from view.HistoryVue import History
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
        self.history = History(self)
        self.history.grid(row=2, column=0)
        self.listOperators: list=None
        self.listCards :list<MyButton>=None
        self.createWidgets()



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
        self.unDoBtn =MyButton(self.listOperatorsFrame,state="disable", text="U", width=2, font=tkFont.Font(size=30), fg="blue",
                 command=lambda: self.unDo())
        self.unDoBtn.grid(row=4)

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
        self.unDoBtn.config(state="normal")
        result = self.controller.onCard(index)
        if  type(result) == type(String):
            messagebox.showerror("error",result,default=messagebox.OK)
        elif result == 0 :
            self.listCards[index].config(highlightbackground="green")
            self.history.addOperandeLeft(self.listCards[index].cget("text"))
        elif result == -1 :#fin du game
            answer = messagebox.askyesno("replay","Bravo vous avez trouvé ! voulez-vous rejouer ?")
            if answer:
                self.replay()
            else :
                self.master.forget()
                self.controller.goMenuPrincipal()

        else:
            button = MyButton(self.listNumbersFrame, text=result, width=4, height=2, font=tkFont.Font(size=30),
                              fg="blue", command=lambda c=len(self.listCards): self.on_card(c))
            button.grid(row=1, column=len(self.listCards)-6, padx=4, pady=4)
            self.listCards.append(button)
            self.history.addOperandeRight(self.listCards[index].cget("text"), result)
            #self.updateAfterValidOperation()
            self.unDoBtn.config(state="disable")
        self.updateCards()

    def updateAfterValidOperation(self):
        i=0
        while i  < len(self.listCards):
            self.listCards[i].config(highlightbackground="red")
            i+=1


    def onOp(self,index):
        op=self.controller.onOp(index)
        self.history.addOperator(op)
        self.updateCards()

    @staticmethod
    def toggleAll(buttons,state):
        for button in buttons:
            button.config(state=state)

    def replay(self):
        self.controller.initTrainingGame()
        self.cibleValue.set(self.controller.getNumberCible())
        self.history.reset()

        while len(self.listCards) != 0:
            self.listCards.pop().destroy()
        self.createCards()

    def rollBack(self):
     #  lastCards = self.controller.getLastCards()
     #   for card in lastCards:
     #     self.listCards[card].unUse()
        print("rollBack")
        self.controller.rollBack()
        self.listCards.pop().destroy()
        self.updateCards()

    def updateCards(self):
        '''
        #next = 0 if next Char to enter is Number
        #Otherwise it's an operator
        '''

        next = self.controller.operatorIsNext()
        if(next==True):
            self.toggleAll(self.listOperators, "normal")
            self.toggleAll(self.listCards, "disable")
        else:
            self.toggleAll(self.listOperators, "disable")
            cards = self.controller.getUnUsedCards()
            i=0
            while i < len(self.listCards):
                if(i in cards):
                    self.listCards[i].config(state="normal")
                else:
                    self.listCards[i].config(state="disable")
                i+=1

    def unDo(self):
        isOperator = self.controller.unDo()
        self.updateCards()
        self.history.unDo(isOperator)





