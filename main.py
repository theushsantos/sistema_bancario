import usuarios,conta_corrente

def mostrar_extrato(saldo_total,/,*, __extrato):
    print("{}".format(" EXTRATO ".center(36,"=")))
    if(__extrato == ""):
        print("Não possui nenhuma movimentação!")
    else:
        print(__extrato)
    print("\nSaldo:                    R$ {:.2f}".format(saldo_total))
    print("{}".format(" FIM ".center(36,"=")))

def realizar_deposito(valor, saldo_total,grava_extrato,/):
    texto = ""
    if(valor <= 0):
        valor= 0
        texto = "Ops! valor do deposito menor que o permitido"
    else:
        saldo_total += valor
        grava_extrato += f"\nMovimento de deposito:  + R$ {valor:.2f} "
        texto = "Deposito realizado com Sucesso! Valor R$ {:.2f} ".format(valor)
    return texto, saldo_total, grava_extrato

def realizar_saque(*,valor, saldo_total,num_saques,grava_extrato,valor_maximo):
    if saldo == 0.0:
        texto = (f"não será possivel sacar! Saldo: R$ {saldo:.2f}")
    elif(valor > valor_maximo):
        texto = ("Você excedeu o valor maximo de saque!")
    elif(valor > saldo_total):
        texto = ("Saldo é insuficiente, tente um valor menor!")
    elif(valor <= 0.0):
        texto = ("Ops! valor é menor ou igual a zero, tente com um valor maior")
    else:
        num_saques += 1
        saldo_total -= valor
        grava_extrato += (f"\nMovimento de saque:     - R$ {valor:.2f}")
        texto = (f"Saque no valor de R${valor:.2f} realizado com sucesso")
    
    return texto, num_saques, saldo_total, grava_extrato
    

menu = (f"""
{" SISTEMA BANCARIO ".center(24,"=")}

[1] Depositar
[2] Sacar
[3] Extrato
[4] Cadastrar usuários
[5] Cadastrar Conta
[6] Listar usuários
[7] Listar Contas
[8] Sair

=>""")

valor_saque = 0
valor_deposito = 0
saldo = 0
qtd_saques = 0

extrato = """"""

valor_max_transacao = 500 
LIMITE_SAQUES = 3


while True:
    
    opcao = int(input(menu))

    if opcao == 1:

        valor_deposito = float(input("Quanto deseja depositar? "))
        mensagem_retorno_deposito, saldo, extrato = realizar_deposito(valor_deposito, saldo, extrato)
        print(mensagem_retorno_deposito)


    elif opcao == 2:

        if(qtd_saques == LIMITE_SAQUES):
            print("Você excedeu a quantidade de saques por dia!")

        else:
            valor_saque = float(input("Quanto deseja sacar? "))
            mensagem_retorno_saque, qtd_saques, saldo, extrato = realizar_saque(valor=valor_saque,
                                                                                saldo_total=saldo,
                                                                                num_saques=qtd_saques,
                                                                                grava_extrato=extrato,
                                                                                valor_maximo=valor_max_transacao)
            print(mensagem_retorno_saque)
            

    elif opcao == 3:
        mostrar_extrato(saldo,__extrato=extrato) 
        voltar = input("\nVoltar\n=> ")      

    elif opcao == 4:
        usuarios.cadastro_de_usuarios()
        continue
    elif opcao == 5:
        conta_corrente.criar_conta()
        continue
    elif opcao == 6:
        usuarios.listar_usuarios_cadastrados(usuarios.users)
        voltar = input("\nVoltar\n=> ")       
    elif opcao == 7:
        conta_corrente.listar_contas_cadastradas()
        voltar = input("\nVoltar\n=> ")
    elif opcao == 8:
        print('saindo...')
        break
    else:
        print("Ops! opção selecionada inválida")
        continue
