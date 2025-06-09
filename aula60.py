import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco']* 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
print(*produtos, sep= '\n')
print()
print(*novos_produtos, sep= '\n')
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome  = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['nome'],
    reverse=True
)

print(*produtos, sep= '\n')
print()
print(*produtos_ordenados_por_nome, sep= '\n')
print('-'*50)
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco  = sorted(
    copy.deepcopy(produtos),
    key = lambda p: p['preco'],
)

print(*produtos, sep= '\n')
print()
print(*produtos_ordenados_por_preco, sep= '\n')


#import copy importa o módulo copy, que permite fazer \
# cópias profundas (deep copy) de objetos.
#from dados import produtos: importa a lista produtos do módulo (arquivo) dados.py.


#copy.deepcopy(produtos): faz uma cópia profunda da lista produtos,\
#  garantindo que alterações não afetem o original.
#for p in ...: para cada produto p na lista copiada.
#{**p, 'preco': ...}: cria um novo dicionário copiando todos os dados\
#  de p, mas altera o valor de 'preco'.
#p['preco'] * 1.1: aumenta o preço em 10%.
#round(..., 2): arredonda o preço para 2 casas decimais.
#Resultado: novos_produtos é uma nova lista com os preços aumentados.

#copy.deepcopy(produtos): faz uma cópia profunda da lista original.
#sorted(..., key=lambda p: p['nome'], reverse=True): ordena a lista pelo campo 'nome' em ordem decrescente (de Z para A).
#lambda p: p['nome']: função anônima que retorna o nome do produto para ser usado como chave de ordenação.
#Resultado: produtos_ordenados_por_nome é uma nova lista ordenada por nome decrescente