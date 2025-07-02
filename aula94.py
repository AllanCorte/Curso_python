# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (A)
#   -> super class, base class, parent class
# Classes filhas (B, C)
#   -> sub class, child class, derived class

class A(object):
    atributo_a = 'valor a'  # Atributo de classe de A

    def __init__(self, atributo):
        self.atributo = atributo  # Atributo de instância

    def metodo(self):
        print('A')  # Método que imprime 'A'


class B(A):
    atributo_b = 'valor b'  # Atributo de classe de B

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)  # Chama o __init__ da classe A
        self.outra_coisa = outra_coisa  # Novo atributo de instância

    def metodo(self):
        print('B')  # Método que imprime 'B' (sobrescreve o de A)


class C(B):
    atributo_c = 'valor c'  # Atributo de classe de C

    def __init__(self, *args, **kwargs):
        # Chama o __init__ da classe B (e, por consequência, de A)
        super().__init__(*args, **kwargs)

    def metodo(self):
        # Chama explicitamente o método metodo das classes A e B
        # super().metodo()  # Chamaria o método de B (MRO)
        # super(B, self).metodo()  # Chamaria o método de A
        # super(A, self).metodo()  # Chamaria o método de object (não faz nada)
        A.metodo(self)  # Imprime 'A'
        B.metodo(self)  # Imprime 'B'
        print('C')      # Imprime 'C'


# print(C.mro())  # Mostra a ordem de resolução de métodos (MRO) da classe C
# print(B.mro())  # Mostra a MRO de B
# print(A.mro())  # Mostra a MRO de A

c = C('Atributo', 'Qualquer')  # Cria um objeto de C, passando argumentos para os __init__ das classes
# print(c.atributo)            # Mostra o atributo herdado de A
# print(c.outra_coisa)         # Mostra o atributo herdado de B
c.metodo()                     # Chama o método metodo de C (imprime A, B, C)
# print(c.atributo_a)          # Mostra o atributo de classe de A
# print(c.atributo_b)          # Mostra o atributo de classe de B
# print(c.atributo_c)          # Mostra o atributo de classe de C
# c.metodo()                   # Chama novamente o método metodo de C