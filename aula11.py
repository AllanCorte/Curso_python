# introdução ao try/execpet
# try -> tentar executar o codigo
# except -> ocorreu algum errado ao tentar executar
numero_str = input('vou dobrar o nummero que digitar: ')

try:
    print(numero_str)

    numero_float = float(numero_str)
    print('float', numero_float)
    print(f'o dobro do numero {numero_str} é o numero {numero_float * 2}')


except:
    print('isso não é um numero')
