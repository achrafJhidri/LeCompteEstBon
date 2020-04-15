from model.solver import algo


class Solution :

    def __init__(self):
        self.log=list()
        self.solutionIndex=0
    def solve(self, cards ,target):
        i = 0
        entiers = list()
        while i < len(cards) :
            # on transforme les Cards en entiers
            entiers.append(cards[i].value)
            i+=1

        stop=list()
        stop.append(False)
        algo(entiers=entiers,aTrouver=target,log=self.log,stop=stop)

        return len(self.log) > 0

    def getSolution(self):
        result = None
        if self.solutionIndex < len(self.log) :
            result=  self.log[self.solutionIndex]
            self.solutionIndex+=1
        return result



    def resetSolution(self):
        self.solutionIndex=0

