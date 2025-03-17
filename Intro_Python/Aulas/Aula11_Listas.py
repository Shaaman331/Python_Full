#Listas
nomes = ["Lucca","Raquel","Joao"]
print(type(nomes))
print(nomes[0])
nomes[0] = "Luis"
print(nomes)

#Adicionar valor na ultima posicao da lista
nomes.append("Maria")
print(nomes)

nomes.append("Rosana")
print(nomes)

#Adicionar valor em uma posicao especifica da lista
while True:
    nome = input("Digite -1 para sair ou cadastre um nome: ")
    if nome == "-1":
        break
    nomes.append(nome)
    print(nomes)

#Inserir valor na lista
nomes.insert(0,"Luis")
print(nomes)

nomes01 = ["Lucca","Raquel","Joao", "Maria", "Rosana"]
print(nomes01.index("Lucca"))
nome.pop(nomes01.index("Raquel"))
print(nomes01)
nomes01.sort()
print(nomes01)

#Ordenar lista
num = [3, 2, 1, 5, 27, 1.5, 49, 43, 54, 37, 6, 10]
num.sort()
print(num)

#Ordenar lista em ordem decrescente
num.sort(reverse=True)
print(num)

num_ordenados = sorted(num)
print(num_ordenados)


