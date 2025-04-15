"""
Herança Multipla
Herança múltipla é um recurso da programação orientada a objetos (POO) que permite que uma classe herde atributos e métodos de mais de uma classe pai. 
Em Python, a herança múltipla é suportada e pode ser útil em certos casos, mas também pode levar a ambiguidades e conflitos se não for usada com cuidado.
"""

class Animal:
    def andar(self):
        print("Estou andando como um animal...")

    def correr(self):
        print("Estou correndo como um animal...")
    
    def pular(self):
        print("Estou pulando como um animal...")

class Felino(Animal):
    def felino(self):
        print("Sou um felino...")

class Gato(Felino, Animal):
    def miar(self):
        print("Estou miando...")
    
class Cachorro(Animal):
    def latir(self):
        print("Estou latindo...")


y = Gato()
y.andar()
y.correr()
y.pular()
y.miar()

"""
Nesse exemplo, a classe Cachorro herda os atributos e métodos de Animal e Mamífero. 
A ordem de inicialização das classes pai é importante, pois a classe Cachorro precisa chamar os construtores (__init__) das classes pai na ordem correta.
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Mamifero:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mamar(self):
        print(f"{self.nome} está mamando.")

class Cachorro(Animal, Mamifero):
    def __init__(self, nome, idade, raça):
        Animal.__init__(self, nome)
        Mamifero.__init__(self, nome, idade)
        self.raça = raça

    def latir(self):
        print(f"{self.nome} está latindo.")

cachorro = Cachorro("Beto", 3, "Vira-lata")
cachorro.comer()  # imprime "Beto está comendo."
cachorro.mamar()  # imprime "Beto está mamando."
cachorro.latir()  # imprime "Beto está latindo."


"""
Agora, suponha que as classes pai Animal e Mamífero tenham um método com o mesmo nome, comer:
"""

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Mamifero:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def comer(self):
        print(f"{self.nome} está comendo leite.")

class Cachorro(Animal, Mamifero):
    def __init__(self, nome, idade, raça):
        Animal.__init__(self, nome)
        Mamífero.__init__(self, nome, idade)
        self.raça = raça

cachorro = Cachorro("Beto", 3, "Vira-lata")
cachorro.comer()  # qual método será chamado?


