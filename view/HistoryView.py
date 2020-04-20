import tkinter as tk
import tkinter.font as tkFont

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
        self.createGrid()

    def createGrid(self):
        i  = 0
        while i < 6:
            buttonList = list()
            # create line
            for j in range(0, 5):
                operator = tk.Button(self, text="", state=tk.DISABLED, width=5, font=tkFont.Font(size=10))
                operator.grid(row=i, column=j)
                buttonList.append(operator)
            operator = tk.Button(self, text="", state=tk.DISABLED, width=5, font=tkFont.Font(size=10),
                                 fg="red", command=lambda c=i:self.deleteLine(c))
            operator.grid(row=i, column=6)
            buttonList.append(operator)
            self.history.append(buttonList)
            i+=1


    def reset(self):
        for line in self.history:
            for i in range(0, 6):
                line[i].config(text="", state=tk.DISABLED)

    def unDo(self, row, column):
        self.history[row][column].config(text="")
        if (column == self.LEFT and row > 0) :
            self.history[row-1][self.DEL].config(state=tk.NORMAL)

    def addResult(self,right,result, row ):
        self.history[row][self.RIGHT].config(text=right)
        self.history[row][self.EQUAL].config(text="=")
        self.history[row][self.RES].config(text=result)
        self.history[row][self.DEL].config(text="x", state=tk.NORMAL)

    def addLeftOperand(self, value, row):
        self.history[row][self.LEFT].config(text=value)
        if(row > 0):
            self.history[row-1][self.DEL].config(state=tk.DISABLED)


    def addOperator(self, operator, row):
        self.history[row][self.OP].config(text=operator)

    def deleteLine(self, row):
        self.history[row][self.DEL].config(text="", state=tk.DISABLED)
        for i in range(0, 5):
            self.history[row][i].config(text="")
        if(row > 0):
            self.history[row-1][self.DEL].config(state=tk.NORMAL)
        self.master.rollBack()











