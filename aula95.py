# Exemplo de herança em Python

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Nome da pessoa
        self.idade = idade  # Idade da pessoa


class Estudante(Pessoa):
    def __init__(self, nome, idade, nota):
        super().__init__(nome, idade)  # Chama o construtor da classe
        # Pessoa (herança)
        self.nota = nota  # Nota, exclusivo da classe Estudante


estudante = Estudante("Carlos", 22, 10)  # Cria um objeto estudante
print(estudante.nome)   # Imprime o nome: Carlos
print(estudante.idade)  # Imprime a idade: 22
print(estudante.nota)   # Imprime a nota: 10
