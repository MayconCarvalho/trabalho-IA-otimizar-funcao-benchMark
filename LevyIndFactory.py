from IndividuoFactory import IndividuoFactory
from LevyInd import LevyInd


class LevyIndFactory(IndividuoFactory):

    def __init__(self, genes):
        self.__genes = genes

    def get_individuo(self) -> LevyInd:
        return LevyInd(self.__genes)
