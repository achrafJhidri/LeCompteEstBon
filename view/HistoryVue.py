import tkinter as tk
from assets.Constantes import Config

class History(tk.Frame):
    def __init__(self, master):
        self.master=master
        tk.Frame.__init__(self, master=master)
        self.listOperations =[]
        self.history = []
        self.LEFT = 0
        self.OP = 1
        self.RIGHT = 2
        self.EQUAL = 3
        self.RES = 4
        self.DEL = 5

        self.actualRow=0
        self.createGrid()

    def createGrid(self):
        i  = 0
        while i < Config().NUMBER_OF_CARDS:
            buttonList = list()
            # create line
            for j in range(0, 6):
                operator = tk.Button(self, text="", state=tk.DISABLED, width=5)
                operator.grid(row=i, column=j)
                buttonList.append(operator)
            self.history.append(buttonList)
            i+=1

    def addOperandeLeft(self,value):
        self.history[self.actualRow][self.LEFT].config(text=value)

    def addOperator(self, operator):
        self.history[self.actualRow][self.OP].configure(text=operator)

    def addOperandeRight(self, value, result):
        #RightOperande
        row = self.actualRow
        rightOp = self.history[row][self.RIGHT]
        rightOp.configure(text=value)

        #equalBtn
        equalBtn=self.history[row][self.EQUAL]
        equalBtn.configure(text="=")

        #result
        resultBtn =self.history[row][self.RES]
        resultBtn.configure(text=result)

        #deleteBtn
        deleteBtn = self.history[row][self.DEL]
        deleteBtn.config(text="x", fg="red",state=tk.NORMAL, command=lambda : self.deleteLine())

        if self.actualRow > 0  :
            self.history[self.actualRow-1][self.DEL].config(text="x", fg="red", state=tk.DISABLED)
        self.actualRow += 1


    def deleteLine(self):
        self.deleteLastButtons()
        self.master.rollBack()

    def unDo(self, isOperator):
        if(isOperator):
            self.history[self.actualRow][self.OP].config(text="")
        else:
            self.history[self.actualRow][self.LEFT].config(text="")

    def deleteLastButtons(self):

        if self.actualRow != 1 :
            self.history[self.actualRow - 2][self.DEL].config(state=tk.NORMAL)

        listButtons = self.history[self.actualRow - 1]
        for button in listButtons:
            button.config(text="", state=tk.DISABLED)
        self.actualRow -= 1

    def reset(self):

        self.history.clear()
        self.createGrid()
        self.actualRow=0
