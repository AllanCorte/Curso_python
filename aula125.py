# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os


# C:\Users\Allan\OneDrive\Imagens
# Correção: 'Users' em vez de 'User'
# Correção: usar 'C:\\' em vez de 'C:'
caminho = os.path.join('C:\\', 'Users', 'Allan', 'OneDrive', 'Imagens')

for pasta in os.listdir(caminho):
    print(pasta)
