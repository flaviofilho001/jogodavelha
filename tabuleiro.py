class Tabuleiro:
    DESCONHECIDO = 0
    JOGADOR_0 = 1
    JOGADOR_X = 4

    def __init__(self):
        self.matriz = [
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
            [Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO, Tabuleiro.DESCONHECIDO],
        ]

    def tem_campeao(self):
        # Verifica linhas e colunas
        for i in range(3):
            if self.matriz[i][0] == self.matriz[i][1] == self.matriz[i][2] != Tabuleiro.DESCONHECIDO:
                return self.matriz[i][0]  # Retorna o vencedor da linha
            if self.matriz[0][i] == self.matriz[1][i] == self.matriz[2][i] != Tabuleiro.DESCONHECIDO:
                return self.matriz[0][i]  # Retorna o vencedor da coluna

        # Verifica diagonais
        if self.matriz[0][0] == self.matriz[1][1] == self.matriz[2][2] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][0]  # Retorna o vencedor da diagonal principal
        if self.matriz[0][2] == self.matriz[1][1] == self.matriz[2][0] != Tabuleiro.DESCONHECIDO:
            return self.matriz[0][2]  # Retorna o vencedor da diagonal secundária

        # Nenhum vencedor encontrado
        return Tabuleiro.DESCONHECIDO
