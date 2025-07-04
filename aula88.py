# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       só DEVE ser usado dentro da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

class Foo:
    def __init__(self):
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privadado'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        print("_metodo_protected")
        return "_metodo_protected"
    
    def __metodo_private(self):
        print("__metodo_private")
        return self.__private

f = Foo()
print(f.public)
print(f._protected)
