menu = (f"""
{" SISTEMA BANCARIO ".center(24,"=")}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=>""")

valor_saque = 0
valor_deposito = 0
saldo = 0
limite = 500

extrato = """"""

numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Quanto deseja depositar? "))
        if(valor_deposito <= 0):
            valor_deposito = 0
            print("Ops! valor do deposito menor que o permitido")
        else:
            saldo += valor_deposito
            extrato += (f"\nMovimento de deposito:  + R$ {valor_deposito:.2f} ")
            print("Deposito realizado com Sucesso! Valor R$ {:.2f} ".format(valor_deposito))


    elif opcao == 2:

        if(numero_saques == LIMITE_SAQUES):
            print("Você excedeu a quantidade de saques por dia!")

        else:
            valor_saque = float(input("Quanto deseja sacar? "))
            if saldo == 0.0:
                print(f"não será possivel sacar! Saldo: R$ {saldo:.2f}")
            elif(valor_saque > limite):
                print("Você excedeu o valor maximo de saque!")
            elif(valor_saque > saldo):
                print("Saldo é insuficiente, tente um valor menor!")
            elif(valor_saque <= 0.0):
                print("Ops! valor é menor ou igual a zero, tente com um valor maior")
            else:
                numero_saques += 1
                saldo = saldo - valor_saque
                extrato += (f"\nMovimento de saque:     - R$ {valor_saque:.2f}")
                print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso")

    elif opcao == 3:

        print("{}".format(" EXTRATO ".center(36,"=")))
        if(extrato == ""):
            print("Não possui nenhuma movimentação!")
        else:
            print(extrato)
        print("\nSaldo:                    R$ {:.2f}".format(saldo))
        print("{}".format(" FIM ".center(36,"=")))

    elif opcao == 4:
        print("Saindo...")
        break
    
    else:
        print("Ops! opção selecionada inválida")
        continue
