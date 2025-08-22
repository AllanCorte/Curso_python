# Exercício: Sistema de Gestão de Produtos
#
# OBJETIVO: Criar um sistema completo para gerenciar produtos de uma loja
#
# REQUISITOS:
# 1. Classe Produto com atributos: nome, preco, categoria, quantidade_estoque
# 2. Classe Loja que gerencia uma lista de produtos
# 3. Menu interativo com as seguintes opções:
#    - Adicionar produto
#    - Listar todos os produtos
#    - Buscar produto por nome
#    - Atualizar preço de um produto
#    - Remover produto
#    - Calcular valor total do estoque
#    - Salvar produtos em arquivo JSON
#    - Carregar produtos de arquivo JSON
#    - Sair
# 4. Tratamento de erros adequado
# 5. Validações (preço > 0, quantidade >= 0, etc.)
# 6. Usar decoradores para log de operações
# 7. Implementar pelo menos 2 métodos especiais (__str__, __repr__)

# import json
# import os
# from datetime import datetime

# TODO: Implemente aqui a classe Produto


class Produto:
    """
    Classe que representa um produto da loja.

    Atributos:
        nome (str): Nome do produto
        preco (float): Preço do produto
        categoria (str): Categoria do produto
        quantidade_estoque (int): Quantidade em estoque
    """


# TODO: Implemente aqui a classe Loja


class Loja:
    """
    Classe que gerencia os produtos da loja.

    Atributos:
        produtos (list): Lista de produtos
        nome_loja (str): Nome da loja
    """
    pass  # Substitua este pass pela sua implementação

# TODO: Implemente aqui o decorador de log


def log_operacao(func):
    """
    Decorador que registra as operações realizadas na loja.
    Deve imprimir a data/hora e a operação realizada.
    """
    pass  # Substitua este pass pela sua implementação

# TODO: Implemente aqui as funções do menu


def exibir_menu():
    """Exibe o menu principal do sistema."""
    pass


def adicionar_produto_menu(loja):
    """Interface para adicionar um novo produto."""
    pass


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


def calcular_valor_estoque_menu(loja):
    """Interface para calcular o valor total do estoque."""
    pass


def salvar_produtos_menu(loja):
    """Interface para salvar produtos em arquivo JSON."""
    pass


def carregar_produtos_menu(loja):
    """Interface para carregar produtos de arquivo JSON."""
    pass

# TODO: Implemente aqui a função principal


def main():
    """Função principal que executa o sistema."""
    print("=== Sistema de Gestão de Produtos ===")
    nome_loja = input("Digite o nome da sua loja: ")
    loja = Loja(nome_loja)

    while True:
        try:
            exibir_menu()
            opcao = input("\nEscolha uma opção: ").strip()

            # Implemente aqui o switch case para as opções do menu
            # Use match-case (Python 3.10+) ou if-elif

            pass  # Substitua este pass pela sua implementação

        except KeyboardInterrupt:
            print("\n\nSistema encerrado pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()

# DICAS PARA IMPLEMENTAÇÃO:
#
# 1. Na classe Produto:
#    - Use __init__ para inicializar os atributos
#    - Implemente __str__ para exibição amigável
#    - Implemente __repr__ para representação técnica
#    - Adicione propriedades com validação usando @property e @setter
#
# 2. Na classe Loja:
#    - Use uma lista para armazenar os produtos
#    - Implemente métodos para CRUD (Create, Read, Update, Delete)
#    - Use list comprehension para buscar produtos
#
# 3. No decorador de log:
#    - Use datetime.now() para obter a data/hora atual
#    - Use functools.wraps para preservar metadados da função
#
# 4. No tratamento de JSON:
#    - Use try/except para capturar erros de arquivo
#    - Converta objetos Produto para dict antes de salvar
#    - Recrie objetos Produto ao carregar do arquivo
#
# 5. Validações importantes:
#    - Preço deve ser maior que 0
#    - Quantidade deve ser >= 0
#    - Nome não pode estar vazio
#    - Categoria não pode estar vazia
#
# EXEMPLO DE USO ESPERADO:
# >>> produto = Produto("Notebook", 2500.00, "Eletrônicos", 10)
# >>> print(produto)
# Produto: Notebook - R$ 2500.00 (Eletrônicos) - Estoque: 10
# >>> loja = Loja("TechShop")
# >>> loja.adicionar_produto(produto)
# >>> loja.listar_produtos()
# [Produto: Notebook - R$ 2500.00 (Eletrônicos) - Estoque: 10]
