import tkinter as tk

class History(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller=controller
        self.listOperations =[]
        # History
        self.historyFrame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.historyFrame.grid(row=2, column=0)
        self.history = []

    def addOperandeLeft(self):

        leftOp = tk.Button(self.historyFrame, text="value", state=tk.DISABLED, width=4, height=2)
        leftOp.grid(row=len(self.history), column=0, padx=2)
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

    def addOperandeRight(self):
        pass

    def addOperator(self):
        pass

    def deleteLine(self):
        pass

    def onDeleteHistory(self, index):
        listButtons = self.historyFrame.grid_slaves(row=index)
        for button in listButtons:
            button.destroy()
        self.history.pop()