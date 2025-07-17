"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC , abstractmethod

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor

class Cliente(Pessoa):
    def __init__(self, nome, idade, conta):
        super().__init__(nome, idade)
        self.conta = conta

class Conta(ABC):
    def __init__(self, agencia, numero_da_conta, saldo):
        self.agencia = agencia
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(Conta):
    def __init__(self, agencia, numero_da_conta, saldo, limite):
        super().__init__(agencia, numero_da_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            return True
        return False

class ContaPoupanca(Conta):
    def __init__(self, agencia, numero_da_conta, saldo):
        super().__init__(agencia, numero_da_conta, saldo)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

class Banco:
    def __init__(self, agencias):
        self.agencias = agencias
        self.contas = []
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)
        self.contas.append(cliente.conta)

    def autentificar(self, cliente, conta):
        if (
            conta.agencia in self.agencias and
            cliente in self.clientes and
            conta in self.contas
        ):
            return True
        return False

# Exemplo de uso
conta1 = ContaCorrente(348, 4365, 10, 100)
cliente1 = Cliente('allan', 24, conta1)

conta2 = ContaPoupanca(24, 365, 103)
cliente2 = Cliente('fabi', 22, conta2)

banco = Banco([348, 24])

banco.adicionar_cliente(cliente1)
banco.adicionar_cliente(cliente2)

if banco.autentificar(cliente1, conta1):
    conta1.deposito(4)
    conta1.sacar(13)
    print(conta1.saldo)