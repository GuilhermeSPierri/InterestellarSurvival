from abc import ABC, abstractmethod


class GameObjectFactory(ABC):
    @abstractmethod
    def criar_objeto(self, x, y):
        pass