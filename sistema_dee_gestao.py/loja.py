class Loja:
    def __init__(self, nome_loja: str) -> None:
        self.nome_loja = nome_loja
        self.produtos: list[dict] = []

    def adicionar_produtos(self, produto):
        self.produtos.append(produto)

    def listar_produtos_menu(self):
        return self.produtos

    def buscar_produto_menu(self, produto):
        for item in self.produtos:
            if item == produto:
                print(item)
                return True


if __name__ == '__main__':
