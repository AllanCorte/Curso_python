
nome = input('digita seu nome: ')
idade = input('digite sua idade: ')

if nome and idade:
    print(f'seu nome é, {nome}')

    print(f'sua idade invertida é {idade[::-1]}')

    if ' ' in nome:
        print(f' seu nome {nome} contém espaços')

    else:
        print('o seu nome não tem espaço')
