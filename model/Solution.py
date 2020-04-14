from model.solver import algo


class Solution :

    def __init__(self):
        self.log=list()
    def __call__(self,cards,target):
        stop=list()
        stop.append(False)
        algo(entiers=cards,aTrouver=target,log=self.log,stop=stop)
        print(self.log)
        return self.log

