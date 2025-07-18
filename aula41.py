# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
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
q_acertos = 0
for pergunta in perguntas:
    print('pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)  
    print()

    escolha = (input('escolha uma opção: '))
    escolha_int = None
    q_opcoes = len(opcoes)
    acertou = False

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < q_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        q_acertos += 1
        print('acertou')
    else:
        print('errou')

    
print(f'a quantidade de acertos foi {q_acertos}')
print( 'de', len(perguntas), 'perguntas')