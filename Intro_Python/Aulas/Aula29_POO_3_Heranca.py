class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

class Vendedor(Pessoa):
    def __init__(self, nome, idade, sexo, salario, comissao):
        super().__init__(nome, idade, sexo)
        self.salario = salario
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario + (self.comissao * 0.1)

    def calcular_comissao(self):
        return self.comissao * 0.1

    def cadastrar_vendedor(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"Salário: {self.salario}")
        print(f"Comissão: {self.comissao}")
        print(f"Salário Total: {self.calcular_salario()}")
        print(f"Comissão Total: {self.calcular_comissao()}")

nome = input("Digite o nome do vendedor: ")
idade = int(input("Digite a idade do vendedor: "))
sexo = input("Digite o sexo do vendedor (M/F): ")
salario = float(input("Digite o salário do vendedor: "))
comissao = float(input("Digite a comissão do vendedor: "))

v1 = Vendedor(nome, idade, sexo, salario, comissao)
v1.cadastrar_vendedor()



class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando um produto.")

class Cliente(Pessoa):
    def comprar(self):
        print(f"{self.nome} está comprando um produto.")

class Cliente(Pessoa):
    def comprar(self, produto):
        print(f"{self.nome} está comprando o produto {produto}.")

c1 = Cliente("Maria", 25, "Feminino")
produto = input("Digite o produto que deseja comprar: ")
c1.comprar(produto)  # Saída: Maria está comprando o produto <produto>.

c2 = Cliente("João", 30, "Masculino")  # Exemplo de criação de outro cliente
produto = input("Digite o produto que deseja comprar: ")
c2.comprar(produto)  # Saída: João está comprando o produto <produto>.

"""
Herança em Python é um conceito fundamental da programação orientada a objetos (POO) que permite que uma classe herde atributos e métodos de outra classe. 
A classe que herda é chamada de "classe filha" ou "subclasse", enquanto a classe de onde a herança é feita é chamada de "classe pai" ou "superclasse".

A herança é útil para criar uma hierarquia de classes, onde as classes filhas compartilham características comuns com a classe pai, 
mas também podem ter suas próprias características específicas.
"""

