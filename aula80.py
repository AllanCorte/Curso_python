# Mantendo estados dentro da classe
class camera:
    def __init__(self, nome, filmando = False):
        self.nome =nome
        self.filamndo = filmando

    def filmar(self):
        if self.filamndo:
            print(f'{self.nome} ja esta filmando')
            return
        
        print(f'{self.nome} está filmando..')
        self.filamndo =True

    def parando_filmar (self):
        if not self.filamndo:
            print(f'{self.nome} nao esta filmando')
            return
        
        print(f'{self.nome} está parando de filmar')
        self.filamndo = False

    def fotografar (self):
        if self.filamndo:
            print(f'{self.nome} não pode fotografar pois esta filmando')
            return
        
        print(f'{self.nome} esta fotografando ...')


c1 = camera('canon')
c2 = camera('sony')

c1.filmar()
c1.fotografar()
c1.parando_filmar()
c1.fotografar()