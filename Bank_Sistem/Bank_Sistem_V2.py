def depositar(saldo, valor_deposito, extrato, opcao):
    while opcao == "1":
        
        valor_deposito = float(input("Qual o valor do deposito? "))
        
        if valor_deposito >= 0:
            saldo += valor_deposito
        
            print("\nDeposito Realizado!\n")
        
            opcao = input("Deseja fazer outro deposito? [1]sim [2]nao\n")
        
            extrato += f"Deposito: R${valor_deposito:.2f}\n"
        else:
        
            print("Valor inválido")
    
    return saldo, extrato, opcao


def saque(saldo, saques_total, opcao, numero_saques, LIMITE_SAQUES, extrato):
    while numero_saques <= LIMITE_SAQUES and opcao == "2":

        saques = float(input("Digite o valor para o saque: "))

        if saques > 500 or saques < 0:
            print("Valor inválido!\nO limite para saque é de R$500,00")

        else:
            print("\nSaque Realizado!\n")

            opcao = input(f"Você tem {LIMITE_SAQUES - numero_saques} saques restantes. \n[2]Fazer outro [0]Sair\n")

            numero_saques += 1

            extrato += f"Saque: R${saques:.2f}\n"

            saques_total += saques

    return saldo, saques_total, opcao, numero_saques, extrato


def mostrar_extrato(saldo, saques_total, numero_saques, extrato):
    print(f"========EXTRATO========")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"Números de saques realizados: {numero_saques-1}")
    print(f"Saldo Atual: R${(saldo-saques_total):.2f}")
    print("========================")


def novo_usuario(usuarios):
    cpf = input("Digite o CPF: ")

    usuario = filtro_user(cpf, usuarios)

    if usuario:
        print("Essa pessoa já está cadastrada!")
        return

    print("Preencha as informações abaixo")

    nome = input("Nome: ")
    data = input("Data de nascimento: ")
    cpf = input("CPF: ")
    print("Endereço:")
    endereco = ""
    endereco += input("Estado: ")
    endereco += input("Cidade: ")
    endereco += input("Bairro: ")
    endereco += input("Logradouro: ")

    usuarios.append({"nome": nome, "data": data, "cpf": cpf, "endereco": endereco})

    print("Usuário Cadastrado com Sucesso!!!")


def filtro_user(cpf, usuarios):
    user_filter = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

    return user_filter[0] if user_filter else None


def conta_corrente(agencia, numero_conta, usuarios):
    cpf = input("Digite o CPF: ")

    usuario = filtro_user(cpf, usuarios)

    if usuario:
        print("Conta Criada com Sucesso!!!")

        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Não foi possível encontrar esse usuário")


def main():
    menu = '''
    Escolha uma Opção: 
    [1] Depositar
    [2] Sacar
    [3] Ver Extrato
    [4] Criar Novo Usuário
    [5] Criar Conta Corrente
    [6] Sair
    '''

    saldo = 0
    extrato = ""
    numero_saques = 1
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saques_total = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            saldo, extrato, opcao = depositar(saldo, 0, extrato, opcao)

        elif opcao == "2":
            print(f"Seu saldo é R${saldo:.2f}")
            saldo, saques_total, opcao, numero_saques, extrato = saque(saldo, saques_total, opcao, numero_saques, LIMITE_SAQUES, extrato)

        elif opcao == "3":
            mostrar_extrato(saldo, saques_total, numero_saques, extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = conta_corrente(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "6":
            break

        else:
            print("Opção Inválida! Tente novamente!")

main()
