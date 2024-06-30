
"""
- Criar conta corrente:
  1: armazenar contas em uma lista
  2: dados da conta: agencia, numero e usuário
  3: numero da conta deve ser sequencial iniciado por 1
  4: numero da agencia é fixo "0001"
  5: um usuário pode ter mais de uma conta mas uma conta não pode ter mais de um usuário

"""

import usuarios

bc_numero_conta = 0
bc_contas = []
bc_usuarios = usuarios.users

usuario_padrao = {}

bc_dd_conta = {
    'agencia': '0001',
    'numero': bc_numero_conta,
    'usuario': usuario_padrao
}

bc_contas.append(bc_dd_conta)

def linha():
    return f'\n{"{}".format("".center(36,"-"))}'

def rlc_usuario_conta(num_conta,*,usuario):
    num_conta += 1

    dd_conta = {
        'agencia': '0001',
        'numero': num_conta,
        'usuario': usuario
    }

    return num_conta, dd_conta

def exibir_dados(dd_conta):
    for chave,valor in dd_conta.items():
        if(chave == 'usuario'):
            print(linha())
            print(f'\nDados do {chave}:\n')
            for chave_user,valor_user in valor.items():
                print(f'{chave_user} : {valor_user}')
        else:
            print("\nDados da conta: \n")
            print(f'{chave} : {valor}')

def listar_contas_cadastradas():
    global bc_contas

    print(f'{"{}".format(" CONTAS CADASTRADAS ".center(48,"-"))}')
    for dd_conta in bc_contas[1:]:
          exibir_dados(dd_conta)
          print(f'{"{}".format("".center(48,"-"))}')
    

def get_usuario(num_cpf,*,usuarios):
    cpf_user = {}
    for usuario in usuarios:
        print(usuario)
        cpf_user = usuario.get('cpf')
        if cpf_user == num_cpf:
            return usuario
        
    return False


def criar_conta():
    global bc_contas, bc_usuarios,bc_numero_conta
    menu = f'''
{"{}".format(" CADASTRO ".center(48,"="))}
{"{}".format(" CONTA CORRENTE ".center(48,"-"))}

(1) - Cadastrar usuario e conta
(2) - Cadastrar Conta
(3) - Voltar

OBS: para cadastrar conta basta digitar o numero do seu CPF,
     caso ainda não tenha cadastro de usuario digite (1), para
     proceguir digite (2).
    
=>'''
    while(True):

        opcao_menu = int(input(menu))

        if(opcao_menu == 1):
            usuarios.cadastro_de_usuarios()
        elif(opcao_menu == 3):
            break
        elif(opcao_menu != 2):
            continue

        print(f'\n{"{}".format("".center(36,"-"))}')

        num_cpf = int(input('Numero CPF => '))

        dd_usuario = get_usuario(num_cpf,usuarios = bc_usuarios)

        if(dd_usuario):
            bc_numero_conta, dd_conta = rlc_usuario_conta(bc_numero_conta,usuario = dd_usuario)
            bc_contas.append(dd_conta)

            print(f"Conta Incluida!\n{linha()}\nDados da conta:\n")
            exibir_dados(dd_conta)

        else:
            print('usuario não encontrado, conta não cadastrada!')





