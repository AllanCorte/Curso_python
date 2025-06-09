#https://docs.python.org/pt-br/3/library/stdtypes.html


num = 0 

while num <= 100:
     num += 1

     if num == 6:
       print('não vou mostrar o 6')
       continue
     
     if num >= 20 and num <= 35:
         print(f'o numero {num}, esta restrito')
         continue
     
     print(num)
     if num == 40:
         
         break

print('cabou')