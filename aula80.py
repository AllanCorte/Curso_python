# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
p1 = Pessoa('allan', 'Corte', 21)
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'
p1.idade = 21
p2 = Pessoa('Maria', 'Joana',33)
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'
p3 = Pessoa('alan', 'alves', 44)
print(p1.nome)
print(p1.sobrenome)
print(p1.idade)


print(p2.nome, p2.sobrenome, p2.idade)

print(p3.nome, p3.sobrenome)
print(p3.idade)