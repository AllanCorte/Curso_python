# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor

    def get_cor(self):
        print('GET COR')
        return self.cor_tinta
    
    #no pyhton posso fazer  ele se comporta como atributo
    @property
    def cor (self):
        print('allan')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 1234556

#####################################
caneta = Caneta('azul')
print(caneta.get_cor())

print(caneta.cor)