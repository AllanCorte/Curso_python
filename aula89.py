# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome  # Nome do escritor
        self._ferramenta = None  # Ferramenta começa como None

    @property
    def ferramenta(self):
        # Getter para acessar a ferramenta
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        # Setter para definir a ferramenta
        self._ferramenta = ferramenta

class FerramentaDeEescrever:
    def __init__(self, nome):
        self.nome = nome  # Nome da ferramenta

    def escrever(self):
        # Método que retorna uma mensagem de escrita
        return f'{self.nome}, está escrevendo'
    
escritor = Escritor('allan')  # Cria um escritor chamado allan
caneta = FerramentaDeEescrever('caneta bic')  # Cria uma caneta
#escritor.ferramenta = caneta  # Associa a caneta ao escritor (descomentando esta linha)
maquina_de_escrever = FerramentaDeEescrever('maquina de escrever')  # Cria uma máquina de escrever
escritor.ferramenta = maquina_de_escrever  # Associa a máquina ao escritor
print(escritor.ferramenta.escrever())  # Imprime a mensagem da ferramenta associada
