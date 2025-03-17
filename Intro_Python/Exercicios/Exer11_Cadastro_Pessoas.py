#Faça um programa de cadastro de usuarios, nome , idade, email e telefone.

pessoas = []
while True:
    decisao = int(input("Digite 1 para cadastrar , 2 para sair: "))
    if decisao == 2:
        break
    elif decisao == 1:
        nome = input("Digite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")
        telefone = input("Digite o telefone: ")
        pessoas.append({"nome":nome,"idade":idade,"email":email,"telefone":telefone})
        print("Usuario cadastrado com sucesso!")
        
    else:
        print("Opção invalida!")
