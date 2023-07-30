menu = '''
Escolha uma Opção: 
[1] Depositar
[2] Sacar
[3] Ver Extrato
[4] Sair
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3
saques_total = 0

while True:
    opcao = input(menu)
    
    if opcao == "1":
        
        while opcao == "1":

            valor_deposito = float(input("Qual o valor do deposito? "))

            if valor_deposito >= 0:
                saldo += valor_deposito

                print("\nDeposito Realizado!\n")

                opcao = input("Deseja fazer outro deposito? [1]sim [2]nao\n")

                extrato += f"Deposito: R${valor_deposito:.2f}\n"

            else:
                print("Valor inválido")
                
    elif opcao == "2": 
        print(f"Seu saldo é R${saldo:.2f}")
        
        if saldo <= 0:
            print("Não é possível sacar você nao tem saldo em conta!")

        else:
            while numero_saques <= LIMITE_SAQUES and opcao == "2":

                saques = float(input("Digite o valor para o saque: "))
                
                if saques > 500 or saques < 0:
                    print("Valor inválido! \nO limite para saque é de R$500,00")

                else:
                    print("\nSaque Realizado!\n")
                    opcao = input(f"Você tem {LIMITE_SAQUES-numero_saques} saques restantes. \n[2]Fazer outro [0]Sair\n")
                    numero_saques +=1
                    extrato += f"Saque: R${saques:.2f}\n"
                    saques_total += saques


    
    elif opcao == "3":
        
        print(f"========EXTRATO========")     
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Numeros de saques realizados: {numero_saques-1}")
        print(f"Saldo Atual: R${(saldo-saques_total):.2f}")              
        print("========================")
                
    elif opcao == "4":
        break
  
    else:
        print("Opção Inválida! Tente novamente!")