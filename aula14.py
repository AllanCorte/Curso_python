qtd_linha = 5
qtd_coluna = 5

linha = 1

while linha <= qtd_linha:
    coluna = 1

    while coluna <= qtd_coluna:

        print(f'{linha=} {coluna=}')
        print(f'{linha * '-'}  {coluna *'|'}')

        coluna +=1
    
    linha += 1 

print('acabou')
print(22 * '-')
