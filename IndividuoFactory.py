from Individuo import Individuo
from abc import ABC, abstractmethod


class IndividuoFactory(ABC):

    @abstractmethod
    def get_individuo(self) -> Individuo:
        pass
