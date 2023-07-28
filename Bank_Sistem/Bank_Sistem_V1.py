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
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor_deposito = int(input("Qual o valor do deposito? "))
        if valor_deposito >= 0:
            saldo += valor_deposito
        else:
            print("Valor inválido")
            
    elif opcao == "2": 
        print(f"Seu saldo é {saldo}")
        if saldo <= 0:
            print("Não é possível sacar você nao tem saldo em conta!")
        else:
            while numero_saques < LIMITE_SAQUES:
                saques = int(input("Digite o valor para o saque: "))
                numero_saques +=1
                if saques > 500:
                    print("Valor inválido! O limite para saque é de R$500,00")
    
    elif opcao == "3":
        print(f"""
              ===EXTRATO===
              Valor depositado: {valor_deposito}
              Numeros de saques realizados: {numero_saques}
              Valor total sacado: {saques}
              Saldo Atual: {saldo:.2f}              
              """)
                
    elif opcao == "4":
        break
    else:
        print("Opção Inválida! Tente novamente!")