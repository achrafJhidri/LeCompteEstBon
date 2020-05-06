import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox

from assets.Constantes import Config

from view.gameBoard.HistoryView import History


class GameBoard(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master=master)
        self.controller = controller
        self.controller.setView(self)

        self.initTargetFrame()
        self.initCardsFrame()
        self.initOperatorsFrame()
        self.initHistoryFrame()

        self.listOperators = None
        self.listCards= None

        self.createWidgets()
    def initHistoryFrame(self):
        self.history = History(self)
        self.history.grid(row=2, column=0)

    def initOperatorsFrame(self):
        self.listOperatorsFrame = tk.Frame(self, bd=1)
        self.listOperatorsFrame.grid(row=2, column=1)
    def initCardsFrame(self):
        self.listNumbersFrame = tk.Frame(self, bd=1)
        self.listNumbersFrame.grid(row=1, column=0)
    def initTargetFrame(self):
        self.cibleFrame = tk.Frame(self, bd=1)
        self.cibleValue = tk.StringVar()
        self.cibleValue.set(self.controller.getNumberCible())
        self.cibleLabel = tk.Label(self.cibleFrame, bd=1, width=5, font=tkFont.Font(size=62), textvariable=self.cibleValue)
        self.cibleLabel.pack()
        self.cibleFrame.grid(row=0)
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
            button = tk.Button(self.listOperatorsFrame, text=str(listOp[i]), width=1, font=tkFont.Font(size=10),
                               fg="blue",
                               command=lambda c=i: self.onClick(c))
            button.grid(row=i)
            self.listOperators.append(button)
            i += 1
        self.unDoBtn = tk.Button(self.listOperatorsFrame, state="disable", text="U", width=1, font=tkFont.Font(size=10),
                                fg="blue",
                                command=lambda: self.unDo())
        self.unDoBtn.grid(row=4)
    def createCards(self):
        numbers = self.controller.getListNumbers()
        i = 0
        self.listCards = list()
        while i < len(numbers):
            button = tk.Button(self.listNumbersFrame, text=numbers[i], width=5, font=tkFont.Font(size=10), fg="blue",
                              command=lambda c=i: self.onClick(c))
            button.grid(row=0, column=i, )
            self.listCards.append(button)
            i += 1
    def onClick(self, index):
        self.controller.onClick(index)
    @staticmethod
    def toggleAll(buttons, state):
        for button in buttons:
            button.config(state=state)

    def replay(self, game=None):
        self.controller.replay(game)
        self.cibleValue.set(self.controller.getNumberCible())
        self.history.reset()
        while len(self.listCards) != 0:
            self.listCards.pop().destroy()
        self.createCards()
        self.disableUnDo()
        self.toggleAll(self.listOperators, "disable")
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
    def disable(self):
        self.toggleAll(self.listCards, "disable")
    def enable(self):
        self.toggleAll(self.listCards, "normal")
    def createCard(self, value):
        button = tk.Button(self.listNumbersFrame, text=value, width=5, font=tkFont.Font(size=10),
                          fg="blue", command=lambda c=len(self.listCards): self.onClick(c))
        button.grid(row=1, column=len(self.listCards) - Config().NUMBER_OF_CARDS)
        self.listCards.append(button)
    def targetFound(self):
        answer = messagebox.askyesno("replay", "Bravo vous avez trouvé ! voulez-vous rejouer ?")
        if answer:
            self.master.on_replay()
        else:
            self.master.forget()
            self.controller.goMenuPrincipal()


class GameBoardMultiPlayer(GameBoard):
    def __init__(self, master, controller):
        GameBoard.__init__(self, master=master,controller=controller)

    def disable(self):
        self.toggleAll(self.listCards, "disable")
        self.toggleAll(self.listOperators,"disable")
        self.disableUnDo()
        self.history.disable()
    def enable(self):
        self.toggleAll(self.listCards, "normal")
    def targetFound(self):
        self.master.targetFound()

    def setTarget(self, newTarget):
        self.cibleValue.set(newTarget)


