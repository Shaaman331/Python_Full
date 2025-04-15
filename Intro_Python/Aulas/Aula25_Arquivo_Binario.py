import pickle
x = [1,2,3,4]

print(pickle.dumps(x))

"""
Nesse exemplo, o objeto meu_objeto é serializado usando o método dumps() do pickle. 
O resultado é uma sequência de bytes que pode ser armazenada ou transmitida.
"""
# Crie um objeto
meu_objeto = {'nome': 'João', 'idade': 30}

# Serializar o objeto
serializado = pickle.dumps(meu_objeto)

# Imprima o objeto serializado
print(serializado)

# Deserializar o objeto
deserializado = pickle.loads(serializado)

# Imprima o objeto deserializado
print(deserializado)

#Uma forma mais complexa de serializar objetos

print()

# Crie um objeto
meu_objeto = {'nome': 'João', 'idade': 30}

# Abra um arquivo em modo de escrita binária
with open('meu_objeto.pkl', 'wb') as arquivo:
    # Serializar o objeto e salve no arquivo
    pickle.dump(meu_objeto, arquivo)

# Abra o arquivo em modo de leitura binária
with open('meu_objeto.pkl', 'rb') as arquivo:
    # Deserializar o objeto do arquivo
    deserializado = pickle.load(arquivo)

# Imprima o objeto deserializado
print(deserializado)

print()

# Defina uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

# Crie um objeto da classe
pessoa = Pessoa("João", 30)

# Serializar o objeto
serializado = pickle.dumps(pessoa)

# Imprima o objeto serializado
print("Objeto serializado:")
print(serializado)

# Deserializar o objeto
deserializado = pickle.loads(serializado)

# Imprima o objeto deserializado
print("\nObjeto deserializado:")
print(deserializado)

# Verifique se o objeto deserializado é uma instância da classe Pessoa
print("\nÉ uma instância da classe Pessoa?")
print(isinstance(deserializado, Pessoa))

# Acesse os atributos do objeto deserializado
print("\nAtributos do objeto deserializado:")
print(deserializado.nome)
print(deserializado.idade)

# Defina uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

# Crie um objeto da classe
pessoa = Pessoa("João", 30)

# Serializar o objeto
serializado = pickle.dumps(pessoa)

# Imprima o objeto serializado
print("Objeto serializado:")
print(serializado)

# Deserializar o objeto
deserializado = pickle.loads(serializado)

# Imprima o objeto deserializado
print("\nObjeto deserializado:")
print(deserializado)

# Verifique se o objeto deserializado é uma instância da classe Pessoa
print("\nÉ uma instância da classe Pessoa?")
print(isinstance(deserializado, Pessoa))

# Acesse os atributos do objeto deserializado
print("\nAtributos do objeto deserializado:")
print(deserializado.nome)
print(deserializado.idade)

print()
# Defina uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"

# Crie um objeto da classe
pessoa = Pessoa("João", 30)

# Abra um arquivo em modo de escrita binária
with open('pessoa.pkl', 'wb') as arquivo:
    # Serializar o objeto e salve no arquivo
    pickle.dump(pessoa, arquivo)

# Abra o arquivo em modo de leitura binária
with open('pessoa.pkl', 'rb') as arquivo:
    # Deserializar o objeto do arquivo
    deserializado = pickle.load(arquivo)

# Imprima o objeto deserializado
print("Objeto deserializado:")
print(deserializado)

# Verifique se o objeto deserializado é uma instância da classe Pessoa
print("\nÉ uma instância da classe Pessoa?")
print(isinstance(deserializado, Pessoa))

# Acesse os atributos do objeto deserializado
print("\nAtributos do objeto deserializado:")
print(deserializado.nome)
print(deserializado.idade)