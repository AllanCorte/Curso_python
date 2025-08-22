from aula82_a import CAMINHO_ARQUIVO, pessoa
import json

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8')as arquivo:
    entrada = json.load(arquivo)
    p1 = pessoa(**entrada[0])
    p2 = pessoa(**entrada[1])
    p3 = pessoa(**entrada[2])

print(p1.nome, p1.idade)
