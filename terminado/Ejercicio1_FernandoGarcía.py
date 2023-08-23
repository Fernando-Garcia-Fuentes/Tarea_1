# Fernando García Fuentes A01800375
# Librerías
from math import sqrt, pow

# Variables
catA = int(input('Escribe el cateto adyacente: '))
catO = int(input('Escribe el cateto opuesto: '))

# Operaciones
hipotenusa = sqrt(pow(catA , 2) + pow(catO , 2))

# Prints
print(f'La hipotenusa es {hipotenusa}')