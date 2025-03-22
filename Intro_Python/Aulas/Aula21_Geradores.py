from pympler.asizeof import asizeof

"""
sys.getsizeof() é uma função do módulo sys em Python que retorna o tamanho em bytes de um objeto. Isso pode ser útil para entender como o Python aloca memória para diferentes tipos de dados.
"""


# Exemplo 1: Tamanho de um inteiro
x = 10
print(asizeof(x))  # Saída: 28 (ou 24, dependendo da plataforma)

# Exemplo 2: Tamanho de uma string
y = "Olá, mundo!"
print(asizeof(y))  # Saída: 50 (ou 46, dependendo da plataforma)

# Exemplo 3: Tamanho de uma lista
z = [1, 2, 3, 4, 5]
print(asizeof(z))  # Saída: 120 (ou 112, dependendo da plataforma)

# Exemplo 4: Tamanho de um dicionário
w = {"nome": "João", "idade": 30}
print(asizeof(w))  # Saída: 240 (ou 224, dependendo da plataforma)

# Exemplo 5: Tamanho de uma lista com objetos
v = [object() for _ in range(10)]
print(asizeof(v))  # Saída: 560 (ou 528, dependendo da plataforma)

def dobro(lista):
    lista_dobro = []
    for i in lista:
        lista_dobro.append(i*2)
        return lista_dobro
X = asizeof(dobro(range(0, 100)))
print(X)  # Saída: 560 (ou 528, dependendo da plataforma)
print()


