""" CALCULADORA COM WHILE """
while True:
    numero_1 = input('digite um numero: ')
    operador = input('digite um operador (+-/*): ')
    numero_2 = input('digite outro numero: ')

    numero_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True

    except Exception:
        numero_validos = None

    if numero_validos is None:
        print('um ou ambos numero digitados estão errados')
        continue

    operador_permitidos = '+-/*'

    if operador not in operador_permitidos:
        print('operador invalido ')
        continue

    if len(operador) > 1:
        print('digite apenas um operador')
        continue

    print(' realizando sua conta. confira os resultados abaixo')

    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)

    sair = input('quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
