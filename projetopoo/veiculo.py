class Veiculo:
    def __init__(self, nome, capacidade, velocidade_maxima):
        self._nome = nome
        self._capacidade = capacidade
        self._velocidade_maxima = velocidade_maxima

    def exibir_informacoes(self):
        return f"Nome: {self._nome}, Capacidade: {self._capacidade} pessoas, Velocidade Máxima: {self._velocidade_maxima} km/h"

    def mover(self):
        return f"{self._nome} está se movendo."

    def parar(self):
        return f"{self._nome} está parando."

