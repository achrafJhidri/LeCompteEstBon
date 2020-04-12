from .op import BinaryOp


EPSYLON = 1e-9


class Plus(BinaryOp):
    def __init__(self):
        pass
    
    def evaluate(self , left , right):
        return left+right
    
    def __repr__(self):
        return "+"

    @staticmethod
    def isValid(left, right):
        return True

class Multi(BinaryOp):
    def __init__(self):
        pass
    
    def evaluate(self , left , right):
        return left*right
    
    def __repr__(self):
        return "*"

    @staticmethod
    def isValid(left, right):
         return left != 1 and right != 1
    
class Minus(BinaryOp):
    def __init__(self):
        pass
    
    def evaluate(self , left , right):
        return left-right
    
    def __repr__(self):
        return "-"
    @staticmethod
    def isValid(left, right):
         return left > right
class Divide(BinaryOp):
    def __init__(self):
        pass
    
    def evaluate(self , left , right):
        if right - 0 < EPSYLON :
            raise ArithmeticError(" division by 0")
        return int(left / right)
    
    def __repr__(self):
        return "/"

    @staticmethod
    def isValid(left, right):
         return left > right > 1 and left % right == 0 #avoiding division by 0 ( it's not possible ) && by 1 for the actuel project x/1 is x so i don't this kind of
    