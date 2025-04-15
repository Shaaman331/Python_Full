arquivo = open("pessoas.txt", "a")
i = 0   
while True:
    if i >4:
        break
    arquivo.write(input("Digite seu nome: ") + "\n")
    i += 1
