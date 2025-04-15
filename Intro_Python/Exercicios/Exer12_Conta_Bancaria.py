"""
Agora, vamos criar uma interação com o usuário para que ele possa realizar operações na conta bancária.

O código é um sistema de conta bancária simples que permite ao usuário realizar operações de depósito, 
saque e verificação de saldo. 
Aqui está uma explicação detalhada do código:
"""
# Defina uma classe chamada "ContaBancaria"
"""
A classe ContaBancaria é responsável por gerenciar a conta bancária do usuário. 
Ela tem os seguintes atributos e métodos:
- Atributos: saldo (saldo atual da conta), deposito (valor do depósito), saque (valor do saque)

__init__: O método de inicialização da classe, que é chamado quando um objeto da classe é criado. 
Ele recebe o nome do titular da conta e o saldo inicial (opcional).

depositar: O método que realiza o depósito de um valor na conta. 
Ele verifica se o valor é positivo e, se sim, adiciona o valor ao saldo da conta.

sacar: O método que realiza o saque de um valor da conta. 
Ele verifica se o valor é positivo e se o saldo da conta é suficiente para realizar o saque. 
Se sim, subtrai o valor do saldo da conta.

obter_saldo: O método que retorna o saldo atual da conta.

"""
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de {valor} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso.")
        else:
            print("Saque inválido.")

    def obter_saldo(self):
        return self.__saldo

"""
Função main

A função main é a função principal do programa, que é chamada quando o programa é executado. 
Ela é responsável por:

Exibir uma mensagem de boas-vindas ao usuário.
Perguntar ao usuário o nome do titular da conta.
Criar um objeto da classe ContaBancaria com o nome do titular da conta.
Exibir um menu de opções ao usuário, que inclui:
Depositar
Sacar
Ver saldo
Sair
Processar a opção escolhida pelo usuário e realizar a ação correspondente.
"""
def main():
    print("Bem-vindo ao sistema de conta bancária!")

    # Pergunte ao usuário o nome do titular da conta
    titular = input("Digite o nome do titular da conta: ")

    # Crie um objeto da classe "ContaBancaria"
    minha_conta = ContaBancaria(titular)

    while True:
        print("\nOpções:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver saldo")
        print("4. Sair")

        # Pergunte ao usuário a opção desejada
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            # Pergunte ao usuário o valor a depositar
            valor = float(input("Digite o valor a depositar: "))
            minha_conta.depositar(valor)
        elif opcao == "2":
            # Pergunte ao usuário o valor a sacar
            valor = float(input("Digite o valor a sacar: "))
            minha_conta.sacar(valor)
        elif opcao == "3":
            # Exiba o saldo atual
            print(f"Saldo atual: {minha_conta.obter_saldo()}")
        elif opcao == "4":
            # Sair do sistema
            print("Obrigado por usar o sistema de conta bancária!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()

"""
Estrutura de Controle

A estrutura de controle do programa é baseada em um loop while que continua até que o usuário escolha a opção de sair. 
Dentro do loop, o programa exibe o menu de opções e processa a opção escolhida pelo usuário.
"""