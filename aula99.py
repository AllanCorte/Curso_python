# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    ...
class OutroError(Exception):
    ...

def levantar():
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note('olha a nota 1')
    exception_.add_note('voce errou isso')
    raise exception_


try:   
    levantar()

except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('vou lança denovo')
    exception_.add_note('mais umaa nota ')
    exception_.__notes__ = error.__notes__.copy()
    raise exception_ from error
