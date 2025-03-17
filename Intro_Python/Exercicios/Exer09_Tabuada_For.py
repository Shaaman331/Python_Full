#Tabuada com laço for

n1 = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{n1} x {i} = {n1 * i}")


print()

#Tabuada com laço for e range com 10 passos de 1 em 1
for a in range(1, 11):
    print(f"==========Tabuada {a}==========")
    for b in range(1, 11):
        print(f"{a} x {b} = {a * b}")
        

