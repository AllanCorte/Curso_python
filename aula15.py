nome = input(str('qual o seu nome: '))
indice = 0
novo_nome = ''

while indice < len(nome):
    print(f'*{nome[indice]}*')

    letra = nome[indice]
    novo_nome += letra
    indice += 1

    novo_nome += '*'
    
print(novo_nome)
