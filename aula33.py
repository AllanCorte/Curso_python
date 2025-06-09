"""
escopo de funções e python 
escopo significa o local onde aquele codigo pode atingir
exite o escopo global e o local 
[o escopo global é o escopo onde todo o codigo é alcançavel.]
o escopo local é o escopo onde apenas nomes do mesmo local
 pode ser alcançados
"""

x = 122

def escopo():
    global x 
    x = 12
    
    def outra_função():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_função()
    print(x)

print(x)
escopo()
print(x)
