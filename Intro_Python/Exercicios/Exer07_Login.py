#Login com While
USUARIO = "Lucca"
SENHA = "minha_senha123"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login == USUARIO and senha == SENHA:
        print("Logado com sucesso, Lucca!")
        break
    else:
        print("Login ou senha inválidos, tente novamente!")
        