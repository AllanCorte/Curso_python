nome = 'allan'
idade = 23

def ano_nascimento(x, y):
    return x - y

numero_validos = None
ano = input('qual é o ano que voce nasceu:')
ano_atual = input('qual é o ano atual: ')

try:
    ano_atual_int = int(ano_atual)
    ano_int = int(ano)
    numero_validos = True
    
except Exception:
        numero_validos = None

if numero_validos is None:
        print('um ou ambos numero digitados estão errados')
    

print(ano_nascimento(ano_atual_int, ano_int))