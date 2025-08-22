# dictionary comprehesion e set comprehension

produto = {
    'nome': 'caneta azul',
    'preço': 2.5,
    'categoria': 'escritorio',

}

dc = {
    chave: valor
    if isinstance(valor, (int, float))else valor.upper()
    for chave, valor
    in produto.items()

}

print(dc)
