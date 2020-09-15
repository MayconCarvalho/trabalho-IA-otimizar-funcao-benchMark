from functools import reduce
from numpy import random

from IndividuoFactory import IndividuoFactory


class FGA:

    def executar(nPop: int, nGeracoes: int, nElite: int, indFact: IndividuoFactory):
        # criando a população inicial com genes aleatorios
        popInicial = [indFact.get_individuo() for _ in range(nPop)]

        for g in range(1, nGeracoes + 1):
            # criando a lista filhos por recombinação e adicionando na lista
            filhos = []
            for i in range(0, nPop if nPop % 2 == 0 else nPop - 1, 2):
                filhos += popInicial[i].recombinar(popInicial[i + 1])

            # caso a nPop seja impar, escolhe aleatoriamente outro individuo
            # e gera mais um filho com o ultimo pai
            if nPop % 2 == 1:
                filhos += popInicial[nPop - 1].recombinar(popInicial[random.randint(nPop)])

            # criado a lista de mutantes e adicionado na lista
            mutantes = []
            for i in popInicial:
                mutantes.append(i.mutar())

            # contanenando todas as listas de individuos
            aux = popInicial + filhos + mutantes

            # calculando a avaliacao de cada individuo e ordenando a lista
            aux.sort()

            # criado lista de nova populacao (newPop)
            newPop = []

            # adicionando os individuos de elite na lista newPop
            j = 0
            while len(newPop) < nElite:
                if aux[j] not in newPop:
                    newPop.append(aux[j])
                aux.pop(j)

            # roleta viciada adicionado os outros individuos na lista
            while len(newPop) < nPop:
                # soma das avaliacoes de todos os individuos
                soma = 0
                for i in aux:
                    aval = i.get_avaliacao()
                    soma += 1. / aval if aval != 0 else 0
                # valor aleatorio gerado pela roleta
                r = random.random()
                roleta = r * soma
                roletaParcial = 0
                j = 0
                # buscando elemento a ser inserido na nova lista usando roleta
                while roletaParcial < roleta:
                    if aux[j].get_avaliacao() != 0:
                        roletaParcial += 1. / aux[j].get_avaliacao()
                    j += 1

                if j == len(aux):
                    j -= 1

                if aux[j] not in newPop:
                    newPop.append(aux[j])

                aux.pop(j)

            popInicial = newPop
            popInicial.sort()
            print(f'Nº geração: {g}', end=' | ')
            print(f'Melhor individuo: \'{popInicial[0]}\'')
