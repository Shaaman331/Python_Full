"""
Geradores em Python são uma forma de criar iteradores, 
que são objetos que permitem iterar sobre uma sequência 
de valores sem precisar carregar todos os valores na memória ao mesmo tempo. 
Isso é especialmente útil quando se trabalha com grandes conjuntos de dados ou quando se precisa de uma forma eficiente de gerar uma sequência de valores.

Um gerador é uma função que usa a palavra-chave yield para produzir uma série de resultados, 
em vez de usar return para produzir um único resultado.

"""

def meu_gerador():
    yield 1
    yield 2
    yield 3

for valor in meu_gerador():
    print(valor)

print()

def pares():
    i = 0
    while True:
        yield i
        i += 2

for _ in range(10):
    print(next(pares()))



print()

def primos():
    def é_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    i = 2
    while True:
        if é_primo(i):
            yield i
        i += 1

for _ in range(10):
    print(next(primos()))



