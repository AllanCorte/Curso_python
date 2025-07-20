from dataclasses import dataclass


@dataclass(init=False)
class Pessoa:
    nome: str
    sobrenome: str

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, valor):
        nome, *sobrenome = valor.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def __post_init__(self):
        print('POST INIT')


if __name__ == '__main__':
    p1 = Pessoa('Luiz', 'Otávio')
    p1.nome_completo = 'Maria Helena'
    print(p1)
    print(p1.nome_completo)
