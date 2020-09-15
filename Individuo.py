from abc import ABC, abstractmethod


class Individuo(ABC):

    def __init__(self, avaliacao):
        self._avaliacao = avaliacao

    @abstractmethod
    def recombinar(self, ind):
        pass

    @abstractmethod
    def mutar(self):
        pass

    @abstractmethod
    def get_avaliacao(self):
        pass
