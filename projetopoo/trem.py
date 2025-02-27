from veiculo import Veiculo

class Trem(Veiculo):
    def __init__(self, nome, capacidade, velocidade_maxima, tipo):
        super().__init__(nome, capacidade, velocidade_maxima)
        self.tipo = tipo  # Tipo de trem (ex: carga, passageiro)

    def mover(self):
        return f"O trem {self._nome} está seguindo nos trilhos."

    def parar(self):
        return f"O trem {self._nome} está freando e parando."

    def diminuir_fumaca(self):
        return f"O trem {self._nome} diminuiu a fumaça."
