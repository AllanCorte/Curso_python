# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome  # Nome do cliente
        self.endereco = []  # Lista para armazenar os endereços do cliente

    def inserir_endereco(self, rua, numero):
        # Cria um novo endereço e adiciona à lista de endereços do cliente
        self.endereco.append(Endereco(rua, numero))

    def listar_endereco(self):
        # Lista todos os endereços do cliente
        for endereco in self.endereco:
            print(f'o seu nome é {self.nome} e seu endereço', endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua  # Nome da rua
        self.numero = numero  # Número do endereço

# Cria um cliente chamado 'allan'
cliente1 = Cliente('allan')
# Adiciona um endereço ao cliente1
cliente1.inserir_endereco('av brasil', 123)

# Cria um cliente chamado 'isa'
cliente2 = Cliente('isa')
# Adiciona um endereço ao cliente2
cliente2.inserir_endereco('av itamar', 444)

# Lista os endereços de cada cliente
cliente1.listar_endereco()
cliente2.listar_endereco()

print('aqui termina o meu codigo ')