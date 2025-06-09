# problema dos paramentros mutaveis em funções python

def adiciona_clientes(nome, lista=[]):
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('joana', cliente1)
print(cliente1)