from LevyIndFactory import LevyIndFactory
from FGA import FGA

if __name__ == '__main__':
    d = 4
    nPop = 40
    nGeracoes = 10
    nElite = 6
    indFact = LevyIndFactory(d)
    FGA.executar(nPop, nGeracoes, nElite, indFact)

