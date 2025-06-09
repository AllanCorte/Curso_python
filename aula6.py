try:
    valor1 = int(input('Digite o seu primeiro valor: '))
    valor2 = int(input('Digite o seu segundo valor: '))

    if valor1 > valor2:
        print(f'O {valor1} é maior que {valor2}')

    elif valor1 < valor2:
        print(f'O {valor1} é menor que {valor2}')

    else:
        print(f'O valor de {valor1} é igual ao valor {valor2}')

except ValueError:
    print('Por favor, digite apenas números inteiros.')