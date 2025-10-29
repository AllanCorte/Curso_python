frase = ('A vida começa onde termina sua zona de conforto.').lower()

print(frase)

i = 0
apareceu_mais_vezes = 0
letra_mais_vezes = ''

while i < len(frase):

    letra_atual = frase[i]
    i += 1

    if letra_atual == ' ':
        continue

    q_letra = frase.count(letra_atual)

    if apareceu_mais_vezes < q_letra:
        apareceu_mais_vezes = q_letra
        letra_mais_vezes = letra_atual

    i += 1

print(' a letra que apareceu mais vezes '
      f'"{letra_mais_vezes}" que apareceu {apareceu_mais_vezes}'
      )
