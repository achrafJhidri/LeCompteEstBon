



class Card :
    def __init__(self,value):
        self.used = False
        self.value = value


    def toggleUse(self):
        self.used=not self.used

    def isUsed(self):
        return self.used
