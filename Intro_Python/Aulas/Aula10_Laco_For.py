#Laço for com intervalos 
for i in range(2, 100, 2):
    print(i)

for x in range(100, 0, -1):
    print(x)

for z in range(1, 100, -2):
    print(z)

#Lista em range
print(list( range(0,100,3)))

#Laço for exibindo lista nome
n = input("Digite seu nome: ")
for i in n:
    print(i)
    
#Laço Aninhado
for c in range(0, 3):
    for d in range(0, 3):
        print(f"c = {c} e d = {d}")
    