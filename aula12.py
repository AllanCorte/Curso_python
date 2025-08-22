"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num1 = int(input('digite um numero inteiro por favor: '))

if num1 % 2 == 0:

    print('o numero é par')

else:
    print('o numero é impar')
