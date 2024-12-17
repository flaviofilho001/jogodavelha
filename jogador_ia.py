# -*- coding: utf-8 -*-
from random import randint
from jogador import Jogador
from tabuleiro import Tabuleiro

class JogadorIA(Jogador):
    def __init__(self, tabuleiro: Tabuleiro, tipo: int):
        super().__init__(tabuleiro, tipo)

    def getJogada(self) -> (int, int):
        adversario = Tabuleiro.JOGADOR_X if self.tipo == Tabuleiro.JOGADOR_0 else Tabuleiro.JOGADOR_0

        # R1: Verifica se pode ganhar ou bloquear o adversário
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    # Testa marcando o local para verificar vitória
                    self.matriz[l][c] = self.tipo
                    if self.tabuleiro.tem_campeao() == self.tipo:
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = adversario
                    if self.tabuleiro.tem_campeao() == adversario:
                        self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                        return (l, c)
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO

        # R2: Verifica se pode criar duas sequências de duas marcações
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    self.matriz[l][c] = self.tipo
                    sequencias = 0
                    for i in range(3):
                        # Conta sequências possíveis
                        if self.__conta_linha(i) == 2:
                            sequencias += 1
                        if self.__conta_coluna(i) == 2:
                            sequencias += 1
                    if self.__conta_diagonal_principal() == 2:
                        sequencias += 1
                    if self.__conta_diagonal_secundaria() == 2:
                        sequencias += 1
                    self.matriz[l][c] = Tabuleiro.DESCONHECIDO
                    if sequencias >= 2:
                        return (l, c)

        # R3: Verifica se o centro está livre
        if self.matriz[1][1] == Tabuleiro.DESCONHECIDO:
            return (1, 1)

        # R4: Verifica se o adversário marcou um canto e tenta marcar o oposto
        cantos = [(0, 0), (0, 2), (2, 0), (2, 2)]
        for canto, oposto in zip(cantos, reversed(cantos)):
            if self.matriz[canto[0]][canto[1]] == adversario and self.matriz[oposto[0]][oposto[1]] == Tabuleiro.DESCONHECIDO:
                return oposto

        # R5: Verifica se há um canto vazio
        for canto in cantos:
            if self.matriz[canto[0]][canto[1]] == Tabuleiro.DESCONHECIDO:
                return canto

        # R6: Escolhe um quadrado arbitrariamente
        lista = []
        for l in range(3):
            for c in range(3):
                if self.matriz[l][c] == Tabuleiro.DESCONHECIDO:
                    lista.append((l, c))

        if len(lista) > 0:
            p = randint(0, len(lista) - 1)
            return lista[p]
        else:
            return None

    # Funções auxiliares para contar sequências
    def __conta_linha(self, linha):
        return sum(1 for v in self.matriz[linha] if v == self.tipo)

    def __conta_coluna(self, coluna):
        return sum(1 for linha in range(3) if self.matriz[linha][coluna] == self.tipo)

    def __conta_diagonal_principal(self):
        return sum(1 for i in range(3) if self.matriz[i][i] == self.tipo)

    def __conta_diagonal_secundaria(self):
        return sum(1 for i in range(3) if self.matriz[i][2 - i] == self.tipo)
