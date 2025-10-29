# args - argumentos não nomeados
# *- *args
# (empacotamento e desempacotamento)

# lembre-te de desempacotamento
# x,y, *resto = 1,2,3,4
# print(x, y, resto)


def soma(x, y):
    return x + y


soma(1, 2)
# def soma(*args):

#   total = 0
#  for numero in args:
#    total += numero
#  return total

# soma_ = soma(1, 2, 3)
# print(soma_)


def criar_multiplicador(multiplicador):
    def multiplicar(numero):

        return multiplicar

# duplicar = criar_multiplicador(2)
# print(duplicar(3))
