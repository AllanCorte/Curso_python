# dir, hasattr e getattr em Python
#quais metodos estão disponiveis na minha string

string = 'Luiz'
metodo = 'strip'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo) 