# this class provide N random cards
# it uses a singleton dp
# to prevent multiple instanciation
from __future__ import annotations
from random import randrange
from typing import Optional

from assets.Constantes import Config

class SingletonMeta(type):
    _instance: Optional[CardsProvider] = None

    # def __call__(self) -> CardsProvider:
    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class CardsProvider(metaclass=SingletonMeta):
    def __init__(self):
        self.cards = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 25, 25, 50, 50, 75, 75, 100, 100]

    def getRandomCards(self, numberOfCards=Config().NUMBER_OF_CARDS):
        mySet = set()
        myCards = list()
        while len(mySet) != numberOfCards:
            rand = randrange(0, len(self.cards))
            mySet.add(rand)
        for x in mySet:
            myCards.append(self.cards[x])
        return myCards


# if __name__ == "__main__":
#     provider = CardsProvider()
#     provider2 = CardsProvider()
#     if id(provider) == id(provider2):
#         print(" same same")
#     print(provider.getRandomCards())
