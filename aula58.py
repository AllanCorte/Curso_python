
# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
import aula58_m #importa todo o modulo
from aula58_m import ano_int, ano_atual_int, nome, ano_nascimento, idade

ano_nascimento(ano_atual_int, ano_int)

print(aula58_m.nome)

print(f'idade verdadeira', idade)

