from .ComplexEX import ComplexExpression


class BinaryExpression(ComplexExpression):
    def __init__(self, left, op, right):
        ComplexExpression.__init__(self, op)
        if left is None or right is None:
            raise ArithmeticError("illegal argument")
        self.left = left
        self.right = right
        self.op = op

    def evaluate(self, x=0):
        return self.op.evaluate(self.left.evaluate(x), self.right.evaluate(x))

    def __repr__(self):
        return "({0}{1}{2})".format(self.left, self.op, self.right)
