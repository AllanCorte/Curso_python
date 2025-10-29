from functools import reduce
import math  # Importa o módulo math para funções matemáticas
print('oi')  # Exemplo de print simples

# =======================
# MÉTODOS DE STRING
# =======================
texto = " Python é legal! "
print(texto.strip())      # strip() remove espaços do início e fim da string
print(texto.lower())      # lower() deixa tudo minúsculo
print(texto.upper())      # upper() deixa tudo maiúsculo
print(texto.capitalize())  # capitalize() deixa só a primeira letra maiúscula
print(texto.replace("legal", "incrível"))  # replace() troca partes do texto
print(texto.split())      # split() divide a string em uma lista de palavras
# join() junta elementos de uma lista em uma string
print("-".join(["a", "b", "c"]))

# =======================
# MÉTODOS DE LISTA
# =======================
lista = [3, 1, 2]
lista.append(4)           # append() adiciona um elemento no final da lista
lista.insert(0, 0)        # insert() adiciona na posição indicada
lista.remove(1)           # remove() remove o primeiro elemento igual ao valor
print(lista.pop())        # pop() remove e retorna o último elemento
print(lista.sort())       # sort() ordena a lista (modifica a lista original)
print(sorted(lista))      # sorted() retorna uma nova lista ordenada
print(lista.count(2))     # count() conta quantas vezes o valor aparece
print(lista.index(2))     # index() retorna o índice do valor

# =======================
# MÉTODOS DE TUPLA
# =======================
tupla = (1, 2, 3, 2)
print(tupla.count(2))   # count() conta quantas vezes 2 aparece
print(tupla.index(3))   # index() retorna o índice do valor 3

# =======================
# MÉTODOS DE DICIONÁRIO
# =======================
d = {"a": 1, "b": 2}
print(d.keys())           # keys() retorna as chaves do dicionário
print(d.values())         # values() retorna os valores
print(d.items())          # items() retorna tuplas (chave, valor)
print(d.get("a"))         # get() retorna o valor da chave (ou None)
d.update({"c": 3})        # update() adiciona/atualiza pares chave-valor

# =======================
# MÉTODOS DE CONJUNTO (set)
# =======================
s = {1, 2, 3}
s.add(4)                  # add() adiciona elemento
s.remove(2)               # remove() remove elemento
print(s.union({5, 6}))    # union() retorna a união de conjuntos
print(s.intersection({3, 4}))  # intersection() retorna a interseção

# =======================
# OUTROS MÉTODOS ÚTEIS
# =======================
print(len(lista))         # len() retorna o tamanho da lista/string
print(type(texto))        # type() mostra o tipo do objeto
print(isinstance(texto, str))  # isinstance() verifica se é de um tipo

# enumerate() retorna índices e valores de uma lista
for i, valor in enumerate(lista):
    print(i, valor)

# range() cria uma sequência de números
for i in range(5):
    print(i)

# zip() junta listas em pares
for a, b in zip([1, 2], ["a", "b"]):
    print(a, b)

# =======================
# FUNÇÕES EM PYTHON
# =======================


def saudacao(nome):
    """Função simples que imprime uma saudação."""
    print(f'Olá, {nome}!')


def soma(a, b=0):
    """Função com valor padrão para o parâmetro b."""
    return a + b


def argumentos_nomeados(x, y, z=0):
    """Função com argumentos nomeados e valor padrão."""
    print(x, y, z)


def funcao_varios_args(*args, **kwargs):
    """
    *args: recebe vários argumentos posicionais (tupla)
    **kwargs: recebe vários argumentos nomeados (dicionário)
    """
    print('args:', args)
    print('kwargs:', kwargs)


# Função anônima (lambda) - função rápida, geralmente para usar em uma linha
def soma_lambda(x, y): return x + y


print(soma_lambda(2, 3))  # Exemplo de uso da função lambda

# List comprehension (cria listas de forma compacta)
quadrados = [x**2 for x in range(5)]  # Cria lista de quadrados de 0 a 4
print(quadrados)

# =======================
# TRATAMENTO DE ERROS
# =======================
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Não pode dividir por zero!")  # Captura erro de divisão por zero

# =======================
# IMPORTAÇÃO DE MÓDULOS
# =======================
print(math.sqrt(16))  # sqrt() calcula a raiz quadrada

# =======================
# POO - CLASSES E OBJETOS
# =======================


class Pessoa:
    """Classe simples com construtor e método."""

    def __init__(self, nome, idade):
        # self.nome e self.idade são atributos do objeto
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        # Método que imprime uma apresentação
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')

# Herança: Cliente herda de Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome, idade)  # Chama o construtor da classe mãe
        self.saldo = saldo

    def mostrar_saldo(self):
        print(f'Saldo: {self.saldo}')

# Propriedades (getter/setter)


class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @property
    def preco(self):
        # Getter: retorna o preço
        return self._preco

    @preco.setter
    def preco(self, valor):
        # Setter: só permite preço >= 0
        if valor >= 0:
            self._preco = valor


# Exemplo de uso de classes:
p1 = Pessoa('Maria', 30)
p1.apresentar()

c1 = Cliente('João', 40, 1000)
c1.apresentar()
c1.mostrar_saldo()

produto = Produto('Caneta', 2.5)
print(produto.preco)
produto.preco = 3.0
print(produto.preco)

# map: aplica uma função a cada item da lista
print(list(map(lambda x: x*2, [1, 2, 3])))

# filter: filtra itens de acordo com uma condição
print(list(filter(lambda x: x > 1, [1, 2, 3])))

# reduce: reduz uma lista a um único valor
print(reduce(lambda x, y: x + y, [1, 2, 3]))

# DICA: Consulte sempre a documentação oficial do Python para mais detalhes!
