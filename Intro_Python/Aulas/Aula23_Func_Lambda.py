import os
"""
Uma função lambda em Python é uma função anônima, ou seja, 
uma função que não tem um nome. Ela é definida com a palavra-chave lambda 
e é usada para criar funções pequenas e simples.
Onde argumentos é uma lista de variáveis que serão passadas para a função, 
e expressão é o código que será executado quando a função for chamada.

"""

soma = lambda x, y: x + y
print(soma(2, 3))  # imprime 5


numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # imprime [2, 4]




nomes = ['João', 'Maria', 'Pedro']
nomes_maiusculos = list(map(lambda x: x.upper(), nomes))
print(nomes_maiusculos)  # imprime ['JOÃO', 'MARIA', 'PEDRO']


import functools
numeros = [1, 2, 3, 4, 5]
soma = functools.reduce(lambda x, y: x + y, numeros)
print(soma)  # imprime 15


classificacao = lambda nota: 'Aprovado' if nota >= 7 else 'Reprovado'
print(classificacao(8))  # imprime 'Aprovado'
print(classificacao(5))  # imprime 'Reprovado'


quadrado = lambda x: x ** 2
print(quadrado(4))  # imprime 16
