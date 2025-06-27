# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': '44',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def saudação ():
    print('parabens voce acertou')

def erro ():
    print('infelizmente voce errou')

q_acertos = 0

for pergunta in perguntas:
    print('pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)  
    print()

    try:
        escolha = (int(input('escolha uma opção de resposta: ')))
        if escolha >= 0 and escolha < len(opcoes):
            if opcoes[escolha] == pergunta['Resposta']:
                saudação()
                q_acertos +=1 
            else:
                erro()
        else: 
            print('escolhe um numero dentro do intervalo')
    except ValueError:
        print('por favor somente numeros inteiros')
        continue

    print()
    
print(f'a quantidade de acertos foi {q_acertos}')
print( 'de', len(perguntas), 'perguntas')