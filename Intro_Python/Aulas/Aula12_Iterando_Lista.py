idades  = [2, 4, 6, 8, 10, 20, 25, 30, 50, 10]

#x = list(enumerate(idades))

for i, j in enumerate(idades):
    print(f'Posição: {i}, Valor: {j}')

idades_pares = []

for idade in idades:
    if idade % 2 == 0:
        idades_pares.append(idade)
print(idades_pares)


