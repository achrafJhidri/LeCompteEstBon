import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from view.MyButton import MyButton
from view.NewHistoryView import NewHistory


class NewGameBoard(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller = controller
        self.controller.setView(self)
        self.controller.setView(self)
        self.cibleFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.cibleValue = tk.StringVar()
        self.cibleValue.set(self.controller.getNumberCible())
        self.cibleLabel = tk.Label(self.cibleFrame, bd=1, relief=tk.SUNKEN, width=5, font=tkFont.Font(size=62),
                                   textvariable=self.cibleValue)
        self.cibleLabel.pack()
        self.cibleFrame.grid(row=0)
        self.listNumbersFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.listNumbersFrame.grid(row=1, column=0)
        self.listOperatorsFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.listOperatorsFrame.grid(row=2, column=1)
        self.history = NewHistory(self)
        self.history.grid(row=2, column=0)
        self.listOperators: list = None
        self.listCards: list < MyButton >= None
        self.createWidgets()

    def createWidgets(self):
        self.createOperators()
        self.createCards()

        self.toggleAll(self.listOperators, "disabled")
        self.toggleAll(self.listCards, "normal")

    def createOperators(self):
        listOp = self.controller.getOperators()
        i = 0
        self.listOperators = list()
        while i < len(listOp):
            button = MyButton(self.listOperatorsFrame, text=str(listOp[i]), width=2, font=tkFont.Font(size=30),
                              fg="blue",
                              command=lambda c=i: self.onClick(c))
            button.grid(row=i)
            self.listOperators.append(button)
            i += 1
        self.unDoBtn = MyButton(self.listOperatorsFrame, state="disable", text="U", width=2, font=tkFont.Font(size=30),
                                fg="blue",
                                command=lambda: self.unDo())
        self.unDoBtn.grid(row=4)

    def createCards(self):
        numbers = self.controller.getListNumbers()
        i = 0
        self.listCards = list()
        while i < len(numbers):
            self.createCard(numbers[i])
            i += 1

    def onClick(self, index):
        self.controller.onClick(index)

    '''
    def updateAfterValidOperation(self):
        i = 0
        while i < len(self.listCards):
            self.listCards[i].config(highlightbackground="red")
            i += 1
    
    '''
    @staticmethod
    def toggleAll(buttons, state):
        for button in buttons:
            button.config(state=state)


    def replay(self):
        self.controller.replay()
        self.cibleValue.set(self.controller.getNumberCible())
        self.history.reset()

        while len(self.listCards) != 0:
            self.listCards.pop().destroy()
        self.createCards()

    def rollBack(self):
        left, right = self.controller.deleteLine()
        self.listCards[left].config(state="normal")
        self.listCards[right].config(state="normal")
        self.listCards.pop().destroy()



    def unDo(self):
        self.controller.unDo()

    def erase(self, row, column):
        self.history.unDo(row,column)



    def deleteLine(self):
        self.listCards.pop()
        left, right = self.controller.deleteLine()
        self.listCards[left].config(state="normal")
        self.listCards[right].config(state="normal")

    def addRightOperand(self, right, result, row):
        self.createCard(result)
        self.history.addResult(right, result, row)

    def disableCard(self, index):
        self.listCards[index].config(state="disable")

    def disableUnDo(self):
        self.unDoBtn.config(state="disable")

    def operationNotValid(self,left, op, right):
        msg= "{0} {1} {2} n'est pas une opération valide".format(left, op, right)
        messagebox.showerror("error", msg, default=messagebox.OK)


    def addLeftOperand(self, value, row):
        self.history.addLeftOperand(value,row)


    def enableOperators(self):
        self.toggleAll(self.listCards, "disable")
        self.toggleAll(self.listOperators, "normal")

    def enableUnDo(self):
        self.unDoBtn.config(state="normal")

    def addOperator(self, operator, row):
        self.history.addOperator(operator, row)


    def enableCards(self, unUsedCards):
        for card in unUsedCards:
            self.listCards[card].config(state="normal")
        self.toggleAll(self.listOperators,"disable")


    def disableCards(self):
        self.toggleAll(self.listCards,"disable")
        self.toggleAll(self.listOperators,"normal")

    def createCard(self, value):
        i = len(self.listCards)
        button = MyButton(self.listNumbersFrame, text=value, width=4, height=2, font=tkFont.Font(size=30),
                          fg="blue", command=lambda c=i: self.onClick(c))
        button.grid(row=int(i/6), column=int(i%6), padx=4, pady=4, )
        self.listCards.append(button)












