# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []  # Lista para armazenar os produtos do carrinho

    def total(self):
        # Retorna o valor total dos produtos no carrinho
        return sum([p.preco for p in self._produtos])
    
    def inserir_produtos(self, *produtos):
        # Adiciona um ou mais produtos ao carrinho
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        # Lista todos os produtos do carrinho
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome  # Nome do produto
        self.preco = preco  # Preço do produto

carrinho = Carrinho()  # Cria um carrinho de compras
p1, p2 = Produto('caneta', 1.20), Produto('camisa', 20)  # Cria dois produtos
carrinho.inserir_produtos(p1, p2)  # Adiciona os produtos ao carrinho
carrinho.listar_produtos()  # Lista os produtos do carrinho
print(carrinho.total())  # Imprime o valor total dos produtos