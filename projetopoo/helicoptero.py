from veiculo import Veiculo

class Helicoptero(Veiculo):
    def __init__(self, nome, capacidade, velocidade_maxima, autonomia_voo):
        super().__init__(nome, capacidade, velocidade_maxima)
        self.autonomia_voo = autonomia_voo

    def mover(self):
        return f"O helicóptero {self._nome} está voando."

    def parar(self):
        return f"O helicóptero {self._nome} está reduzindo a rotação das hélices e pousando."

    def pousar(self):
        return f"O helicóptero {self._nome} pousou com sucessor."
