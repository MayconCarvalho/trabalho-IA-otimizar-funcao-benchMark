from LevyIndFactory import LevyIndFactory
from FGA import FGA

if __name__ == '__main__':
    rainhas = 9
    nPop = 40
    nGeracoes = 10
    nElite = 6
    indFact = LevyIndFactory(rainhas)
    FGA.executar(nPop, nGeracoes, nElite, indFact)

