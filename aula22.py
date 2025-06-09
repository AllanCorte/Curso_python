"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
palavra_secreta = ('churrasco')
letra_acertada = ''
tentativa = 0

while True:
    letra = input('digite uma letra: ')
    tentativa += 1

    if len(letra) > 1:
        print('digite só uma letra')
        continue
    
    if letra in palavra_secreta:
        letra_acertada += letra

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formada += letra_secreta

        else:
            palavra_formada += ('*')

    print('a palvra formada é:', palavra_formada )

    if palavra_formada == palavra_secreta:
        print('parabens voce ganhou ')
        print('a palavra era', palavra_secreta)
        print('tentativas', tentativa)