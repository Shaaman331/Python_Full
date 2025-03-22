def soma_numeros(n1, n2):
    print(n1 + n2)
soma_numeros(n1=5, n2 = 2)
    

def soma_numeros01(n1, n2, *args):
    print(f"n1 = {n1} n2 = {n2} args = {args}")

soma_numeros01(1,2,3,4,5,6,7,8)


def soma_numeros02(*args):
    soma = 0
    for valor in args:
        soma = soma + valor
        print(soma)

soma_numeros02(1, 2, 3, 4, 5, 6, 7, 8)

def soma_numeros03(**kwargs):
    x = kwargs.get('x', 1)
    y = kwargs.get('y', 0)
    print(x + y)


    def soma_numeros04(**kwargs):
        x = kwargs.get("test1")
        if x:
            print("Foi passado")
        else:
            print("Não foi passado")
        
        soma_numeros04("test1")
    soma_numeros04()

print()

def soma_numeros05(n1, n2):
    soma = n1 + n2
    if soma > 5:
        return soma
    print("To aqui")
    
soma = soma_numeros05(5,2)
print(soma)





