from model.expressions.Ex import Constant
from model.expressions.binaryEx import BinaryExpression


class History:

    def __init__(self):
        self.init()

    def init(self):
        self.currentOperation = None
        self.listOperations = list()  # list of operation (IndexLeftOp,Op, IndexRightOp)

    def addOperande(self,indexCard):
        if  self.currentOperation is None:
            self.currentOperation = BinaryExpression(indexCard, None, None)
        else:
            self.currentOperation.right=indexCard
            self.listOperations.append(self.currentOperation)
            self.currentOperation = None

    def nextIdex(self):
        return self.currentOperation.count()


    def addOperator(self, operator):
        self.currentOperation.op=operator

    def erase(self):
        if(self.currentOperation and self.getOp()):
            self.currentOperation.op=None
        else:
            self.currentOperation=None

    def deleteLastOperation(self):
        self.listOperations.pop()
        self.currentOperation=None

    def getLastCards(self):
         if(len(self.listOperations)>0):
             lastOp = self.listOperations.pop()
             return lastOp.left, lastOp.right


    def evaluateCurrentOp(self, left, right):
        res=  BinaryExpression(Constant(left),self.currentOperation.op,Constant(right)).evaluate()
        return res

    def getLeft(self):
        if(self.currentOperation):
            return self.currentOperation.left
        else:
            return None

    def getRight(self):
        if(self.currentOperation):
            return self.currentOperation.right
        else:
            return None

    def getOp(self):
        if(self.currentOperation):
            return self.currentOperation.op
        else:
            return None










