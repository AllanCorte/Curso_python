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
        return f'nome: {self.nome}, Preço: {self.preco}, '\
            f'categoria: {self.categoria}, quantidade: '\
            f'{self.quantidade_de_estoque}'

    def __repr__(self):
        class_name = type(self).__name__
        attrs = (
            f'({self.nome!r}, {self.preco!r}, '
            f'{self.categoria!r}, {self.quantidade_de_estoque!r})'
        )
        return f'{class_name}{attrs}'


if __name__ == '__main__':

    A1 = Produto('allan', 1.23, 'celular', 4)
    print(A1)
