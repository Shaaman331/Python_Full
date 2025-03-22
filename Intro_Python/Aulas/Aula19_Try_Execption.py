n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))
try:
    print(n1/n2)
except:
    print("Erro ao dividir")
finally:
    print("Finalizado")

print()

try:
    z = int(input("Digit3 um numero: "))
    print(5/z)
except ValueError:
    print("Digite um numero inteiro")
except ZeroDivisionError:
    print("Nao digite 0")
