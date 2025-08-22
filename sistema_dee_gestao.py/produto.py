class Produto:
    def __init__(self, nome: str, preco: float, categoria: str,
                 quantidade_estoque: int) -> None:
        self._nome = nome
        self._preco = preco
        self._categoria = categoria
        self._quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, preco: float):
        self._preco = preco

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria: str):
        self._categoria = categoria

    @property
    def quantidade_de_estoque(self):
        return self._quantidade_estoque

    @quantidade_de_estoque.setter
    def quantidade_de_estoque(self, quantidade_de_estoque: int):
        self._quantidade_estoque = quantidade_de_estoque

    def __str__(self) -> str:
        return f'nome:{self.nome}, Preço:{self.preco},'\
            f'categoria: {self.categoria}, quantidade:'\
            f'{self.quantidade_de_estoque}'

    def __repr__(self):
        class_name = type(self).__name__
        attrs = (
            f'({self.nome!r}, {self.preco!r}, '
            f'{self.categoria!r}, {self.quantidade_de_estoque!r})'
        )
        return f'{class_name}{attrs}'


class Loja:
    def __init__(self, nome_loja: str) -> None:
        self.nome_loja = nome_loja
        self.produtos: list[dict] = []


def log_operacao(func):
    """
    Decorador que registra as operações realizadas na loja.
    Deve imprimir a data/hora e a operação realizada.
    """
    pass  # Substitua este pass pela sua implementação


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("""
=== SISTEMA DE GESTÃO DE PRODUTOS ===
0 - Adicionar produto
1 - Listar todos os produtos
2 - Buscar produto por nome
3 - Atualizar preço de um produto
4 - Remover produto
5 - Calcular valor total do estoque
6 - Salvar produtos em arquivo JSON
7 - Carregar produtos de arquivo JSON
8 - Sair
""")


def adicionar_produto_menu():
    """Interface para adicionar um novo produto."""


def listar_produtos_menu(loja):
    """Interface para listar todos os produtos."""
    pass


def buscar_produto_menu(loja):
    """Interface para buscar um produto por nome."""
    pass


def atualizar_preco_menu(loja):
    """Interface para atualizar o preço de um produto."""
    pass


def remover_produto_menu(loja):
    """Interface para remover um produto."""
    pass
