import tkinter as tk
import tkinter.font as tkFont


from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression
from model.operators.binaryOperators import Plus, Multi, Divide, Minus
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

        self.listCards=None
        self.listOperators=None

        self.currentOperation : BinaryExpression = None
        self.createWidgets()



    def createWidgets(self):
        self.createOperators()
        self.createCards()

        self.toggleAll(self.listOperators,"disabled")
        self.toggleAll(self.listCards,"normal")


    def createOperators(self):
        self.listOperators = list()
        button = MyButton(self.listOperatorsFrame, text="+", width=2, font= tkFont.Font(size=30),  fg="blue",command=lambda c = 0 : self.onOp(c))
        button.grid(row=0)
        self.listOperators.append(button)
        button = MyButton(self.listOperatorsFrame, text="x", width=2, font= tkFont.Font(size=30),  fg="blue",command=lambda c = 1 : self.onOp(c))
        button.grid(row=1)
        self.listOperators.append(button)
        button = MyButton(self.listOperatorsFrame, text="/", width=2,  font= tkFont.Font(size=30),  fg="blue",command=lambda c = 2 : self.onOp(c))
        button.grid(row=2)
        self.listOperators.append(button)
        button = MyButton(self.listOperatorsFrame, text="-", width=2,  font= tkFont.Font(size=30),  fg="blue",command=lambda c = 3 : self.onOp(c))
        button.grid(row=3)
        self.listOperators.append(button)

        self.operators= dict()
        self.operators[0]=Plus()
        self.operators[1]=Multi()
        self.operators[2]=Divide()
        self.operators[3]=Minus()



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
        self.listCards[index].use()
        # for button in self.listCards:
        #     button.config(state="disable")
        if(self.currentOperation is None ):
            self.currentOperation=BinaryExpression(Constant(self.listCards[index].cget("text")),None,None)
            self.toggleAll(self.listOperators, "normal")
            self.toggleAll(self.listCards, state="disable")
        else :
            self.currentOperation.right = Constant(self.listCards[index].cget("text"))
            result = self.currentOperation.evaluate()
            button = MyButton(self.listNumbersFrame, text=result, width=4, height=2, font=tkFont.Font(size=30),
                                  fg="blue", command=lambda c=len(self.listCards): self.on_card(c))
            button.grid(row=0,column=len(self.listCards),padx=4,pady=4)
            self.listCards.append(button)
            self.currentOperation = None




    def onOp(self,index):
        self.toggleAll(self.listCards, "normal")
        self.toggleAll(self.listOperators, state="disabled")
        self.currentOperation.op=self.operators[index]


    @staticmethod
    def toggleAll(buttons,state):
        for button in buttons:
            if not button.isUsed() :
                button.config(state=state)

    def replay(self):
        self.controller.initTrainingGame()
        self.cibleValue.set(self.controller.getNumberCible())


        # self.cibleLabel.pack()