#Notas do aluno com While
while True:
    nota_aluno = int(input("Digite nota do aluno: "))
    if nota_aluno >= 0 and nota_aluno <= 10:
        print(f"Nota do aluno armazenada com sucesso: {nota_aluno}")
        break
    print("Nota invalida digite novamente")
