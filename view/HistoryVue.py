import tkinter as tk

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

    def addOperandeLeft(self,value):
        lastRow = self.lastRow()
        if(lastRow>=0 and self.history[lastRow][self.LEFT].cget("text")==""):
            self.history[lastRow][self.LEFT].config(text=value)
        else:
            nbRows = lastRow+1
            buttonList = list()
            leftOp = tk.Button(self, text=value, state=tk.DISABLED, width=4, height=2)
            leftOp.grid(row=nbRows, column=self.LEFT, padx=2)
            buttonList.append(leftOp)
            #create line
            for i in range(1,6):
                operator = tk.Button(self, text="", state=tk.DISABLED, width=4, height=2)
                operator.grid(row=nbRows, column=i, padx=2)
                buttonList.append(operator)
            self.history.append(buttonList)
            if (nbRows > 0):
                self.history[nbRows - 1][self.DEL].config(state=tk.DISABLED)

    def addOperator(self, operator):
        button = self.history[self.lastRow()][self.OP]
        button.configure(text=operator)

    def lastRow(self):
        return len(self.history) -1


        '''
        # New button for history
        rightOp = tk.Button(self.historyFrame, text="value", state=tk.DISABLED, width=4, height=2)
        rightOp.grid(row=len(self.history), column=2, padx=2)

        # Button =
        equalButton = tk.Button(self.historyFrame, text="=", state=tk.DISABLED, width=4, height=2)
        equalButton.grid(row=len(self.history), column=3, padx=2)

        # Button result
        resultButton = tk.Button(self.historyFrame, text="esult", state=tk.DISABLED, width=4, height=2)
        resultButton.grid(row=len(self.history), column=4, padx=2)

        # Button delete line
        deleteButton = tk.Button(self.historyFrame, text="x", fg="red", width=4, height=2,
                                 command=lambda c=len(self.history): self.onDeleteHistory(c))
        deleteButton.grid(row=len(self.history), column=5)

        opButton = tk.Button(self.historyFrame, text=repr(self.currentOperation.op), state=tk.DISABLED, width=4,
                             height=2)
        opButton.grid(row=len(self.history), column=1)



        # add to history
        self.history.append(self.currentOperation)
        '''
    def addOperandeRight(self, value, result):
        #RightOperande
        row = self.lastRow()
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



    def deleteLine(self):
        self.deleteLastButtons()
        if(self.lastRow()>=0):
            self.master.rollBack()

    def unDo(self, isOperator):
        if(isOperator):
            self.history[self.lastRow()][self.OP].config(text="")
        else:
            self.deleteLastButtons()

    def deleteLastButtons(self):
        row = self.lastRow()
        listButtons = self.history[row]
        for button in listButtons:
            button.destroy()
        self.history.pop()
        if (row > 0):
            self.history[row - 1][self.DEL].config(state=tk.NORMAL)

    def reset(self):
        print("reset")
        while self.lastRow()>=0:
            print("deleteLine")
            self.deleteLine()



