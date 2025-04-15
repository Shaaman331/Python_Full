class Pessoas:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def logar_sistema(self):
        print(f"Olá {self.nome}, você está logado no sistema")
        return self

    @classmethod 
    def criar_funcionario(cls, nome, idade, sexo, cargo):
        return cls(nome, idade, sexo)
    

    @staticmethod
    def e_adulto(idade):
        if idade >= 18:
            return True
        return False
    

        
p1 = Pessoas("Tarcisio", 35, "M")
p1.logar_sistema()
p2 = Pessoas.criar_funcionario("João", 30, "M", "Gerente")
p2.logar_sistema()
print(Pessoas.e_adulto(21))


"""
Para criar um método de classe em Python, você pode usar o decorador @classmethod. Aqui está um exemplo de como você pode criar um método de classe
para classe Pessoas:

O parâmetro `cls` é uma referência à classe em que o método é chamado. Ele é usado para criar uma nova instância da classe.
Com isso, você pode criar instâncias das classes `Pessoas` e `Funcionarios` de forma mais elegante e flexível.

O decorador @staticmethod é usado em Python para definir um método estático em uma classe. Um método estático é um método que pertence à classe em si, 
e não a uma instância da classe.

"""
