from .Ex import Expression

class ComplexExpression(Expression):
    def __init__(self,op):
        if op is None :
            raise ArithmeticError(" no a valid Operator")
