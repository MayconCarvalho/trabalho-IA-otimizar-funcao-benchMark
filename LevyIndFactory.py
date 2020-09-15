from IndividuoFactory import IndividuoFactory
from LevyInd import LevyInd


class LevyIndFactory(IndividuoFactory):

    def __init__(self, d):
        self.__d = d

    def get_individuo(self) -> LevyInd:
        return LevyInd(self.__d)
