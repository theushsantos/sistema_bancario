
"""
- criar funções para as operações:
  1: sacar
  2: depositar
  3: visualizar histórico

- criar 2 novas funções para:
  1: criar usuário
  2: criar conta corrente (vinculada ao usuário)

- função saque:
  1: deve receber argumentos por nome(keyword only)
    sugestão: saldo, valor, extrato,limite, numero saques, limite saques
    sugestão retorno: saldo e extrato

- função deposito:
  1: receber argumentos apenas por posição (positional only)
    sugestão: saldo, valor. extrato
    sugestão de retorno: saldo e extrato

- função extrato:
  1: receber os argumentos por nome e posição
    s. posicionas: saldo
    s. nomeados: extrato

- funções criar usuário e criar conta

- Criar usuário:
  1: armazenar os usuários em uma lista
  2: dado de nome, data de nascimento, cpf(somente os números, não pode ter mais de um usuário com o mesmo numero) e endereço(string: logradoro - numero - bairro - cidade/sigla do estado)

- Criar conta corrente:
  1: armazenar contas em uma lista
  2: dados da conta: agencia, numero e usuário
  3: numero da conta deve ser sequencial iniciado por 1
  4: numero da agencia é fixo "0001"
  5: um usuário pode ter mais de uma conta mas uma conta não pode ter mais de um usuário

"""
import usuarios

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
        print("Contas...")
        continue
    elif opcao == 6:
        usuarios.listar_usuarios_cadastrados(usuarios.users)
        voltar = input("\nVoltar\n=> ")       
    elif opcao == 7:
        print("Contas...")
    elif opcao == 8:
        print('saindo...')
        break
    else:
        print("Ops! opção selecionada inválida")
        continue
