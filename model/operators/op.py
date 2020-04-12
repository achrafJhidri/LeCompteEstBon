#this is an interface for any Operator type
class Operator:
    def __repr__(self):
        raise NotImplementedError("not implemented at this level")
    
class BinaryOp(Operator):
    def __repr__(self):
        raise NotImplementedError("not implemented at this level")
    
    def evaluate(self , left , right):
        raise NotImplementedError("not implemented at this level")
    
class UnaryOp(Operator):
    def __repr__(self):
        raise NotImplementedError("not implemented at this level")
    
    def evaluate(self , argument):
        raise NotImplementedError("not implemented at this level")
    
