from veiculo import Veiculo

class Navio(Veiculo):
    def __init__(self, nome, capacidade, velocidade_maxima, tipo):
        super().__init__(nome, capacidade, velocidade_maxima)
        self.tipo = tipo

    def mover(self):
        return f"O navio {self._nome} está navegando no mar."

    def parar(self):
        return f"O navio {self._nome} está reduzindo a velocidade e lançando a âncora."

    def ancorar(self):
        return f"O navio {self._nome} está ancorado com sucesso."