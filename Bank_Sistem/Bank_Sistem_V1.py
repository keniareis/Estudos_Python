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
            valor_deposito = int(input("Qual o valor do deposito? "))
            if valor_deposito >= 0:
                saldo += valor_deposito
                print("\nDeposito Realizado!\n")
                opcao = input("Deseja fazer outro deposito? [1]sim, [2]nao\n")
            else:
                print("Valor inválido")
                
    elif opcao == "2": 
        print(f"Seu saldo é {saldo:.2f}\n")
        
        if saldo <= 0:
            print("Não é possível sacar você nao tem saldo em conta!")
        else:
            while numero_saques < LIMITE_SAQUES and opcao == "2":
                saques = int(input("Digite o valor para o saque: "))
                
                if saques > 500 or saques < 0:
                    print("Valor inválido! O limite para saque é de R$500,00")
                else:
                    opcao = input(f"Você tem {LIMITE_SAQUES-numero_saques} restantes. [2]Fazer outro [0]Sair\n")
                
                saques_total += saques
                numero_saques +=1
    
    elif opcao == "3":
        print(f"""
              ===EXTRATO===
              Valor depositado: {saldo:.2f}
              Numeros de saques realizados: {numero_saques-1}
              Valor total sacado: {saques_total:.2f}
              Saldo Atual: {(saldo-saques_total):.2f}              
              """)
                
    elif opcao == "4":
        break
  
    else:
        print("Opção Inválida! Tente novamente!")