# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('ocorreu erro', e)
    finally:
        print ('fechando o arquivo')
        arquivo.close()

with my_open('aula103.txt', 'w') as arquivo:
    arquivo.write('allan alves\n', 123)
    print('WITH', arquivo)