# this class provides the configuration constants
# it uses a singleton dp
# to prevent multiple instanciation
from __future__ import annotations

from tkinter.font import Font
from typing import Optional


class SingletonMeta(type):
    _instance: Optional[Config] = None

    # def __call__(self) -> CardsProvider:
    def __call__(self):
        if self._instance is None:
            self._instance = super().__call__()
        return self._instance


class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.NUMBER_OF_CARDS = 6
        self.MIN   = 100
        self.MAX = 999




