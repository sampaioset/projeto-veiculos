from veiculo import Veiculo

class Aviao(Veiculo):
    def __init__(self, nome, capacidade, velocidade_maxima, companhia):
        super().__init__(nome, capacidade, velocidade_maxima)
        self.companhia = companhia

    def mover(self):
        return f"O avião {self._nome} da {self.companhia} está decolando."

    def parar(self):
        return f"O avião {self._nome} está ativando os freios e taxiando até o portão."

    def aterrissar(self):
        return f"O avião {self._nome} aterrissou com sucesso."
