"""
Programação Orientada a Objetos (POO) em Python

A Programação Orientada a Objetos (POO) é um paradigma de programação que 
organiza o código em objetos que possuem propriedades e métodos. 
Em Python, a POO é uma das principais características da linguagem.

Conceitos básicos

Classe: Uma classe é um modelo que define as propriedades e métodos de um objeto. É como um molde que define a estrutura e o comportamento de um objeto.
Objeto: Um objeto é uma instância de uma classe. É uma entidade que possui propriedades e métodos definidos pela classe.
Atributo: Um atributo é uma propriedade de um objeto. É uma variável que é definida dentro de uma classe ou objeto.
Método: Um método é uma função que é definida dentro de uma classe ou objeto. É uma ação que pode ser executada em um objeto
"""

# Exemplo de classe e objeto em Python
#Exemplo 1: Classe e Objeto

# Defina uma classe chamada "Carro"
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} {self.ano}"

# Crie um objeto chamado "meu_carro" da classe "Carro"
meu_carro = Carro("Fiat", "Uno", 2015)

# Acesse os atributos do objeto
print(meu_carro.marca)  # Saída: Fiat
print(meu_carro.modelo)  # Saída: Uno
print(meu_carro.ano)  # Saída: 2015

# Execute o método "descricao" do objeto
print(meu_carro.descricao())  # Saída: Fiat Uno 2015

#Exemplo 2: Herança

# Defina uma classe chamada "Veiculo"
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} {self.ano}"

# Defina uma classe chamada "Carro" que herda de "Veiculo"
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas):
        super().__init__(marca, modelo, ano)
        self.portas = portas

    def descricao(self):
        return f"{super().descricao()} com {self.portas} portas"

# Crie um objeto chamado "meu_carro" da classe "Carro"
meu_carro = Carro("Fiat", "Uno", 2015, 4)

# Acesse os atributos do objeto
print(meu_carro.marca)  # Saída: Fiat
print(meu_carro.modelo)  # Saída: Uno
print(meu_carro.ano)  # Saída: 2015
print(meu_carro.portas)  # Saída: 4

# Execute o método "descricao" do objeto
print(meu_carro.descricao())  # Saída: Fiat Uno 2015 com 4 portas


#Polimorfismo
# Defina uma classe chamada "Forma"
class Forma:
    def area(self):
        pass

# Defina uma classe chamada "Circulo" que herda de "Forma"
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2

# Defina uma classe chamada "Retangulo" que herda de "Forma"
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Crie objetos de "Circulo" e "Retangulo"
circulo = Circulo(5)
retangulo = Retangulo(4, 6)

# Execute o método "area" dos objetos
print(circulo.area())  # Saída: 78.5
print(retangulo.area())  # Saída: 24

"""
Encapsulamento

O encapsulamento é o conceito de ocultar os detalhes internos de uma classe e expor apenas o que é necessário. 
Isso é feito usando modificadores de acesso, como público, protegido e privado.



"""

# Defina uma classe chamada "ContaBancaria"
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saque inválido.")

    def obter_saldo(self):
        return self.__saldo

# Crie um objeto da classe "ContaBancaria"
minha_conta = ContaBancaria("João")

# Realize operações na conta
minha_conta.depositar(100)  # Saída: Depósito de 100 realizado com sucesso.
minha_conta.sacar(50)  # Saída: Saque de 50 realizado com sucesso.
print(minha_conta.obter_saldo())  # Saída: 50

