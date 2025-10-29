import json


class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = pessoa('allan', 22)
p2 = pessoa('fabiana', 27)
p3 = pessoa('isadora', 2)

dados = [vars(p1), vars(p2), vars(p3)]
CAMINHO_ARQUIVO = 'aula82.json'
with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)
