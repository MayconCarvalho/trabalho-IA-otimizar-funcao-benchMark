from Individuo import Individuo
from numpy import zeros
from numpy import random
from numpy import where
from numpy import sin
from numpy import pi


class LevyInd(Individuo):

    def __init__(self, d: int, rand=True):
        super().__init__(-1)
        self.__d = d
        self.__genes = [random.uniform(-10, 10) for _ in range(d)]
        self.__calcExec = False

    def recombinar(self, ind):
        corte: int = random.randint(1, self.__d - 1)
        F1 = LevyInd(self.__d, False)
        F2 = LevyInd(self.__d, False)

        genes = zeros(self.__d, dtype=int)
        for i in range(0, corte):
            genes[i] = self.__genes[i]

        for i in range(corte, self.__d):
            if ind.get_genes()[i] not in genes:
                genes[i] = ind.get_genes()[i]

        for i in range(self.__d):
            if i + 1 not in genes:
                index = where(genes == 0)
                genes[index[0][0]] = i + 1
        F1.__genes = genes

        genes = zeros(self.__d, dtype=int)
        for i in range(0, corte):
            genes[i] = ind.get_genes()[i]

        for i in range(corte, self.__d):
            if self.get_genes()[i] not in genes:
                genes[i] = self.get_genes()[i]

        for i in range(self.__d):
            if i + 1 not in genes:
                index = where(genes == 0)
                genes[index[0][0]] = i + 1
        F2.__genes = genes
        ret = [F1, F2]
        return ret

    def mutar(self):
        mut = LevyInd(self.__d, False)
        ind1 = random.randint(self.__d)
        ind2 = random.randint(self.__d)

        while ind2 == ind1:
            ind2 = random.randint(self.__d)

        genesAux = self.__genes
        genesAux[ind1], genesAux[ind2] = genesAux[ind2], genesAux[ind1]
        mut.__genes = genesAux

        return mut

    def get_avaliacao(self) -> float:
        if self.__calcExec is False:
            self._avaliacao = sin(pi * self.w_i(1)) ** 2
            for i in range(1, self.__d - 1):
                self._avaliacao += (self.w_i(i) - 1) ** 2 * (1 + 10 * sin(pi * self.w_i(i) + 1) ** 2)
                self._avaliacao += (self.w_i(self.__d) - 1) ** 2 * (1 + sin(2 * pi * self.w_i(self.__d)))

        return self._avaliacao

    def get_genes(self):
        return self.__genes

    def w_i(self, i) -> float:
        return 1 + (self.__genes[i] - 1) / 4

    def __add__(self, other) -> float:
        if not isinstance(other, float):
            other = float(other.get_avaliacao())

        if self.get_avaliacao() != 0 and other != 0:
            return 1. / self._avaliacao + 1. / other
        elif self.get_avaliacao() != 0 and other == 0:
            return 1. / self._avaliacao
        elif self.get_avaliacao() == 0 and other != 0:
            return 1. / other
        else:
            return 0.0

    def __lt__(self, other):
        return self.get_avaliacao() < other.get_avaliacao()

    def __str__(self):
        return f'avaliacao: {self._avaliacao}, ' \
               f'genes: {self.__genes}'
