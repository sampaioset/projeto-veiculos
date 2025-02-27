from navio import Navio
from helicoptero import Helicoptero
from trem import Trem
from aviao import Aviao

def main():
    # Criando instâncias dos veículos
    navio = Navio("Titanic", 3000, 40, "cruzeiro")
    helicoptero = Helicoptero("Apache", 5, 300, 4)
    trem = Trem("Expresso Polar", 800, 200, "passageiro")
    aviao = Aviao("Boeing 747", 660, 900, "Latam")

    # Exibindo informações e testando métodos
    print(navio.exibir_informacoes())
    print(navio.mover())
    print(navio.parar())  # Chamando parar() antes de ancorar
    print(navio.ancorar())

    print(helicoptero.exibir_informacoes())
    print(helicoptero.mover())
    print(helicoptero.parar())  # Chamando parar() antes de pousar
    print(helicoptero.pousar())

    print(trem.exibir_informacoes())
    print(trem.mover())
    print(trem.parar())  # Chamando parar() antes de diminuir a fumaça
    print(trem.diminuir_fumaca())

    print(aviao.exibir_informacoes())
    print(aviao.mover())
    print(aviao.parar())  # Chamando parar() antes de aterrissar
    print(aviao.aterrissar())

if __name__ == "__main__":
    main()
