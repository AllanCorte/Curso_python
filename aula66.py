l1 = [1, 2, 3, 4, 5]
l2 = [2, 3, 4, 5]
indice = 0
l3 = []
while indice < len(l2):
    soma = l1[indice] + l2[indice]
    l3.append(soma)
    indice += 1

    
print(l3)