from abc import ABC, ABCMeta, abstractproperty,abstractclassmethod
from datetime import datetime

class Cliente:
    def __init__(self,endereco) -> None:
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self, conta):
        self._contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self,nome, data_nascimento,cpf,endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

class Conta:
    def __init__(self,numero,cliente) -> None:
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente:Cliente,numero):
        return cls.Conta(numero,cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico
        
    def sacar(self,valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
    
    def deposito(self,valor):

        if valor >0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        return False       

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saque=3) -> None:
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("@@@ Operação falhou! O valor do saque excedeu o limite. @@@")
            
        elif excedeu_saques:
            print("@@@ Operação falhou! Excedeu a quantidade de saques diario. @@@")
        
        else:
            return super().sacar(valor)
        
        return False

    def __str__(self):
        return f"""
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    
class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M::%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self,conta):
        pass

class Deposito(Transacao):
    def __init__(self,valor) -> None:
        self._valor=valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        sucesso_trasacao = conta.depositar(self.valor)

        if sucesso_trasacao:
            conta.historico.adicionar_transacao(self)   

class Saque(Transacao):
    def __init__(self,valor) -> None:
        self._valor=valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
