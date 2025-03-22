#Raise você pode especificar o tipo de exceção que deseja lançar e uma mensagem de erro associada.

def soma(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError("Não é possível somar números negativos")
    return n1 + n2
print(soma(5, -3))  

print()

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero!")
    return a / b

#Assert é usado para verificar se uma condição é verdadeira. Se a condição for falsa, o programa lançará uma exceção do tipo AssertionError.

z = 5
assert z >0, f"O valor {z} não é positivo"  
print(z)
print()

def soma(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "Os argumentos devem ser números!"
    return a + b
