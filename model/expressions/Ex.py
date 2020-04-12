# Expression is an interface for all the expressions types
class Expression:
    def evaluate(self, x):
        raise NotImplementedError("this method is not implemented at this level see the documentation")

    def __repr__(self):
        raise NotImplementedError("this method is not implemented at this level see the documentation")

class Constant(Expression):
    
    def __init__(self, value):
        self.value = float(value)

    def evaluate(self, x=0):
        return self.value

    def __repr__(self):
        return "%d" % self.value

class Variable(Expression):
    def __init__(self):
        pass

    def evaluate(self, x=0):
        return float(x)

    def __repr__(self):
        return "x"