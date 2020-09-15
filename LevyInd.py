from Individuo import Individuo
from numpy import zeros
from numpy import random
from numpy import sin
from numpy import pi


class LevyInd(Individuo):

    def __init__(self, d: int, rand=True):
        super().__init__(-1)
        self.__d = d
        self.__calcExec = False

        if rand:
            self.__genes = [random.uniform(-10, 10) for _ in range(d)]
        else:
            self.__genes = zeros(d, dtype=float)

    def recombinar(self, ind):
        alpha = 0.33
        f1 = LevyInd(self.__d, False)
        f2 = LevyInd(self.__d, False)

        for i in range(self.__d):
            f1[i] = (1 - alpha) * self.__genes[i] + alpha * ind.get_genes()[i]
            f2[i] = (1 - alpha) * self.__genes[i] + alpha * ind.get_genes()[i]

        return [f1, f2]

    def mutar(self):
        mutou = False
        mut = LevyInd(self.__d, False)
        for i in range(self.__d):
            num = random.rand()
            if num < 0.1:
                num = self.__genes[i] + random.normal()
                mut[i] = num if -10 < num < 10 else -10 if num < -10 else 10
                mutou = True
            else:
                mut[i] = self.__genes[i]

        if mutou is False:
            j = random.randint(0, self.__d)
            num = self.__genes[j] + random.normal()
            mut[j] = num if -10 < num < 10 else -10 if num < -10 else 10

        return mut

    def get_avaliacao(self) -> float:
        if self.__calcExec is False:
            self._avaliacao = sin(pi * self.w_i(0)) ** 2
            for i in range(0, self.__d - 2):
                self._avaliacao += (self.w_i(i) - 1) ** 2 * (1 + 10 * sin(pi * self.w_i(i) + 1) ** 2)
                self._avaliacao += (self.w_i(self.__d - 1) - 1) ** 2 * (1 + sin(2 * pi * self.w_i(self.__d - 1)) ** 2)

        return self._avaliacao

    def get_genes(self):
        return self.__genes

    def w_i(self, i) -> float:
        return 1 + (self.__genes[i] - 1) / 4

    def __setitem__(self, key, value):
        self.__genes[key] = value

    def __getitem__(self, item):
        return self.__genes[item]

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
        return self.get_avaliacao() <= other.get_avaliacao()

    def __str__(self):
        return f'avaliacao: {self._avaliacao}, ' \
               f'genes: {self.__genes}'
