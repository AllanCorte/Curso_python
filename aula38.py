pessoa = {}

chave = 'nome'
pessoa[chave] = 'allan alves'



pessoa['sobrenome'] = 'corte'
print(pessoa)

print(pessoa[chave])

del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print('essa chave não existe')

else:
    print(pessoa['sobrenome'])