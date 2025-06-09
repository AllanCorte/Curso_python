from aula59_package.modulo import soma_modulo
from aula59_package import modulo
import aula59_package.modulo


#from aula59_package.modulo import soma_modulo
print(soma_modulo(1, 3))

#from aula59_package import modulo
print(modulo.soma_modulo(1, 2))

#import aula59_package.modulo
print(aula59_package.modulo.soma_modulo(1, 1))

import aula59_package

print(aula59_package.dobra(3))

print(aula59_package.soma_modulo(2, 3))

from aula59_package import nome

print(nome)