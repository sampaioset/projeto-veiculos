# Projeto Veículos - Programação Orientada a Objetos (POO)

## Descrição do Projeto

Este projeto foi desenvolvido para demonstrar os conceitos de **Programação Orientada a Objetos (POO)**, utilizando os pilares fundamentais: **Herança**, **Polimorfismo** e **Encapsulamento**.

O objetivo deste projeto é simular a movimentação e a parada de diferentes tipos de veículos (Navio, Helicóptero, Trem e Avião), onde cada um herda características da classe principal `Veiculo`, mas com comportamentos específicos de cada tipo de veículo.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

- **`veiculo.py`**: Define a classe base `Veiculo`, que contém atributos e métodos comuns a todos os veículos.
- **`navio.py`**: Subclasse de `Veiculo`, representando um navio, com métodos específicos como ancorar e navegar.
- **`helicoptero.py`**: Subclasse de `Veiculo`, representando um helicóptero, com métodos como voar e pousar.
- **`trem.py`**: Subclasse de `Veiculo`, representando um trem, com métodos como buzinar e diminuir a fumaça.
- **`aviao.py`**: Subclasse de `Veiculo`, representando um avião, com métodos como decolagem e aterrissagem.
- **`main.py`**: Arquivo principal onde instanciamos os veículos, chamamos os métodos e exibimos os resultados no terminal.

## Conceitos de POO Aplicados
### Herança
As classes **`navio.py`**, **`helicoptero.py`**, **`trem.py`** e **`aviao.py`**  herdam os atributos e métodos da classe Veiculo. Isso permite que todos os veículos compartilhem comportamentos comuns, mas também possuam comportamentos exclusivos.

### Polimorfismo
O método `mover()`  foi sobrescrito em cada subclasse, assim como o método `parar()`. Cada tipo de veículo possui um comportamento específico para o movimento, mesmo utilizando o mesmo nome de método.

### Encapsulamento
Os atributos como `nome`, `capacidade` e `velocidade_maxima` são protegidos **`(com um underscore _)`**, e só podem ser acessados por meio de métodos públicos como **`exibir_informacoes()`**, garantindo a proteção e controle sobre os dados.

## Conclusão
Este projeto demonstra como a Programação Orientada a Objetos pode ser aplicada de maneira prática, utilizando conceitos de Herança, Polimorfismo e Encapsulamento para criar uma simulação de diferentes tipos de veículos com comportamentos distintos.


