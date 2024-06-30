users = [
    {
        'nome': 'nome',
        'data_nascimento': 'dd/mm/aaaa',
        'cpf':00000000000,
        'endereco':'logradouro-numero-bairro-cidade/estado'
    }
]

def valida_cpf(num_cpf,lista_usuarios):
    
    valida = False
    for usuario in lista_usuarios:
        valida = (num_cpf == usuario.get('cpf'))
        if(valida):
           return False, '00000000000', 'não incluído'
    return True, num_cpf,'CPF incluido'
            
    
def set_data():
    print("{}".format(" data(DD/MM/AAAAA) ".center(36,"-")))

    dia = int(input("Dia(DD): "))
    while(dia <= 0 or dia > 30):
        print('\nOps! Modelo de data incorreto!\nTente Novamente!\n')
        dia = int(input("Dia(DD): "))

    mes = int(input("Mes(MM): "))
    while(mes <= 0 or mes > 12):
        print('\nOps! Modelo de data incorreto!\nTente Novamente!\n')
        mes = int(input("Mes(MM): "))

    ano = int(input("Ano(AAAA): "))
    while(ano < 1900 or len(str(ano)) > 4):
        print('\nOps! Modelo de data incorreto!\nTente Novamente!\n')
        ano = int(input("Ano(AAAA): "))

    data = str(f'{dia}/{mes}/{ano}')
    

    return data



def dados_endereco():
    print("{}".format(" ENDEREÇO ".center(36,"-")))
    logradouro = input("Logradouro: ")
    numero = input('Numero: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado(ES): ')
    print("{}".format("".center(36,"-")))
    endereco = f'{logradouro}-{numero}-{bairro}-{cidade}/{estado}'
    return endereco

def listar_usuarios_cadastrados(lista):

    print("\n=----------------------=\n")
    for user in lista[1::]:
        for chave,valor in user.items():
            print(f"{chave}: {valor}")
        print("\n=----------------------=\n")
 

    
def cadastro_de_usuarios():
    global users
    continuar = True
    while(continuar):

        print("{}".format(" CADASTRO USUÁRIO ".center(36,"=")))

        usr_nome = str(input("Nome: ")).strip()
        usr_cpf = int(input("CPF(00000000000): "))

        while(len(str(usr_cpf)) < 11 or len(str(usr_cpf)) > 11):
            print("\nOps!CPF invalido, tente novamente\n")
            usr_cpf = int(input("CPF(00000000000): "))

        cpf_valido, usr_cpf, mensagem_valida_cpf = valida_cpf(usr_cpf,users) 

        if(cpf_valido):

            print(f"\n{mensagem_valida_cpf}!\n")

            usr_data_nascimento= set_data()
            usr_endereco = dados_endereco().strip('')

            class_user = {
                'nome': usr_nome,
                'data_nascimento': usr_data_nascimento,
                'cpf':usr_cpf,
                'endereco':usr_endereco.split('-')
            }

            users.append(class_user)
            print("\nINCLUIDO COM SUCESSO!\n")
            for chave,valor in class_user.items():
                print(f'{chave} : {valor}')
            print("{}".format("".center(36,"-")))

        else:
            print(f"{mensagem_valida_cpf}!\nCPF já cadastrado na lista!")
            
        print("{}".format("".center(36,"=")))

        print("1 - Continuar cadastrando\n2 - Sair")
        continuar = True if int(input("=> ")) == 1 else False



    
